# Generated from grammar/Python3d.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr4.Token import CommonToken
import re
import importlib
# Allow languages to extend the lexer and parser, by loading the parser dynamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u0187\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\5")
        buf.write("#\u0109\n#\3$\3$\7$\u010d\n$\f$\16$\u0110\13$\3$\3$\7")
        buf.write("$\u0114\n$\f$\16$\u0117\13$\3%\3%\3&\3&\3&\5&\u011e\n")
        buf.write("&\3&\3&\5&\u0122\n&\3&\5&\u0125\n&\5&\u0127\n&\3&\3&\3")
        buf.write("\'\3\'\3\'\3\'\6\'\u012f\n\'\r\'\16\'\u0130\3(\3(\7(\u0135")
        buf.write("\n(\f(\16(\u0138\13(\3)\3)\7)\u013c\n)\f)\16)\u013f\13")
        buf.write(")\3)\3)\3*\3*\7*\u0145\n*\f*\16*\u0148\13*\3*\6*\u014b")
        buf.write("\n*\r*\16*\u014c\5*\u014f\n*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\61\5\61\u0160\n\61\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\6\65\u016b\n\65\r")
        buf.write("\65\16\65\u016c\3\66\3\66\7\66\u0171\n\66\f\66\16\66\u0174")
        buf.write("\13\66\3\67\3\67\5\67\u0178\n\67\3\67\5\67\u017b\n\67")
        buf.write("\3\67\3\67\5\67\u017f\n\67\38\58\u0182\n8\39\39\59\u0186")
        buf.write("\n9\3\u013d\2:\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\2g\2i\2k\2")
        buf.write("m\2o\2q\2\3\2\7\3\2\63;\3\2\62;\4\2\13\13\"\"\4\2\f\f")
        buf.write("\16\17\5\2C\\aac|\2\u0194\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\3s\3\2\2\2\5\177\3\2\2\2\7\u0081\3\2\2\2\t\u0095")
        buf.write("\3\2\2\2\13\u0097\3\2\2\2\r\u009d\3\2\2\2\17\u00a6\3\2")
        buf.write("\2\2\21\u00ad\3\2\2\2\23\u00b0\3\2\2\2\25\u00b5\3\2\2")
        buf.write("\2\27\u00ba\3\2\2\2\31\u00c0\3\2\2\2\33\u00c4\3\2\2\2")
        buf.write("\35\u00c7\3\2\2\2\37\u00cd\3\2\2\2!\u00cf\3\2\2\2#\u00d5")
        buf.write("\3\2\2\2%\u00d7\3\2\2\2\'\u00d9\3\2\2\2)\u00dc\3\2\2\2")
        buf.write("+\u00df\3\2\2\2-\u00e2\3\2\2\2/\u00e5\3\2\2\2\61\u00e7")
        buf.write("\3\2\2\2\63\u00e9\3\2\2\2\65\u00eb\3\2\2\2\67\u00ed\3")
        buf.write("\2\2\29\u00f1\3\2\2\2;\u00f5\3\2\2\2=\u00fa\3\2\2\2?\u0100")
        buf.write("\3\2\2\2A\u0102\3\2\2\2C\u0104\3\2\2\2E\u0108\3\2\2\2")
        buf.write("G\u010a\3\2\2\2I\u0118\3\2\2\2K\u0126\3\2\2\2M\u012a\3")
        buf.write("\2\2\2O\u0132\3\2\2\2Q\u0139\3\2\2\2S\u014e\3\2\2\2U\u0150")
        buf.write("\3\2\2\2W\u0152\3\2\2\2Y\u0154\3\2\2\2[\u0156\3\2\2\2")
        buf.write("]\u0158\3\2\2\2_\u015a\3\2\2\2a\u015f\3\2\2\2c\u0163\3")
        buf.write("\2\2\2e\u0165\3\2\2\2g\u0167\3\2\2\2i\u016a\3\2\2\2k\u016e")
        buf.write("\3\2\2\2m\u0175\3\2\2\2o\u0181\3\2\2\2q\u0185\3\2\2\2")
        buf.write("st\7i\2\2tu\7t\2\2uv\7k\2\2vw\7|\2\2wx\7|\2\2xy\7n\2\2")
        buf.write("yz\7{\2\2z{\7\60\2\2{|\7w\2\2|}\7u\2\2}~\7g\2\2~\4\3\2")
        buf.write("\2\2\177\u0080\7?\2\2\u0080\6\3\2\2\2\u0081\u0082\7i\2")
        buf.write("\2\u0082\u0083\7t\2\2\u0083\u0084\7k\2\2\u0084\u0085\7")
        buf.write("|\2\2\u0085\u0086\7|\2\2\u0086\u0087\7n\2\2\u0087\u0088")
        buf.write("\7{\2\2\u0088\u0089\7\60\2\2\u0089\u008a\7t\2\2\u008a")
        buf.write("\u008b\7g\2\2\u008b\u008c\7c\2\2\u008c\u008d\7f\2\2\u008d")
        buf.write("\u008e\7a\2\2\u008e\u008f\7v\2\2\u008f\u0090\7c\2\2\u0090")
        buf.write("\u0091\7d\2\2\u0091\u0092\7n\2\2\u0092\u0093\7g\2\2\u0093")
        buf.write("\u0094\7*\2\2\u0094\b\3\2\2\2\u0095\u0096\7<\2\2\u0096")
        buf.write("\n\3\2\2\2\u0097\u0098\7d\2\2\u0098\u0099\7t\2\2\u0099")
        buf.write("\u009a\7g\2\2\u009a\u009b\7c\2\2\u009b\u009c\7m\2\2\u009c")
        buf.write("\f\3\2\2\2\u009d\u009e\7e\2\2\u009e\u009f\7q\2\2\u009f")
        buf.write("\u00a0\7p\2\2\u00a0\u00a1\7v\2\2\u00a1\u00a2\7k\2\2\u00a2")
        buf.write("\u00a3\7p\2\2\u00a3\u00a4\7w\2\2\u00a4\u00a5\7g\2\2\u00a5")
        buf.write("\16\3\2\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7g\2\2\u00a8")
        buf.write("\u00a9\7v\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab\7t\2\2\u00ab")
        buf.write("\u00ac\7p\2\2\u00ac\20\3\2\2\2\u00ad\u00ae\7k\2\2\u00ae")
        buf.write("\u00af\7h\2\2\u00af\22\3\2\2\2\u00b0\u00b1\7g\2\2\u00b1")
        buf.write("\u00b2\7n\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4\7h\2\2\u00b4")
        buf.write("\24\3\2\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7n\2\2\u00b7")
        buf.write("\u00b8\7u\2\2\u00b8\u00b9\7g\2\2\u00b9\26\3\2\2\2\u00ba")
        buf.write("\u00bb\7y\2\2\u00bb\u00bc\7j\2\2\u00bc\u00bd\7k\2\2\u00bd")
        buf.write("\u00be\7n\2\2\u00be\u00bf\7g\2\2\u00bf\30\3\2\2\2\u00c0")
        buf.write("\u00c1\7h\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3\7t\2\2\u00c3")
        buf.write("\32\3\2\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6\7p\2\2\u00c6")
        buf.write("\34\3\2\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7c\2\2\u00c9")
        buf.write("\u00ca\7p\2\2\u00ca\u00cb\7i\2\2\u00cb\u00cc\7g\2\2\u00cc")
        buf.write("\36\3\2\2\2\u00cd\u00ce\7.\2\2\u00ce \3\2\2\2\u00cf\u00d0")
        buf.write("\7r\2\2\u00d0\u00d1\7t\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3")
        buf.write("\7p\2\2\u00d3\u00d4\7v\2\2\u00d4\"\3\2\2\2\u00d5\u00d6")
        buf.write("\7>\2\2\u00d6$\3\2\2\2\u00d7\u00d8\7@\2\2\u00d8&\3\2\2")
        buf.write("\2\u00d9\u00da\7?\2\2\u00da\u00db\7?\2\2\u00db(\3\2\2")
        buf.write("\2\u00dc\u00dd\7@\2\2\u00dd\u00de\7?\2\2\u00de*\3\2\2")
        buf.write("\2\u00df\u00e0\7>\2\2\u00e0\u00e1\7?\2\2\u00e1,\3\2\2")
        buf.write("\2\u00e2\u00e3\7#\2\2\u00e3\u00e4\7?\2\2\u00e4.\3\2\2")
        buf.write("\2\u00e5\u00e6\7-\2\2\u00e6\60\3\2\2\2\u00e7\u00e8\7/")
        buf.write("\2\2\u00e8\62\3\2\2\2\u00e9\u00ea\7,\2\2\u00ea\64\3\2")
        buf.write("\2\2\u00eb\u00ec\7\61\2\2\u00ec\66\3\2\2\2\u00ed\u00ee")
        buf.write("\7k\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0\7v\2\2\u00f08\3")
        buf.write("\2\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f3\7v\2\2\u00f3\u00f4")
        buf.write("\7t\2\2\u00f4:\3\2\2\2\u00f5\u00f6\7n\2\2\u00f6\u00f7")
        buf.write("\7k\2\2\u00f7\u00f8\7u\2\2\u00f8\u00f9\7v\2\2\u00f9<\3")
        buf.write("\2\2\2\u00fa\u00fb\7h\2\2\u00fb\u00fc\7n\2\2\u00fc\u00fd")
        buf.write("\7q\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff\7v\2\2\u00ff>\3")
        buf.write("\2\2\2\u0100\u0101\7$\2\2\u0101@\3\2\2\2\u0102\u0103\7")
        buf.write("\60\2\2\u0103B\3\2\2\2\u0104\u0105\5Q)\2\u0105D\3\2\2")
        buf.write("\2\u0106\u0109\5I%\2\u0107\u0109\5G$\2\u0108\u0106\3\2")
        buf.write("\2\2\u0108\u0107\3\2\2\2\u0109F\3\2\2\2\u010a\u010e\5")
        buf.write("e\63\2\u010b\u010d\5g\64\2\u010c\u010b\3\2\2\2\u010d\u0110")
        buf.write("\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f")
        buf.write("\u0111\3\2\2\2\u0110\u010e\3\2\2\2\u0111\u0115\7\60\2")
        buf.write("\2\u0112\u0114\5g\64\2\u0113\u0112\3\2\2\2\u0114\u0117")
        buf.write("\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116")
        buf.write("H\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119\5S*\2\u0119")
        buf.write("J\3\2\2\2\u011a\u011b\6&\2\2\u011b\u0127\5i\65\2\u011c")
        buf.write("\u011e\7\17\2\2\u011d\u011c\3\2\2\2\u011d\u011e\3\2\2")
        buf.write("\2\u011e\u011f\3\2\2\2\u011f\u0122\7\f\2\2\u0120\u0122")
        buf.write("\4\16\17\2\u0121\u011d\3\2\2\2\u0121\u0120\3\2\2\2\u0122")
        buf.write("\u0124\3\2\2\2\u0123\u0125\5i\65\2\u0124\u0123\3\2\2\2")
        buf.write("\u0124\u0125\3\2\2\2\u0125\u0127\3\2\2\2\u0126\u011a\3")
        buf.write("\2\2\2\u0126\u0121\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0129")
        buf.write("\b&\2\2\u0129L\3\2\2\2\u012a\u012b\7i\2\2\u012b\u012c")
        buf.write("\7a\2\2\u012c\u012e\3\2\2\2\u012d\u012f\5q9\2\u012e\u012d")
        buf.write("\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u012e\3\2\2\2\u0130")
        buf.write("\u0131\3\2\2\2\u0131N\3\2\2\2\u0132\u0136\5o8\2\u0133")
        buf.write("\u0135\5q9\2\u0134\u0133\3\2\2\2\u0135\u0138\3\2\2\2\u0136")
        buf.write("\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137P\3\2\2\2\u0138")
        buf.write("\u0136\3\2\2\2\u0139\u013d\7$\2\2\u013a\u013c\13\2\2\2")
        buf.write("\u013b\u013a\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013e\3")
        buf.write("\2\2\2\u013d\u013b\3\2\2\2\u013e\u0140\3\2\2\2\u013f\u013d")
        buf.write("\3\2\2\2\u0140\u0141\7$\2\2\u0141R\3\2\2\2\u0142\u0146")
        buf.write("\5e\63\2\u0143\u0145\5g\64\2\u0144\u0143\3\2\2\2\u0145")
        buf.write("\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2")
        buf.write("\u0147\u014f\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014b\7")
        buf.write("\62\2\2\u014a\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c")
        buf.write("\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014f\3\2\2\2")
        buf.write("\u014e\u0142\3\2\2\2\u014e\u014a\3\2\2\2\u014fT\3\2\2")
        buf.write("\2\u0150\u0151\7*\2\2\u0151V\3\2\2\2\u0152\u0153\7+\2")
        buf.write("\2\u0153X\3\2\2\2\u0154\u0155\7]\2\2\u0155Z\3\2\2\2\u0156")
        buf.write("\u0157\7_\2\2\u0157\\\3\2\2\2\u0158\u0159\7}\2\2\u0159")
        buf.write("^\3\2\2\2\u015a\u015b\7\177\2\2\u015b`\3\2\2\2\u015c\u0160")
        buf.write("\5i\65\2\u015d\u0160\5k\66\2\u015e\u0160\5m\67\2\u015f")
        buf.write("\u015c\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u015e\3\2\2\2")
        buf.write("\u0160\u0161\3\2\2\2\u0161\u0162\b\61\3\2\u0162b\3\2\2")
        buf.write("\2\u0163\u0164\13\2\2\2\u0164d\3\2\2\2\u0165\u0166\t\2")
        buf.write("\2\2\u0166f\3\2\2\2\u0167\u0168\t\3\2\2\u0168h\3\2\2\2")
        buf.write("\u0169\u016b\t\4\2\2\u016a\u0169\3\2\2\2\u016b\u016c\3")
        buf.write("\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016dj")
        buf.write("\3\2\2\2\u016e\u0172\7%\2\2\u016f\u0171\n\5\2\2\u0170")
        buf.write("\u016f\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2")
        buf.write("\u0172\u0173\3\2\2\2\u0173l\3\2\2\2\u0174\u0172\3\2\2")
        buf.write("\2\u0175\u0177\7^\2\2\u0176\u0178\5i\65\2\u0177\u0176")
        buf.write("\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u017e\3\2\2\2\u0179")
        buf.write("\u017b\7\17\2\2\u017a\u0179\3\2\2\2\u017a\u017b\3\2\2")
        buf.write("\2\u017b\u017c\3\2\2\2\u017c\u017f\7\f\2\2\u017d\u017f")
        buf.write("\4\16\17\2\u017e\u017a\3\2\2\2\u017e\u017d\3\2\2\2\u017f")
        buf.write("n\3\2\2\2\u0180\u0182\t\6\2\2\u0181\u0180\3\2\2\2\u0182")
        buf.write("p\3\2\2\2\u0183\u0186\5o8\2\u0184\u0186\t\3\2\2\u0185")
        buf.write("\u0183\3\2\2\2\u0185\u0184\3\2\2\2\u0186r\3\2\2\2\30\2")
        buf.write("\u0108\u010e\u0115\u011d\u0121\u0124\u0126\u0130\u0136")
        buf.write("\u013d\u0146\u014c\u014e\u015f\u016c\u0172\u0177\u017a")
        buf.write("\u017e\u0181\u0185\4\3&\2\b\2\2")
        return buf.getvalue()


