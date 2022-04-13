# Generated from grammar/Python3d2.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\62")
        buf.write("\u0167\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\5!\u00e7\n!\3\"\3\"\7\"\u00eb\n")
        buf.write("\"\f\"\16\"\u00ee\13\"\3\"\3\"\7\"\u00f2\n\"\f\"\16\"")
        buf.write("\u00f5\13\"\3#\3#\3$\3$\3$\5$\u00fc\n$\3$\3$\5$\u0100")
        buf.write("\n$\3$\5$\u0103\n$\5$\u0105\n$\3$\3$\3%\3%\3%\3%\6%\u010d")
        buf.write("\n%\r%\16%\u010e\3&\3&\7&\u0113\n&\f&\16&\u0116\13&\3")
        buf.write("\'\3\'\7\'\u011a\n\'\f\'\16\'\u011d\13\'\3\'\3\'\3(\3")
        buf.write("(\7(\u0123\n(\f(\16(\u0126\13(\3(\6(\u0129\n(\r(\16(\u012a")
        buf.write("\5(\u012d\n(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3")
        buf.write("/\3\60\3\60\3\60\5\60\u0140\n\60\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\6\64\u014b\n\64\r\64\16\64\u014c")
        buf.write("\3\65\3\65\7\65\u0151\n\65\f\65\16\65\u0154\13\65\3\66")
        buf.write("\3\66\5\66\u0158\n\66\3\66\5\66\u015b\n\66\3\66\3\66\5")
        buf.write("\66\u015f\n\66\3\67\5\67\u0162\n\67\38\38\58\u0166\n8")
        buf.write("\3\u011b\29\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\2e\2g\2i\2k\2m\2")
        buf.write("o\2\3\2\7\3\2\63;\3\2\62;\4\2\13\13\"\"\4\2\f\f\16\17")
        buf.write("\5\2C\\aac|\2\u0174\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\3q\3\2\2")
        buf.write("\2\5s\3\2\2\2\7y\3\2\2\2\t\u0082\3\2\2\2\13\u0089\3\2")
        buf.write("\2\2\r\u008c\3\2\2\2\17\u0091\3\2\2\2\21\u0096\3\2\2\2")
        buf.write("\23\u009c\3\2\2\2\25\u00a0\3\2\2\2\27\u00a3\3\2\2\2\31")
        buf.write("\u00a9\3\2\2\2\33\u00ab\3\2\2\2\35\u00b1\3\2\2\2\37\u00b3")
        buf.write("\3\2\2\2!\u00b5\3\2\2\2#\u00b8\3\2\2\2%\u00bb\3\2\2\2")
        buf.write("\'\u00be\3\2\2\2)\u00c1\3\2\2\2+\u00c3\3\2\2\2-\u00c5")
        buf.write("\3\2\2\2/\u00c7\3\2\2\2\61\u00c9\3\2\2\2\63\u00cb\3\2")
        buf.write("\2\2\65\u00cd\3\2\2\2\67\u00d1\3\2\2\29\u00d5\3\2\2\2")
        buf.write(";\u00da\3\2\2\2=\u00e0\3\2\2\2?\u00e2\3\2\2\2A\u00e6\3")
        buf.write("\2\2\2C\u00e8\3\2\2\2E\u00f6\3\2\2\2G\u0104\3\2\2\2I\u0108")
        buf.write("\3\2\2\2K\u0110\3\2\2\2M\u0117\3\2\2\2O\u012c\3\2\2\2")
        buf.write("Q\u012e\3\2\2\2S\u0130\3\2\2\2U\u0132\3\2\2\2W\u0134\3")
        buf.write("\2\2\2Y\u0136\3\2\2\2[\u0138\3\2\2\2]\u013a\3\2\2\2_\u013f")
        buf.write("\3\2\2\2a\u0143\3\2\2\2c\u0145\3\2\2\2e\u0147\3\2\2\2")
        buf.write("g\u014a\3\2\2\2i\u014e\3\2\2\2k\u0155\3\2\2\2m\u0161\3")
        buf.write("\2\2\2o\u0165\3\2\2\2qr\7<\2\2r\4\3\2\2\2st\7d\2\2tu\7")
        buf.write("t\2\2uv\7g\2\2vw\7c\2\2wx\7m\2\2x\6\3\2\2\2yz\7e\2\2z")
        buf.write("{\7q\2\2{|\7p\2\2|}\7v\2\2}~\7k\2\2~\177\7p\2\2\177\u0080")
        buf.write("\7w\2\2\u0080\u0081\7g\2\2\u0081\b\3\2\2\2\u0082\u0083")
        buf.write("\7t\2\2\u0083\u0084\7g\2\2\u0084\u0085\7v\2\2\u0085\u0086")
        buf.write("\7w\2\2\u0086\u0087\7t\2\2\u0087\u0088\7p\2\2\u0088\n")
        buf.write("\3\2\2\2\u0089\u008a\7k\2\2\u008a\u008b\7h\2\2\u008b\f")
        buf.write("\3\2\2\2\u008c\u008d\7g\2\2\u008d\u008e\7n\2\2\u008e\u008f")
        buf.write("\7k\2\2\u008f\u0090\7h\2\2\u0090\16\3\2\2\2\u0091\u0092")
        buf.write("\7g\2\2\u0092\u0093\7n\2\2\u0093\u0094\7u\2\2\u0094\u0095")
        buf.write("\7g\2\2\u0095\20\3\2\2\2\u0096\u0097\7y\2\2\u0097\u0098")
        buf.write("\7j\2\2\u0098\u0099\7k\2\2\u0099\u009a\7n\2\2\u009a\u009b")
        buf.write("\7g\2\2\u009b\22\3\2\2\2\u009c\u009d\7h\2\2\u009d\u009e")
        buf.write("\7q\2\2\u009e\u009f\7t\2\2\u009f\24\3\2\2\2\u00a0\u00a1")
        buf.write("\7k\2\2\u00a1\u00a2\7p\2\2\u00a2\26\3\2\2\2\u00a3\u00a4")
        buf.write("\7t\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7p\2\2\u00a6\u00a7")
        buf.write("\7i\2\2\u00a7\u00a8\7g\2\2\u00a8\30\3\2\2\2\u00a9\u00aa")
        buf.write("\7.\2\2\u00aa\32\3\2\2\2\u00ab\u00ac\7r\2\2\u00ac\u00ad")
        buf.write("\7t\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af\7p\2\2\u00af\u00b0")
        buf.write("\7v\2\2\u00b0\34\3\2\2\2\u00b1\u00b2\7>\2\2\u00b2\36\3")
        buf.write("\2\2\2\u00b3\u00b4\7@\2\2\u00b4 \3\2\2\2\u00b5\u00b6\7")
        buf.write("?\2\2\u00b6\u00b7\7?\2\2\u00b7\"\3\2\2\2\u00b8\u00b9\7")
        buf.write("@\2\2\u00b9\u00ba\7?\2\2\u00ba$\3\2\2\2\u00bb\u00bc\7")
        buf.write(">\2\2\u00bc\u00bd\7?\2\2\u00bd&\3\2\2\2\u00be\u00bf\7")
        buf.write("#\2\2\u00bf\u00c0\7?\2\2\u00c0(\3\2\2\2\u00c1\u00c2\7")
        buf.write("-\2\2\u00c2*\3\2\2\2\u00c3\u00c4\7/\2\2\u00c4,\3\2\2\2")
        buf.write("\u00c5\u00c6\7,\2\2\u00c6.\3\2\2\2\u00c7\u00c8\7\61\2")
        buf.write("\2\u00c8\60\3\2\2\2\u00c9\u00ca\7\'\2\2\u00ca\62\3\2\2")
        buf.write("\2\u00cb\u00cc\7\60\2\2\u00cc\64\3\2\2\2\u00cd\u00ce\7")
        buf.write("k\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0\7v\2\2\u00d0\66\3")
        buf.write("\2\2\2\u00d1\u00d2\7u\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4")
        buf.write("\7t\2\2\u00d48\3\2\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7")
        buf.write("\7k\2\2\u00d7\u00d8\7u\2\2\u00d8\u00d9\7v\2\2\u00d9:\3")
        buf.write("\2\2\2\u00da\u00db\7h\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd")
        buf.write("\7q\2\2\u00dd\u00de\7c\2\2\u00de\u00df\7v\2\2\u00df<\3")
        buf.write("\2\2\2\u00e0\u00e1\7$\2\2\u00e1>\3\2\2\2\u00e2\u00e3\5")
        buf.write("M\'\2\u00e3@\3\2\2\2\u00e4\u00e7\5E#\2\u00e5\u00e7\5C")
        buf.write("\"\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7B\3")
        buf.write("\2\2\2\u00e8\u00ec\5c\62\2\u00e9\u00eb\5e\63\2\u00ea\u00e9")
        buf.write("\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec")
        buf.write("\u00ed\3\2\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00ec\3\2\2\2")
        buf.write("\u00ef\u00f3\7\60\2\2\u00f0\u00f2\5e\63\2\u00f1\u00f0")
        buf.write("\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3")
        buf.write("\u00f4\3\2\2\2\u00f4D\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6")
        buf.write("\u00f7\5O(\2\u00f7F\3\2\2\2\u00f8\u00f9\6$\2\2\u00f9\u0105")
        buf.write("\5g\64\2\u00fa\u00fc\7\17\2\2\u00fb\u00fa\3\2\2\2\u00fb")
        buf.write("\u00fc\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u0100\7\f\2\2")
        buf.write("\u00fe\u0100\4\16\17\2\u00ff\u00fb\3\2\2\2\u00ff\u00fe")
        buf.write("\3\2\2\2\u0100\u0102\3\2\2\2\u0101\u0103\5g\64\2\u0102")
        buf.write("\u0101\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0105\3\2\2\2")
        buf.write("\u0104\u00f8\3\2\2\2\u0104\u00ff\3\2\2\2\u0105\u0106\3")
        buf.write("\2\2\2\u0106\u0107\b$\2\2\u0107H\3\2\2\2\u0108\u0109\7")
        buf.write("i\2\2\u0109\u010a\7a\2\2\u010a\u010c\3\2\2\2\u010b\u010d")
        buf.write("\5o8\2\u010c\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u010c")
        buf.write("\3\2\2\2\u010e\u010f\3\2\2\2\u010fJ\3\2\2\2\u0110\u0114")
        buf.write("\5m\67\2\u0111\u0113\5o8\2\u0112\u0111\3\2\2\2\u0113\u0116")
        buf.write("\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115")
        buf.write("L\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u011b\7$\2\2\u0118")
        buf.write("\u011a\13\2\2\2\u0119\u0118\3\2\2\2\u011a\u011d\3\2\2")
        buf.write("\2\u011b\u011c\3\2\2\2\u011b\u0119\3\2\2\2\u011c\u011e")
        buf.write("\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u011f\7$\2\2\u011f")
        buf.write("N\3\2\2\2\u0120\u0124\5c\62\2\u0121\u0123\5e\63\2\u0122")
        buf.write("\u0121\3\2\2\2\u0123\u0126\3\2\2\2\u0124\u0122\3\2\2\2")
        buf.write("\u0124\u0125\3\2\2\2\u0125\u012d\3\2\2\2\u0126\u0124\3")
        buf.write("\2\2\2\u0127\u0129\7\62\2\2\u0128\u0127\3\2\2\2\u0129")
        buf.write("\u012a\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2")
        buf.write("\u012b\u012d\3\2\2\2\u012c\u0120\3\2\2\2\u012c\u0128\3")
        buf.write("\2\2\2\u012dP\3\2\2\2\u012e\u012f\7*\2\2\u012fR\3\2\2")
        buf.write("\2\u0130\u0131\7+\2\2\u0131T\3\2\2\2\u0132\u0133\7]\2")
        buf.write("\2\u0133V\3\2\2\2\u0134\u0135\7_\2\2\u0135X\3\2\2\2\u0136")
        buf.write("\u0137\7}\2\2\u0137Z\3\2\2\2\u0138\u0139\7\177\2\2\u0139")
        buf.write("\\\3\2\2\2\u013a\u013b\7?\2\2\u013b^\3\2\2\2\u013c\u0140")
        buf.write("\5g\64\2\u013d\u0140\5i\65\2\u013e\u0140\5k\66\2\u013f")
        buf.write("\u013c\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u013e\3\2\2\2")
        buf.write("\u0140\u0141\3\2\2\2\u0141\u0142\b\60\3\2\u0142`\3\2\2")
        buf.write("\2\u0143\u0144\13\2\2\2\u0144b\3\2\2\2\u0145\u0146\t\2")
        buf.write("\2\2\u0146d\3\2\2\2\u0147\u0148\t\3\2\2\u0148f\3\2\2\2")
        buf.write("\u0149\u014b\t\4\2\2\u014a\u0149\3\2\2\2\u014b\u014c\3")
        buf.write("\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014dh")
        buf.write("\3\2\2\2\u014e\u0152\7%\2\2\u014f\u0151\n\5\2\2\u0150")
        buf.write("\u014f\3\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150\3\2\2\2")
        buf.write("\u0152\u0153\3\2\2\2\u0153j\3\2\2\2\u0154\u0152\3\2\2")
        buf.write("\2\u0155\u0157\7^\2\2\u0156\u0158\5g\64\2\u0157\u0156")
        buf.write("\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u015e\3\2\2\2\u0159")
        buf.write("\u015b\7\17\2\2\u015a\u0159\3\2\2\2\u015a\u015b\3\2\2")
        buf.write("\2\u015b\u015c\3\2\2\2\u015c\u015f\7\f\2\2\u015d\u015f")
        buf.write("\4\16\17\2\u015e\u015a\3\2\2\2\u015e\u015d\3\2\2\2\u015f")
        buf.write("l\3\2\2\2\u0160\u0162\t\6\2\2\u0161\u0160\3\2\2\2\u0162")
        buf.write("n\3\2\2\2\u0163\u0166\5m\67\2\u0164\u0166\t\3\2\2\u0165")
        buf.write("\u0163\3\2\2\2\u0165\u0164\3\2\2\2\u0166p\3\2\2\2\30\2")
        buf.write("\u00e6\u00ec\u00f3\u00fb\u00ff\u0102\u0104\u010e\u0114")
        buf.write("\u011b\u0124\u012a\u012c\u013f\u014c\u0152\u0157\u015a")
        buf.write("\u015e\u0161\u0165\4\3$\2\b\2\2")
        return buf.getvalue()


