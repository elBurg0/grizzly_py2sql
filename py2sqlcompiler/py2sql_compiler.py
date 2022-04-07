import pathlib
from antlr4 import *
from py2sqlcompiler.py_parser5.Python3Lexer import Python3Lexer
from py2sqlcompiler.py_parser5.Python3Parser import Python3Parser
from py2sqlcompiler.py_parser5.Python3Listener import Python3Listener
from py2sqlcompiler.py_parser5.Python3Visitor import Python3Visitor


def main(argv, templates):
    if argv[0] == 0:
        input_stream = FileStream(argv[1])
    else:
        input_stream = InputStream(argv[1])

    lexer = Python3Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()

    listener = Python3Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    visitor = Python3Visitor(templates)
    visitor.visit(tree)

    # Add statements that should be queried before PL/SQL Block
    pre = "\n".join(line for line in visitor.pre)
    
    output = ""
    # Add assignment statements for DECLARE block
    for var in visitor.assignments:
            output += (f"    {var} {visitor.assignments[var]};\n")

    # Postgresql: cursor after variable declaration
    for line in visitor.cursor:
        # Add Cursor to declare block
            output += (f"    {line};\n")
    
    # Add Statements for BEGIN block
    output += "\n" + "\n    ".join(str(line) for line in visitor.statements)

    return pre, output


if __name__ == '__main__':
    main([0, str(pathlib.Path(__file__).parent.resolve()) + "/code/code1.py"])
