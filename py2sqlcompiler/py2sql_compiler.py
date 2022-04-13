import pathlib
from antlr4 import *
from py2sqlcompiler.py_parser_027.Python3d2Lexer import Python3d2Lexer
from py2sqlcompiler.py_parser_027.Python3d2Parser import Python3d2Parser
from py2sqlcompiler.py_parser_027.Python3d2Listener import Python3d2Listener
from py2sqlcompiler.py_parser_027.Python3d2Visitor import Python3d2Visitor

def main(argv, templates):
    if argv[0] == 0:
        input_stream = FileStream(argv[1])
    else:
        input_stream = InputStream(argv[1])

    lexer = Python3d2Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Python3d2Parser(stream)
    tree = parser.file_input()

    listener = Python3d2Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    visitor = Python3d2Visitor(templates)
    visitor.visit(tree)

    # Add statements that should be queried before PL/SQL Block
    pre = "\n".join(line for line in visitor.pre)
    
    output = ""
    # Add assignment statements for DECLARE block
    for var in visitor.assignments:
            output += (f"    {var} {visitor.assignments[var]};\n")

    # Cursor after variable declaration
    for line in visitor.cursor:
        # Add Cursor to declare block
            output += (f"    {line};\n")
    
    # Add Statements for BEGIN block
    output += "\n" + "\n    ".join(str(line) for line in visitor.statements)

    return pre, output


if __name__ == '__main__':
    main([0, str(pathlib.Path(__file__).parent.resolve()) + "/code/code1.py"])
