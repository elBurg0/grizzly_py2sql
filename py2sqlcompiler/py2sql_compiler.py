import pathlib
from antlr4 import *
from py2sqlcompiler.py_parser_024.Python3dLexer import Python3dLexer
from py2sqlcompiler.py_parser_024.Python3dParser import Python3dParser
from py2sqlcompiler.py_parser_024.Python3dListener import Python3dListener
from py2sqlcompiler.py_parser_024.Python3dVisitor import Python3dVisitor

import grizzly


def main(argv, templates):
    if argv[0] == 0:
        input_stream = FileStream(argv[1])
    else:
        input_stream = InputStream(argv[1])

    lexer = Python3dLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Python3dParser(stream)
    tree = parser.file_input()

    listener = Python3dListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    visitor = Python3dVisitor(templates)
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
