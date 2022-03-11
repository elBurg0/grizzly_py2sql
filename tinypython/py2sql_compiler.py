import sys
import pathlib
from antlr4 import *
from tinypython.src.build.compiler.parser_py.Python3Lexer import Python3Lexer
from tinypython.src.build.compiler.parser_py.Python3Parser import Python3Parser
from tinypython.src.build.compiler.parser_py.Python3Listener import Python3Listener
from tinypython.src.build.compiler.parser_py.Python3Visitor import Python3Visitor
 



def main(argv):
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

    visitor = Python3Visitor()
    output = visitor.visit(tree)

    return """
BEGIN 
    RETURN CONCAT (a, '_compiled');
END;
"""



if __name__ == '__main__':
    main([0, str(pathlib.Path(__file__).parent.resolve()) + "/code/code1.py"])