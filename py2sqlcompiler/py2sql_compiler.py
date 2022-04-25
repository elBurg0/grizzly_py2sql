import pathlib
from antlr4 import *
from py2sqlcompiler.py_parser_028.Python3d3Lexer import Python3d3Lexer
from py2sqlcompiler.py_parser_028.Python3d3Parser import Python3d3Parser
from py2sqlcompiler.py_parser_028.Python3d3Listener import Python3d3Listener
from py2sqlcompiler.py_parser_028.Python3d3Visitor import Python3d3Visitor

def main(argv, templates):
    if argv[0] == 0:
        input_stream = FileStream(argv[1])
    else:
        input_stream = InputStream(argv[1])

    lexer = Python3d3Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Python3d3Parser(stream)
    tree = parser.file_input()

    listener = Python3d3Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    visitor = Python3d3Visitor(templates)
    visitor.visit(tree)

    # Add statements that should be queried before PL/SQL Block
    pre = "\n".join(line for line in visitor.pre)
    
    sql_function = ""
    # TODO use better iteration
    # Add assignment statements for DECLARE block
    for var in visitor.assignments:
            sql_function += (f"    {var} {visitor.assignments[var]};\n")

    # Cursor after variable declaration
    for line in visitor.cursor:
        # Add Cursor to declare block
            sql_function += (f"    {line};\n")
    
    # Add Statements for BEGIN block
    sql_function += "\n    ".join(str(line) for line in visitor.statements)

    return pre, sql_function


if __name__ == '__main__':
    main([0, str(pathlib.Path(__file__).parent.resolve()) + "/code/code1.py"])
