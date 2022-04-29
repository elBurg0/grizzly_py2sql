# Generated from grammar/Python3d3.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u0187\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3#\3#\3#\3$\3$\3%\3%\3&\7&\u010b\n&\f&\16&\u010e")
        buf.write("\13&\3&\3&\7&\u0112\n&\f&\16&\u0115\13&\3\'\3\'\3(\3(")
        buf.write("\3(\5(\u011c\n(\3(\3(\5(\u0120\n(\3(\5(\u0123\n(\5(\u0125")
        buf.write("\n(\3(\3(\3)\3)\3)\3)\6)\u012d\n)\r)\16)\u012e\3*\3*\7")
        buf.write("*\u0133\n*\f*\16*\u0136\13*\3+\3+\7+\u013a\n+\f+\16+\u013d")
        buf.write("\13+\3+\3+\3,\3,\7,\u0143\n,\f,\16,\u0146\13,\3,\6,\u0149")
        buf.write("\n,\r,\16,\u014a\5,\u014d\n,\3-\3-\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64\5\64")
        buf.write("\u0160\n\64\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\3")
        buf.write("8\68\u016b\n8\r8\168\u016c\39\39\79\u0171\n9\f9\169\u0174")
        buf.write("\139\3:\3:\5:\u0178\n:\3:\5:\u017b\n:\3:\3:\5:\u017f\n")
        buf.write(":\3;\5;\u0182\n;\3<\3<\5<\u0186\n<\3\u013b\2=\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\2m\2o\2q\2s\2u\2w\2")
        buf.write("\3\2\7\3\2\63;\3\2\62;\4\2\13\13\"\"\4\2\f\f\16\17\5\2")
        buf.write("C\\aac|\2\u0193\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\3y\3\2\2\2\5{\3\2\2")
        buf.write("\2\7\u0080\3\2\2\2\t\u0088\3\2\2\2\13\u008e\3\2\2\2\r")
        buf.write("\u0097\3\2\2\2\17\u009e\3\2\2\2\21\u00a4\3\2\2\2\23\u00a9")
        buf.write("\3\2\2\2\25\u00b0\3\2\2\2\27\u00b3\3\2\2\2\31\u00b6\3")
        buf.write("\2\2\2\33\u00bb\3\2\2\2\35\u00c1\3\2\2\2\37\u00c5\3\2")
        buf.write("\2\2!\u00c8\3\2\2\2#\u00ce\3\2\2\2%\u00d0\3\2\2\2\'\u00d6")
        buf.write("\3\2\2\2)\u00d8\3\2\2\2+\u00da\3\2\2\2-\u00dd\3\2\2\2")
        buf.write("/\u00e0\3\2\2\2\61\u00e3\3\2\2\2\63\u00e6\3\2\2\2\65\u00e8")
        buf.write("\3\2\2\2\67\u00ea\3\2\2\29\u00ec\3\2\2\2;\u00ee\3\2\2")
        buf.write("\2=\u00f0\3\2\2\2?\u00f2\3\2\2\2A\u00f6\3\2\2\2C\u00fa")
        buf.write("\3\2\2\2E\u00ff\3\2\2\2G\u0105\3\2\2\2I\u0107\3\2\2\2")
        buf.write("K\u010c\3\2\2\2M\u0116\3\2\2\2O\u0124\3\2\2\2Q\u0128\3")
        buf.write("\2\2\2S\u0130\3\2\2\2U\u0137\3\2\2\2W\u014c\3\2\2\2Y\u014e")
        buf.write("\3\2\2\2[\u0150\3\2\2\2]\u0152\3\2\2\2_\u0154\3\2\2\2")
        buf.write("a\u0156\3\2\2\2c\u0158\3\2\2\2e\u015a\3\2\2\2g\u015f\3")
        buf.write("\2\2\2i\u0163\3\2\2\2k\u0165\3\2\2\2m\u0167\3\2\2\2o\u016a")
        buf.write("\3\2\2\2q\u016e\3\2\2\2s\u0175\3\2\2\2u\u0181\3\2\2\2")
        buf.write("w\u0185\3\2\2\2yz\7<\2\2z\4\3\2\2\2{|\7g\2\2|}\7n\2\2")
        buf.write("}~\7u\2\2~\177\7g\2\2\177\6\3\2\2\2\u0080\u0081\7h\2\2")
        buf.write("\u0081\u0082\7k\2\2\u0082\u0083\7p\2\2\u0083\u0084\7c")
        buf.write("\2\2\u0084\u0085\7n\2\2\u0085\u0086\7n\2\2\u0086\u0087")
        buf.write("\7{\2\2\u0087\b\3\2\2\2\u0088\u0089\7d\2\2\u0089\u008a")
        buf.write("\7t\2\2\u008a\u008b\7g\2\2\u008b\u008c\7c\2\2\u008c\u008d")
        buf.write("\7m\2\2\u008d\n\3\2\2\2\u008e\u008f\7e\2\2\u008f\u0090")
        buf.write("\7q\2\2\u0090\u0091\7p\2\2\u0091\u0092\7v\2\2\u0092\u0093")
        buf.write("\7k\2\2\u0093\u0094\7p\2\2\u0094\u0095\7w\2\2\u0095\u0096")
        buf.write("\7g\2\2\u0096\f\3\2\2\2\u0097\u0098\7t\2\2\u0098\u0099")
        buf.write("\7g\2\2\u0099\u009a\7v\2\2\u009a\u009b\7w\2\2\u009b\u009c")
        buf.write("\7t\2\2\u009c\u009d\7p\2\2\u009d\16\3\2\2\2\u009e\u009f")
        buf.write("\7t\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1\7k\2\2\u00a1\u00a2")
        buf.write("\7u\2\2\u00a2\u00a3\7g\2\2\u00a3\20\3\2\2\2\u00a4\u00a5")
        buf.write("\7v\2\2\u00a5\u00a6\7t\2\2\u00a6\u00a7\7{\2\2\u00a7\u00a8")
        buf.write("\7<\2\2\u00a8\22\3\2\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab")
        buf.write("\7z\2\2\u00ab\u00ac\7e\2\2\u00ac\u00ad\7g\2\2\u00ad\u00ae")
        buf.write("\7r\2\2\u00ae\u00af\7v\2\2\u00af\24\3\2\2\2\u00b0\u00b1")
        buf.write("\7c\2\2\u00b1\u00b2\7u\2\2\u00b2\26\3\2\2\2\u00b3\u00b4")
        buf.write("\7k\2\2\u00b4\u00b5\7h\2\2\u00b5\30\3\2\2\2\u00b6\u00b7")
        buf.write("\7g\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba")
        buf.write("\7h\2\2\u00ba\32\3\2\2\2\u00bb\u00bc\7y\2\2\u00bc\u00bd")
        buf.write("\7j\2\2\u00bd\u00be\7k\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0")
        buf.write("\7g\2\2\u00c0\34\3\2\2\2\u00c1\u00c2\7h\2\2\u00c2\u00c3")
        buf.write("\7q\2\2\u00c3\u00c4\7t\2\2\u00c4\36\3\2\2\2\u00c5\u00c6")
        buf.write("\7k\2\2\u00c6\u00c7\7p\2\2\u00c7 \3\2\2\2\u00c8\u00c9")
        buf.write("\7t\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc")
        buf.write("\7i\2\2\u00cc\u00cd\7g\2\2\u00cd\"\3\2\2\2\u00ce\u00cf")
        buf.write("\7.\2\2\u00cf$\3\2\2\2\u00d0\u00d1\7r\2\2\u00d1\u00d2")
        buf.write("\7t\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5")
        buf.write("\7v\2\2\u00d5&\3\2\2\2\u00d6\u00d7\7>\2\2\u00d7(\3\2\2")
        buf.write("\2\u00d8\u00d9\7@\2\2\u00d9*\3\2\2\2\u00da\u00db\7?\2")
        buf.write("\2\u00db\u00dc\7?\2\2\u00dc,\3\2\2\2\u00dd\u00de\7@\2")
        buf.write("\2\u00de\u00df\7?\2\2\u00df.\3\2\2\2\u00e0\u00e1\7>\2")
        buf.write("\2\u00e1\u00e2\7?\2\2\u00e2\60\3\2\2\2\u00e3\u00e4\7#")
        buf.write("\2\2\u00e4\u00e5\7?\2\2\u00e5\62\3\2\2\2\u00e6\u00e7\7")
        buf.write("-\2\2\u00e7\64\3\2\2\2\u00e8\u00e9\7/\2\2\u00e9\66\3\2")
        buf.write("\2\2\u00ea\u00eb\7,\2\2\u00eb8\3\2\2\2\u00ec\u00ed\7\61")
        buf.write("\2\2\u00ed:\3\2\2\2\u00ee\u00ef\7\'\2\2\u00ef<\3\2\2\2")
        buf.write("\u00f0\u00f1\7\60\2\2\u00f1>\3\2\2\2\u00f2\u00f3\7k\2")
        buf.write("\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7v\2\2\u00f5@\3\2\2")
        buf.write("\2\u00f6\u00f7\7u\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7")
        buf.write("t\2\2\u00f9B\3\2\2\2\u00fa\u00fb\7n\2\2\u00fb\u00fc\7")
        buf.write("k\2\2\u00fc\u00fd\7u\2\2\u00fd\u00fe\7v\2\2\u00feD\3\2")
        buf.write("\2\2\u00ff\u0100\7h\2\2\u0100\u0101\7n\2\2\u0101\u0102")
        buf.write("\7q\2\2\u0102\u0103\7c\2\2\u0103\u0104\7v\2\2\u0104F\3")
        buf.write("\2\2\2\u0105\u0106\5U+\2\u0106H\3\2\2\2\u0107\u0108\5")
        buf.write("M\'\2\u0108J\3\2\2\2\u0109\u010b\5m\67\2\u010a\u0109\3")
        buf.write("\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d")
        buf.write("\3\2\2\2\u010d\u010f\3\2\2\2\u010e\u010c\3\2\2\2\u010f")
        buf.write("\u0113\7\60\2\2\u0110\u0112\5m\67\2\u0111\u0110\3\2\2")
        buf.write("\2\u0112\u0115\3\2\2\2\u0113\u0111\3\2\2\2\u0113\u0114")
        buf.write("\3\2\2\2\u0114L\3\2\2\2\u0115\u0113\3\2\2\2\u0116\u0117")
        buf.write("\5W,\2\u0117N\3\2\2\2\u0118\u0119\6(\2\2\u0119\u0125\5")
        buf.write("o8\2\u011a\u011c\7\17\2\2\u011b\u011a\3\2\2\2\u011b\u011c")
        buf.write("\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u0120\7\f\2\2\u011e")
        buf.write("\u0120\4\16\17\2\u011f\u011b\3\2\2\2\u011f\u011e\3\2\2")
        buf.write("\2\u0120\u0122\3\2\2\2\u0121\u0123\5o8\2\u0122\u0121\3")
        buf.write("\2\2\2\u0122\u0123\3\2\2\2\u0123\u0125\3\2\2\2\u0124\u0118")
        buf.write("\3\2\2\2\u0124\u011f\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("\u0127\b(\2\2\u0127P\3\2\2\2\u0128\u0129\7i\2\2\u0129")
        buf.write("\u012a\7a\2\2\u012a\u012c\3\2\2\2\u012b\u012d\5w<\2\u012c")
        buf.write("\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u012c\3\2\2\2")
        buf.write("\u012e\u012f\3\2\2\2\u012fR\3\2\2\2\u0130\u0134\5u;\2")
        buf.write("\u0131\u0133\5w<\2\u0132\u0131\3\2\2\2\u0133\u0136\3\2")
        buf.write("\2\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135T\3")
        buf.write("\2\2\2\u0136\u0134\3\2\2\2\u0137\u013b\7$\2\2\u0138\u013a")
        buf.write("\13\2\2\2\u0139\u0138\3\2\2\2\u013a\u013d\3\2\2\2\u013b")
        buf.write("\u013c\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013e\3\2\2\2")
        buf.write("\u013d\u013b\3\2\2\2\u013e\u013f\7$\2\2\u013fV\3\2\2\2")
        buf.write("\u0140\u0144\5k\66\2\u0141\u0143\5m\67\2\u0142\u0141\3")
        buf.write("\2\2\2\u0143\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145")
        buf.write("\3\2\2\2\u0145\u014d\3\2\2\2\u0146\u0144\3\2\2\2\u0147")
        buf.write("\u0149\7\62\2\2\u0148\u0147\3\2\2\2\u0149\u014a\3\2\2")
        buf.write("\2\u014a\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014d")
        buf.write("\3\2\2\2\u014c\u0140\3\2\2\2\u014c\u0148\3\2\2\2\u014d")
        buf.write("X\3\2\2\2\u014e\u014f\7*\2\2\u014fZ\3\2\2\2\u0150\u0151")
        buf.write("\7+\2\2\u0151\\\3\2\2\2\u0152\u0153\7]\2\2\u0153^\3\2")
        buf.write("\2\2\u0154\u0155\7_\2\2\u0155`\3\2\2\2\u0156\u0157\7}")
        buf.write("\2\2\u0157b\3\2\2\2\u0158\u0159\7\177\2\2\u0159d\3\2\2")
        buf.write("\2\u015a\u015b\7?\2\2\u015bf\3\2\2\2\u015c\u0160\5o8\2")
        buf.write("\u015d\u0160\5q9\2\u015e\u0160\5s:\2\u015f\u015c\3\2\2")
        buf.write("\2\u015f\u015d\3\2\2\2\u015f\u015e\3\2\2\2\u0160\u0161")
        buf.write("\3\2\2\2\u0161\u0162\b\64\3\2\u0162h\3\2\2\2\u0163\u0164")
        buf.write("\13\2\2\2\u0164j\3\2\2\2\u0165\u0166\t\2\2\2\u0166l\3")
        buf.write("\2\2\2\u0167\u0168\t\3\2\2\u0168n\3\2\2\2\u0169\u016b")
        buf.write("\t\4\2\2\u016a\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016dp\3\2\2\2\u016e")
        buf.write("\u0172\7%\2\2\u016f\u0171\n\5\2\2\u0170\u016f\3\2\2\2")
        buf.write("\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3")
        buf.write("\2\2\2\u0173r\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0177")
        buf.write("\7^\2\2\u0176\u0178\5o8\2\u0177\u0176\3\2\2\2\u0177\u0178")
        buf.write("\3\2\2\2\u0178\u017e\3\2\2\2\u0179\u017b\7\17\2\2\u017a")
        buf.write("\u0179\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017c\u017f\7\f\2\2\u017d\u017f\4\16\17\2\u017e\u017a")
        buf.write("\3\2\2\2\u017e\u017d\3\2\2\2\u017ft\3\2\2\2\u0180\u0182")
        buf.write("\t\6\2\2\u0181\u0180\3\2\2\2\u0182v\3\2\2\2\u0183\u0186")
        buf.write("\5u;\2\u0184\u0186\t\3\2\2\u0185\u0183\3\2\2\2\u0185\u0184")
        buf.write("\3\2\2\2\u0186x\3\2\2\2\27\2\u010c\u0113\u011b\u011f\u0122")
        buf.write("\u0124\u012e\u0134\u013b\u0144\u014a\u014c\u015f\u016c")
        buf.write("\u0172\u0177\u017a\u017e\u0181\u0185\4\3(\2\b\2\2")
        return buf.getvalue()


class Python3d3Lexer(Lexer):

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
    T__32 = 33
    T__33 = 34
    STRING = 35
    NUMBER = 36
    FLOAT = 37
    INTEGER = 38
    NEWLINE = 39
    GRZLYNAME = 40
    NAME = 41
    STRING_LITERAL = 42
    DECIMAL_INTEGER = 43
    OPEN_PAREN = 44
    CLOSE_PAREN = 45
    OPEN_BRACK = 46
    CLOSE_BRACK = 47
    OPEN_BRACE = 48
    CLOSE_BRACE = 49
    ASSIGN_EQUAL = 50
    SKIP_ = 51
    UNKNOWN_CHAR = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'else'", "'finally'", "'break'", "'continue'", "'return'", 
            "'raise'", "'try:'", "'except'", "'as'", "'if'", "'elif'", "'while'", 
            "'for'", "'in'", "'range'", "','", "'print'", "'<'", "'>'", 
            "'=='", "'>='", "'<='", "'!='", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'.'", "'int'", "'str'", "'list'", "'float'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "NUMBER", "FLOAT", "INTEGER", "NEWLINE", "GRZLYNAME", 
            "NAME", "STRING_LITERAL", "DECIMAL_INTEGER", "OPEN_PAREN", "CLOSE_PAREN", 
            "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", "CLOSE_BRACE", "ASSIGN_EQUAL", 
            "SKIP_", "UNKNOWN_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "STRING", "NUMBER", "FLOAT", "INTEGER", 
                  "NEWLINE", "GRZLYNAME", "NAME", "STRING_LITERAL", "DECIMAL_INTEGER", 
                  "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", 
                  "OPEN_BRACE", "CLOSE_BRACE", "ASSIGN_EQUAL", "SKIP_", 
                  "UNKNOWN_CHAR", "NON_ZERO_DIGIT", "DIGIT", "SPACES", "COMMENT", 
                  "LINE_JOINING", "ID_START", "ID_CONTINUE" ]

    grammarFileName = "Python3d3.g4"

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
            actions[38] = self.NEWLINE_action 
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
            preds[38] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


