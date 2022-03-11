java -jar lib/antlr.jar -o src/build/compiler/parser_py -Dlanguage=Python3 -listener -visitor grammar/Python3.g4

:: Einbauen zum arbeiten in Eclipse
:: -package src.build.compiler.parser

:: Ausgabe des Parsers in python
:: -Dlanguage=Python3