class Python3dLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    STRING = 33
    NUMBER = 34
    FLOAT = 35
    INTEGER = 36
    NEWLINE = 37
    GRZLYNAME = 38
    NAME = 39
    STRING_LITERAL = 40
    DECIMAL_INTEGER = 41
    OPEN_PAREN = 42
    CLOSE_PAREN = 43
    OPEN_BRACK = 44
    CLOSE_BRACK = 45
    OPEN_BRACE = 46
    CLOSE_BRACE = 47
    SKIP_ = 48
    UNKNOWN_CHAR = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'grizzly.use'", "'='", "'grizzly.read_table('", "':'", "'break'", 
            "'continue'", "'return'", "'if'", "'elif'", "'else'", "'while'", 
            "'for'", "'in'", "'range'", "','", "'print'", "'<'", "'>'", 
            "'=='", "'>='", "'<='", "'!='", "'+'", "'-'", "'*'", "'/'", 
            "'int'", "'str'", "'list'", "'float'", "'\"'", "'.'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "NUMBER", "FLOAT", "INTEGER", "NEWLINE", "GRZLYNAME", 
            "NAME", "STRING_LITERAL", "DECIMAL_INTEGER", "OPEN_PAREN", "CLOSE_PAREN", 
            "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", "CLOSE_BRACE", "SKIP_", 
            "UNKNOWN_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "STRING", "NUMBER", "FLOAT", "INTEGER", "NEWLINE", "GRZLYNAME", 
                  "NAME", "STRING_LITERAL", "DECIMAL_INTEGER", "OPEN_PAREN", 
                  "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", 
                  "CLOSE_BRACE", "SKIP_", "UNKNOWN_CHAR", "NON_ZERO_DIGIT", 
                  "DIGIT", "SPACES", "COMMENT", "LINE_JOINING", "ID_START", 
                  "ID_CONTINUE" ]

    grammarFileName = "Python3d.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    @property
    def tokens(self):
        try:
            return self._tokens
        except AttributeError:
            self._tokens = []
            return self._tokens
    @property
    def indents(self):
        try:
            return self._indents
        except AttributeError:
            self._indents = []
            return self._indents
    @property
    def opened(self):
        try:
            return self._opened
        except AttributeError:
            self._opened = 0
            return self._opened
    @opened.setter
    def opened(self, value):
        self._opened = value
    @property
    def lastToken(self):
        try:
            return self._lastToken
        except AttributeError:
            self._lastToken = None
            return self._lastToken
    @lastToken.setter
    def lastToken(self, value):
        self._lastToken = value
    def reset(self):
        super().reset()
        self.tokens = []
        self.indents = []
        self.opened = 0
        self.lastToken = None
    def emitToken(self, t):
        super().emitToken(t)
        self.tokens.append(t)
    def nextToken(self):
        if self._input.LA(1) == Token.EOF and self.indents:
            for i in range(len(self.tokens)-1,-1,-1):
                if self.tokens[i].type == Token.EOF:
                    self.tokens.pop(i)
            self.emitToken(self.commonToken(LanguageParser.NEWLINE, '\n'))
            while self.indents:
                self.emitToken(self.createDedent())
                self.indents.pop()
            self.emitToken(self.commonToken(LanguageParser.EOF, "<EOF>"))
        next = super().nextToken()
        if next.channel == Token.DEFAULT_CHANNEL:
            self.lastToken = next
        return next if not self.tokens else self.tokens.pop(0)
    def createDedent(self):
        dedent = self.commonToken(LanguageParser.DEDENT, "")
        dedent.line = self.lastToken.line
        return dedent
    def commonToken(self, type, text, indent=0):
        stop = self.getCharIndex()-1-indent
        start = (stop - len(text) + 1) if text else stop
        return CommonToken(self._tokenFactorySourcePair, type, super().DEFAULT_TOKEN_CHANNEL, start, stop)
    @staticmethod
    def getIndentationCount(spaces):
        count = 0
        for ch in spaces:
            if ch == '\t':
                count += 8 - (count % 8)
            else:
                count += 1
        return count
    def atStartOfInput(self):
        return Lexer.column.fget(self) == 0 and Lexer.line.fget(self) == 1


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[36] = self.NEWLINE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            tempt = Lexer.text.fget(self)
            newLine = re.sub("[^\r\n\f]+", "", tempt)
            spaces = re.sub("[\r\n\f]+", "", tempt)
            la_char = ""
            try:
                la = self._input.LA(1)
                la_char = chr(la)       # Python does not compare char to ints directly
            except ValueError:          # End of file
                pass
            # Strip newlines inside open clauses except if we are near EOF. We keep NEWLINEs near EOF to
            # satisfy the final newline needed by the single_put rule used by the REPL.
            try:
                nextnext_la = self._input.LA(2)
                nextnext_la_char = chr(nextnext_la)
            except ValueError:
                nextnext_eof = True
            else:
                nextnext_eof = False
            if self.opened > 0 or nextnext_eof is False and (la_char == '\r' or la_char == '\n' or la_char == '\f' or la_char == '#'):
                self.skip()
            else:
                indent = self.getIndentationCount(spaces)
                previous = self.indents[-1] if self.indents else 0
                self.emitToken(self.commonToken(self.NEWLINE, newLine, indent=indent))      # NEWLINE is actually the '\n' char
                if indent == previous:
                    self.skip()
                elif indent > previous:
                    self.indents.append(indent)
                    self.emitToken(self.commonToken(LanguageParser.INDENT, spaces))
                else:
                    while self.indents and self.indents[-1] > indent:
                        self.emitToken(self.createDedent())
                        self.indents.pop()
                
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[36] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