class Python3d2Lexer(Lexer):

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
    STRING = 31
    NUMBER = 32
    FLOAT = 33
    INTEGER = 34
    NEWLINE = 35
    GRZLYNAME = 36
    NAME = 37
    STRING_LITERAL = 38
    DECIMAL_INTEGER = 39
    OPEN_PAREN = 40
    CLOSE_PAREN = 41
    OPEN_BRACK = 42
    CLOSE_BRACK = 43
    OPEN_BRACE = 44
    CLOSE_BRACE = 45
    ASSIGN_EQUAL = 46
    SKIP_ = 47
    UNKNOWN_CHAR = 48

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'break'", "'continue'", "'return'", "'if'", "'elif'", 
            "'else'", "'while'", "'for'", "'in'", "'range'", "','", "'print'", 
            "'<'", "'>'", "'=='", "'>='", "'<='", "'!='", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'.'", "'int'", "'str'", "'list'", "'float'", 
            "'\"'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "NUMBER", "FLOAT", "INTEGER", "NEWLINE", "GRZLYNAME", 
            "NAME", "STRING_LITERAL", "DECIMAL_INTEGER", "OPEN_PAREN", "CLOSE_PAREN", 
            "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", "CLOSE_BRACE", "ASSIGN_EQUAL", 
            "SKIP_", "UNKNOWN_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "STRING", "NUMBER", 
                  "FLOAT", "INTEGER", "NEWLINE", "GRZLYNAME", "NAME", "STRING_LITERAL", 
                  "DECIMAL_INTEGER", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", 
                  "CLOSE_BRACK", "OPEN_BRACE", "CLOSE_BRACE", "ASSIGN_EQUAL", 
                  "SKIP_", "UNKNOWN_CHAR", "NON_ZERO_DIGIT", "DIGIT", "SPACES", 
                  "COMMENT", "LINE_JOINING", "ID_START", "ID_CONTINUE" ]

    grammarFileName = "Python3d2.g4"

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
            actions[34] = self.NEWLINE_action 
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
            preds[34] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


