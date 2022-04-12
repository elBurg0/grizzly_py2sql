# Generated from grammar/Python3d.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63")
        buf.write("\u0102\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\3\2\3\2\3\2\3\2\3\2\5\2<\n\2")
        buf.write("\3\3\3\3\7\3@\n\3\f\3\16\3C\13\3\3\3\3\3\3\4\3\4\5\4I")
        buf.write("\n\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6R\n\6\3\7\3\7\3\7")
        buf.write("\5\7W\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\5\ni\n\n\3\13\3\13\5\13m\n\13\3\f")
        buf.write("\3\f\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\5\17y\n\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u0084")
        buf.write("\n\20\f\20\16\20\u0087\13\20\3\20\3\20\3\20\5\20\u008c")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u009f\n\22\3")
        buf.write("\22\3\22\3\22\5\22\u00a4\n\22\3\23\3\23\3\23\3\23\6\23")
        buf.write("\u00aa\n\23\r\23\16\23\u00ab\3\23\3\23\5\23\u00b0\n\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\7\25\u00bd\n\25\f\25\16\25\u00c0\13\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u00d7\n\30\f")
        buf.write("\30\16\30\u00da\13\30\3\30\3\30\5\30\u00de\n\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\6\30\u00e9\n\30")
        buf.write("\r\30\16\30\u00ea\3\30\3\30\3\30\3\30\3\30\7\30\u00f2")
        buf.write("\n\30\f\30\16\30\u00f5\13\30\3\31\3\31\3\32\6\32\u00fa")
        buf.write("\n\32\r\32\16\32\u00fb\3\33\3\33\3\33\3\33\3\33\2\3.\34")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\2\6\3\2\20\25\3\2\26\31\3\2\33\36\b\2\3\3\16\16\20")
        buf.write("\32\37!&&)/\2\u0108\2;\3\2\2\2\4A\3\2\2\2\6H\3\2\2\2\b")
        buf.write("J\3\2\2\2\nQ\3\2\2\2\fV\3\2\2\2\16X\3\2\2\2\20^\3\2\2")
        buf.write("\2\22h\3\2\2\2\24l\3\2\2\2\26n\3\2\2\2\30p\3\2\2\2\32")
        buf.write("r\3\2\2\2\34x\3\2\2\2\36z\3\2\2\2 \u008d\3\2\2\2\"\u00a3")
        buf.write("\3\2\2\2$\u00af\3\2\2\2&\u00b1\3\2\2\2(\u00b8\3\2\2\2")
        buf.write("*\u00c1\3\2\2\2,\u00c6\3\2\2\2.\u00dd\3\2\2\2\60\u00f6")
        buf.write("\3\2\2\2\62\u00f9\3\2\2\2\64\u00fd\3\2\2\2\66<\7$\2\2")
        buf.write("\67<\5\b\5\289\5\34\17\29:\7$\2\2:<\3\2\2\2;\66\3\2\2")
        buf.write("\2;\67\3\2\2\2;8\3\2\2\2<\3\3\2\2\2=@\7$\2\2>@\5\6\4\2")
        buf.write("?=\3\2\2\2?>\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2BD\3")
        buf.write("\2\2\2CA\3\2\2\2DE\7\2\2\3E\5\3\2\2\2FI\5\b\5\2GI\5\34")
        buf.write("\17\2HF\3\2\2\2HG\3\2\2\2I\7\3\2\2\2JK\5\n\6\2KL\7$\2")
        buf.write("\2L\t\3\2\2\2MR\5\f\7\2NR\5\24\13\2OR\5*\26\2PR\5\32\16")
        buf.write("\2QM\3\2\2\2QN\3\2\2\2QO\3\2\2\2QP\3\2\2\2R\13\3\2\2\2")
        buf.write("SW\5\16\b\2TW\5\20\t\2UW\5\22\n\2VS\3\2\2\2VT\3\2\2\2")
        buf.write("VU\3\2\2\2W\r\3\2\2\2XY\7&\2\2YZ\7\3\2\2Z[\5\60\31\2[")
        buf.write("\\\7/\2\2\\]\5.\30\2]\17\3\2\2\2^_\7&\2\2_`\7\3\2\2`a")
        buf.write("\5\60\31\2a\21\3\2\2\2bc\7%\2\2cd\7/\2\2di\5.\30\2ef\7")
        buf.write("&\2\2fg\7/\2\2gi\5.\30\2hb\3\2\2\2he\3\2\2\2i\23\3\2\2")
        buf.write("\2jm\5\26\f\2km\5\30\r\2lj\3\2\2\2lk\3\2\2\2m\25\3\2\2")
        buf.write("\2no\7\4\2\2o\27\3\2\2\2pq\7\5\2\2q\31\3\2\2\2rs\7\6\2")
        buf.write("\2st\5.\30\2t\33\3\2\2\2uy\5\36\20\2vy\5 \21\2wy\5\"\22")
        buf.write("\2xu\3\2\2\2xv\3\2\2\2xw\3\2\2\2y\35\3\2\2\2z{\7\7\2\2")
        buf.write("{|\5(\25\2|}\7\3\2\2}\u0085\5$\23\2~\177\7\b\2\2\177\u0080")
        buf.write("\5(\25\2\u0080\u0081\7\3\2\2\u0081\u0082\5$\23\2\u0082")
        buf.write("\u0084\3\2\2\2\u0083~\3\2\2\2\u0084\u0087\3\2\2\2\u0085")
        buf.write("\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u008b\3\2\2\2")
        buf.write("\u0087\u0085\3\2\2\2\u0088\u0089\7\t\2\2\u0089\u008a\7")
        buf.write("\3\2\2\u008a\u008c\5$\23\2\u008b\u0088\3\2\2\2\u008b\u008c")
        buf.write("\3\2\2\2\u008c\37\3\2\2\2\u008d\u008e\7\n\2\2\u008e\u008f")
        buf.write("\5(\25\2\u008f\u0090\7\3\2\2\u0090\u0091\5$\23\2\u0091")
        buf.write("!\3\2\2\2\u0092\u0093\7\13\2\2\u0093\u0094\5.\30\2\u0094")
        buf.write("\u0095\7\f\2\2\u0095\u0096\5&\24\2\u0096\u0097\7\3\2\2")
        buf.write("\u0097\u0098\5$\23\2\u0098\u00a4\3\2\2\2\u0099\u009a\7")
        buf.write("\13\2\2\u009a\u009b\5.\30\2\u009b\u009e\7\f\2\2\u009c")
        buf.write("\u009f\5.\30\2\u009d\u009f\7%\2\2\u009e\u009c\3\2\2\2")
        buf.write("\u009e\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\7")
        buf.write("\3\2\2\u00a1\u00a2\5$\23\2\u00a2\u00a4\3\2\2\2\u00a3\u0092")
        buf.write("\3\2\2\2\u00a3\u0099\3\2\2\2\u00a4#\3\2\2\2\u00a5\u00b0")
        buf.write("\5\b\5\2\u00a6\u00a7\7$\2\2\u00a7\u00a9\7\62\2\2\u00a8")
        buf.write("\u00aa\5\6\4\2\u00a9\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2")
        buf.write("\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\3")
        buf.write("\2\2\2\u00ad\u00ae\7\63\2\2\u00ae\u00b0\3\2\2\2\u00af")
        buf.write("\u00a5\3\2\2\2\u00af\u00a6\3\2\2\2\u00b0%\3\2\2\2\u00b1")
        buf.write("\u00b2\7\r\2\2\u00b2\u00b3\7)\2\2\u00b3\u00b4\5.\30\2")
        buf.write("\u00b4\u00b5\7\16\2\2\u00b5\u00b6\5.\30\2\u00b6\u00b7")
        buf.write("\7*\2\2\u00b7\'\3\2\2\2\u00b8\u00be\5.\30\2\u00b9\u00ba")
        buf.write("\5,\27\2\u00ba\u00bb\5.\30\2\u00bb\u00bd\3\2\2\2\u00bc")
        buf.write("\u00b9\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2")
        buf.write("\u00be\u00bf\3\2\2\2\u00bf)\3\2\2\2\u00c0\u00be\3\2\2")
        buf.write("\2\u00c1\u00c2\7\17\2\2\u00c2\u00c3\7)\2\2\u00c3\u00c4")
        buf.write("\5.\30\2\u00c4\u00c5\7*\2\2\u00c5+\3\2\2\2\u00c6\u00c7")
        buf.write("\t\2\2\2\u00c7-\3\2\2\2\u00c8\u00c9\b\30\1\2\u00c9\u00de")
        buf.write("\7&\2\2\u00ca\u00de\7 \2\2\u00cb\u00de\7!\2\2\u00cc\u00de")
        buf.write("\5\64\33\2\u00cd\u00ce\7)\2\2\u00ce\u00cf\5.\30\2\u00cf")
        buf.write("\u00d0\7*\2\2\u00d0\u00de\3\2\2\2\u00d1\u00d2\7+\2\2\u00d2")
        buf.write("\u00d8\5.\30\2\u00d3\u00d4\5,\27\2\u00d4\u00d5\5.\30\2")
        buf.write("\u00d5\u00d7\3\2\2\2\u00d6\u00d3\3\2\2\2\u00d7\u00da\3")
        buf.write("\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00db")
        buf.write("\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00dc\7,\2\2\u00dc")
        buf.write("\u00de\3\2\2\2\u00dd\u00c8\3\2\2\2\u00dd\u00ca\3\2\2\2")
        buf.write("\u00dd\u00cb\3\2\2\2\u00dd\u00cc\3\2\2\2\u00dd\u00cd\3")
        buf.write("\2\2\2\u00dd\u00d1\3\2\2\2\u00de\u00f3\3\2\2\2\u00df\u00e0")
        buf.write("\f\4\2\2\u00e0\u00e1\7\32\2\2\u00e1\u00f2\5.\30\5\u00e2")
        buf.write("\u00e3\f\3\2\2\u00e3\u00e4\7\16\2\2\u00e4\u00f2\5.\30")
        buf.write("\4\u00e5\u00e8\f\f\2\2\u00e6\u00e7\t\3\2\2\u00e7\u00e9")
        buf.write("\5.\30\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea")
        buf.write("\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00f2\3\2\2\2")
        buf.write("\u00ec\u00ed\f\6\2\2\u00ed\u00ee\7)\2\2\u00ee\u00ef\5")
        buf.write(".\30\2\u00ef\u00f0\7*\2\2\u00f0\u00f2\3\2\2\2\u00f1\u00df")
        buf.write("\3\2\2\2\u00f1\u00e2\3\2\2\2\u00f1\u00e5\3\2\2\2\u00f1")
        buf.write("\u00ec\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2")
        buf.write("\u00f3\u00f4\3\2\2\2\u00f4/\3\2\2\2\u00f5\u00f3\3\2\2")
        buf.write("\2\u00f6\u00f7\t\4\2\2\u00f7\61\3\2\2\2\u00f8\u00fa\t")
        buf.write("\5\2\2\u00f9\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\63\3\2\2\2\u00fd\u00fe")
        buf.write("\7&\2\2\u00fe\u00ff\7\32\2\2\u00ff\u0100\7&\2\2\u0100")
        buf.write("\65\3\2\2\2\30;?AHQVhlx\u0085\u008b\u009e\u00a3\u00ab")
        buf.write("\u00af\u00be\u00d8\u00dd\u00ea\u00f1\u00f3\u00fb")
        return buf.getvalue()


class Python3dParser ( Parser ):

    grammarFileName = "Python3d.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'break'", "'continue'", "'return'", 
                     "'if'", "'elif'", "'else'", "'while'", "'for'", "'in'", 
                     "'range'", "','", "'print'", "'<'", "'>'", "'=='", 
                     "'>='", "'<='", "'!='", "'+'", "'-'", "'*'", "'/'", 
                     "'.'", "'int'", "'str'", "'list'", "'float'", "'\"'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "NUMBER", "FLOAT", 
                      "INTEGER", "NEWLINE", "GRZLYNAME", "NAME", "STRING_LITERAL", 
                      "DECIMAL_INTEGER", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", 
                      "CLOSE_BRACK", "OPEN_BRACE", "CLOSE_BRACE", "ASSIGN_EQUAL", 
                      "SKIP_", "UNKNOWN_CHAR", "INDENT", "DEDENT" ]

    RULE_single_input = 0
    RULE_file_input = 1
    RULE_stmt = 2
    RULE_simple_stmt = 3
    RULE_small_stmt = 4
    RULE_assignment_stmt = 5
    RULE_initialization = 6
    RULE_declaration = 7
    RULE_nontype_initialization = 8
    RULE_flow_stmt = 9
    RULE_break_stmt = 10
    RULE_continue_stmt = 11
    RULE_return_stmt = 12
    RULE_compound_stmt = 13
    RULE_if_stmt = 14
    RULE_while_stmt = 15
    RULE_for_stmt = 16
    RULE_suite = 17
    RULE_rang = 18
    RULE_test = 19
    RULE_print_stmt = 20
    RULE_comp_op = 21
    RULE_expr = 22
    RULE_typ = 23
    RULE_all_chars = 24
    RULE_db_reference = 25

    ruleNames =  [ "single_input", "file_input", "stmt", "simple_stmt", 
                   "small_stmt", "assignment_stmt", "initialization", "declaration", 
                   "nontype_initialization", "flow_stmt", "break_stmt", 
                   "continue_stmt", "return_stmt", "compound_stmt", "if_stmt", 
                   "while_stmt", "for_stmt", "suite", "rang", "test", "print_stmt", 
                   "comp_op", "expr", "typ", "all_chars", "db_reference" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    STRING=30
    NUMBER=31
    FLOAT=32
    INTEGER=33
    NEWLINE=34
    GRZLYNAME=35
    NAME=36
    STRING_LITERAL=37
    DECIMAL_INTEGER=38
    OPEN_PAREN=39
    CLOSE_PAREN=40
    OPEN_BRACK=41
    CLOSE_BRACK=42
    OPEN_BRACE=43
    CLOSE_BRACE=44
    ASSIGN_EQUAL=45
    SKIP_=46
    UNKNOWN_CHAR=47
    INDENT=48
    DEDENT=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Single_inputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(Python3dParser.NEWLINE, 0)

        def simple_stmt(self):
            return self.getTypedRuleContext(Python3dParser.Simple_stmtContext,0)


        def compound_stmt(self):
            return self.getTypedRuleContext(Python3dParser.Compound_stmtContext,0)


        def getRuleIndex(self):
            return Python3dParser.RULE_single_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle_input" ):
                listener.enterSingle_input(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle_input" ):
                listener.exitSingle_input(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_input" ):
                return visitor.visitSingle_input(self)
            else:
                return visitor.visitChildren(self)




    def single_input(self):

        localctx = Python3dParser.Single_inputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_single_input)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Python3dParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(Python3dParser.NEWLINE)
                pass
            elif token in [Python3dParser.T__1, Python3dParser.T__2, Python3dParser.T__3, Python3dParser.T__12, Python3dParser.GRZLYNAME, Python3dParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.simple_stmt()
                pass
            elif token in [Python3dParser.T__4, Python3dParser.T__7, Python3dParser.T__8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.compound_stmt()
                self.state = 55
                self.match(Python3dParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class File_inputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Python3dParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(Python3dParser.NEWLINE)
            else:
                return self.getToken(Python3dParser.NEWLINE, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Python3dParser.StmtContext)
            else:
                return self.getTypedRuleContext(Python3dParser.StmtContext,i)


        def getRuleIndex(self):
            return Python3dParser.RULE_file_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile_input" ):
                listener.enterFile_input(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile_input" ):
                listener.exitFile_input(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile_input" ):
                return visitor.visitFile_input(self)
            else:
                return visitor.visitChildren(self)




    def file_input(self):

        localctx = Python3dParser.File_inputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_file_input)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Python3dParser.T__1) | (1 << Python3dParser.T__2) | (1 << Python3dParser.T__3) | (1 << Python3dParser.T__4) | (1 << Python3dParser.T__7) | (1 << Python3dParser.T__8) | (1 << Python3dParser.T__12) | (1 << Python3dParser.NEWLINE) | (1 << Python3dParser.GRZLYNAME) | (1 << Python3dParser.NAME))) != 0):
                self.state = 61
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [Python3dParser.NEWLINE]:
                    self.state = 59
                    self.match(Python3dParser.NEWLINE)
                    pass
                elif token in [Python3dParser.T__1, Python3dParser.T__2, Python3dParser.T__3, Python3dParser.T__4, Python3dParser.T__7, Python3dParser.T__8, Python3dParser.T__12, Python3dParser.GRZLYNAME, Python3dParser.NAME]:
                    self.state = 60
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(Python3dParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmt(self):
            return self.getTypedRuleContext(Python3dParser.Simple_stmtContext,0)


        def compound_stmt(self):
            return self.getTypedRuleContext(Python3dParser.Compound_stmtContext,0)


        def getRuleIndex(self):
            return Python3dParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = Python3dParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Python3dParser.T__1, Python3dParser.T__2, Python3dParser.T__3, Python3dParser.T__12, Python3dParser.GRZLYNAME, Python3dParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.simple_stmt()
                pass
            elif token in [Python3dParser.T__4, Python3dParser.T__7, Python3dParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.compound_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def small_stmt(self):
            return self.getTypedRuleContext(Python3dParser.Small_stmtContext,0)


        def NEWLINE(self):
            return self.getToken(Python3dParser.NEWLINE, 0)

        def getRuleIndex(self):
            return Python3dParser.RULE_simple_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_stmt" ):
                listener.enterSimple_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_stmt" ):
                listener.exitSimple_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_stmt" ):
                return visitor.visitSimple_stmt(self)
            else:
                return visitor.visitChildren(self)




    def simple_stmt(self):

        localctx = Python3dParser.Simple_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_simple_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.small_stmt()
            self.state = 73
            self.match(Python3dParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Small_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_stmt(self):
            return self.getTypedRuleContext(Python3dParser.Assignment_stmtContext,0)


        def flow_stmt(self):
            return self.getTypedRuleContext(Python3dParser.Flow_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(Python3dParser.Print_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(Python3dParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return Python3dParser.RULE_small_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSmall_stmt" ):
                listener.enterSmall_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSmall_stmt" ):
                listener.exitSmall_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSmall_stmt" ):
                return visitor.visitSmall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def small_stmt(self):

        localctx = Python3dParser.Small_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_small_stmt)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Python3dParser.GRZLYNAME, Python3dParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.assignment_stmt()
                pass
            elif token in [Python3dParser.T__1, Python3dParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.flow_stmt()
                pass
            elif token in [Python3dParser.T__12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.print_stmt()
                pass
            elif token in [Python3dParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.return_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initialization(self):
            return self.getTypedRuleContext(Python3dParser.InitializationContext,0)


        def declaration(self):
            return self.getTypedRuleContext(Python3dParser.DeclarationContext,0)


        def nontype_initialization(self):
            return self.getTypedRuleContext(Python3dParser.Nontype_initializationContext,0)


        def getRuleIndex(self):
            return Python3dParser.RULE_assignment_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_stmt" ):
                listener.enterAssignment_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_stmt" ):
                listener.exitAssignment_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_stmt" ):
                return visitor.visitAssignment_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assignment_stmt(self):

        localctx = Python3dParser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment_stmt)
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.initialization()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.nontype_initialization()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(Python3dParser.NAME, 0)

        def typ(self):
            return self.getTypedRuleContext(Python3dParser.TypContext,0)


        def ASSIGN_EQUAL(self):
            return self.getToken(Python3dParser.ASSIGN_EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(Python3dParser.ExprContext,0)


        def getRuleIndex(self):
            return Python3dParser.RULE_initialization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitialization" ):
                listener.enterInitialization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitialization" ):
                listener.exitInitialization(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialization" ):
                return visitor.visitInitialization(self)
            else:
                return visitor.visitChildren(self)




    def initialization(self):

        localctx = Python3dParser.InitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_initialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(Python3dParser.NAME)
            self.state = 87
            self.match(Python3dParser.T__0)
            self.state = 88
            self.typ()
            self.state = 89
            self.match(Python3dParser.ASSIGN_EQUAL)
            self.state = 90
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(Python3dParser.NAME, 0)

        def typ(self):
            return self.getTypedRuleContext(Python3dParser.TypContext,0)


        def getRuleIndex(self):
            return Python3dParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = Python3dParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(Python3dParser.NAME)
            self.state = 93
            self.match(Python3dParser.T__0)
            self.state = 94
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nontype_initializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GRZLYNAME(self):
            return self.getToken(Python3dParser.GRZLYNAME, 0)

        def ASSIGN_EQUAL(self):
            return self.getToken(Python3dParser.ASSIGN_EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(Python3dParser.ExprContext,0)


        def NAME(self):
            return self.getToken(Python3dParser.NAME, 0)

        def getRuleIndex(self):
            return Python3dParser.RULE_nontype_initialization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNontype_initialization" ):
                listener.enterNontype_initialization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNontype_initialization" ):
                listener.exitNontype_initialization(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNontype_initialization" ):
                return visitor.visitNontype_initialization(self)
            else:
                return visitor.visitChildren(self)




    def nontype_initialization(self):

        localctx = Python3dParser.Nontype_initializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_nontype_initialization)
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Python3dParser.GRZLYNAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(Python3dParser.GRZLYNAME)
                self.state = 97
                self.match(Python3dParser.ASSIGN_EQUAL)
                self.state = 98
                self.expr(0)
                pass
            elif token in [Python3dParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.match(Python3dParser.NAME)
                self.state = 100
                self.match(Python3dParser.ASSIGN_EQUAL)
                self.state = 101
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Flow_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def break_stmt(self):
            return self.getTypedRuleContext(Python3dParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(Python3dParser.Continue_stmtContext,0)


        def getRuleIndex(self):
            return Python3dParser.RULE_flow_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlow_stmt" ):
                listener.enterFlow_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlow_stmt" ):
                listener.exitFlow_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlow_stmt" ):
                return visitor.visitFlow_stmt(self)
            else:
                return visitor.visitChildren(self)




    def flow_stmt(self):

        localctx = Python3dParser.Flow_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_flow_stmt)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Python3dParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.break_stmt()
                pass
            elif token in [Python3dParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.continue_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Python3dParser.RULE_break_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_stmt" ):
                listener.enterBreak_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_stmt" ):
                listener.exitBreak_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = Python3dParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(Python3dParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Python3dParser.RULE_continue_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue_stmt" ):
                listener.enterContinue_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue_stmt" ):
                listener.exitContinue_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = Python3dParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(Python3dParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(Python3dParser.ExprContext,0)


        def getRuleIndex(self):
            return Python3dParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = Python3dParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(Python3dParser.T__3)
            self.state = 113
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(Python3dParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(Python3dParser.While_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(Python3dParser.For_stmtContext,0)


        def getRuleIndex(self):
            return Python3dParser.RULE_compound_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_stmt" ):
                listener.enterCompound_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_stmt" ):
                listener.exitCompound_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_stmt" ):
                return visitor.visitCompound_stmt(self)
            else:
                return visitor.visitChildren(self)




    def compound_stmt(self):

        localctx = Python3dParser.Compound_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_compound_stmt)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Python3dParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.if_stmt()
                pass
            elif token in [Python3dParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.while_stmt()
                pass
            elif token in [Python3dParser.T__8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.for_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Python3dParser.TestContext)
            else:
                return self.getTypedRuleContext(Python3dParser.TestContext,i)


        def suite(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Python3dParser.SuiteContext)
            else:
                return self.getTypedRuleContext(Python3dParser.SuiteContext,i)


        def getRuleIndex(self):
            return Python3dParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = Python3dParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(Python3dParser.T__4)
            self.state = 121
            self.test()
            self.state = 122
            self.match(Python3dParser.T__0)
            self.state = 123
            self.suite()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Python3dParser.T__5:
                self.state = 124
                self.match(Python3dParser.T__5)
                self.state = 125
                self.test()
                self.state = 126
                self.match(Python3dParser.T__0)
                self.state = 127
                self.suite()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Python3dParser.T__6:
                self.state = 134
                self.match(Python3dParser.T__6)
                self.state = 135
                self.match(Python3dParser.T__0)
                self.state = 136
                self.suite()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self):
            return self.getTypedRuleContext(Python3dParser.TestContext,0)


        def suite(self):
            return self.getTypedRuleContext(Python3dParser.SuiteContext,0)


        def getRuleIndex(self):
            return Python3dParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = Python3dParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(Python3dParser.T__7)
            self.state = 140
            self.test()
            self.state = 141
            self.match(Python3dParser.T__0)
            self.state = 142
            self.suite()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Python3dParser.ExprContext)
            else:
                return self.getTypedRuleContext(Python3dParser.ExprContext,i)


        def rang(self):
            return self.getTypedRuleContext(Python3dParser.RangContext,0)


        def suite(self):
            return self.getTypedRuleContext(Python3dParser.SuiteContext,0)


        def GRZLYNAME(self):
            return self.getToken(Python3dParser.GRZLYNAME, 0)

        def getRuleIndex(self):
            return Python3dParser.RULE_for_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stmt" ):
                listener.enterFor_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stmt" ):
                listener.exitFor_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = Python3dParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_for_stmt)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(Python3dParser.T__8)
                self.state = 145
                self.expr(0)
                self.state = 146
                self.match(Python3dParser.T__9)
                self.state = 147
                self.rang()
                self.state = 148
                self.match(Python3dParser.T__0)
                self.state = 149
                self.suite()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(Python3dParser.T__8)
                self.state = 152
                self.expr(0)
                self.state = 153
                self.match(Python3dParser.T__9)
                self.state = 156
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [Python3dParser.STRING, Python3dParser.NUMBER, Python3dParser.NAME, Python3dParser.OPEN_PAREN, Python3dParser.OPEN_BRACK]:
                    self.state = 154
                    self.expr(0)
                    pass
                elif token in [Python3dParser.GRZLYNAME]:
                    self.state = 155
                    self.match(Python3dParser.GRZLYNAME)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 158
                self.match(Python3dParser.T__0)
                self.state = 159
                self.suite()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuiteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmt(self):
            return self.getTypedRuleContext(Python3dParser.Simple_stmtContext,0)


        def NEWLINE(self):
            return self.getToken(Python3dParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(Python3dParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(Python3dParser.DEDENT, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Python3dParser.StmtContext)
            else:
                return self.getTypedRuleContext(Python3dParser.StmtContext,i)


        def getRuleIndex(self):
            return Python3dParser.RULE_suite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuite" ):
                listener.enterSuite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuite" ):
                listener.exitSuite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuite" ):
                return visitor.visitSuite(self)
            else:
                return visitor.visitChildren(self)




    def suite(self):

        localctx = Python3dParser.SuiteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_suite)
        self._la = 0 # Token type
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Python3dParser.T__1, Python3dParser.T__2, Python3dParser.T__3, Python3dParser.T__12, Python3dParser.GRZLYNAME, Python3dParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.simple_stmt()
                pass
            elif token in [Python3dParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(Python3dParser.NEWLINE)
                self.state = 165
                self.match(Python3dParser.INDENT)
                self.state = 167 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 166
                    self.stmt()
                    self.state = 169 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Python3dParser.T__1) | (1 << Python3dParser.T__2) | (1 << Python3dParser.T__3) | (1 << Python3dParser.T__4) | (1 << Python3dParser.T__7) | (1 << Python3dParser.T__8) | (1 << Python3dParser.T__12) | (1 << Python3dParser.GRZLYNAME) | (1 << Python3dParser.NAME))) != 0)):
                        break

                self.state = 171
                self.match(Python3dParser.DEDENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(Python3dParser.OPEN_PAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Python3dParser.ExprContext)
            else:
                return self.getTypedRuleContext(Python3dParser.ExprContext,i)


        def CLOSE_PAREN(self):
            return self.getToken(Python3dParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return Python3dParser.RULE_rang

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRang" ):
                listener.enterRang(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRang" ):
                listener.exitRang(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRang" ):
                return visitor.visitRang(self)
            else:
                return visitor.visitChildren(self)




    def rang(self):

        localctx = Python3dParser.RangContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_rang)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(Python3dParser.T__10)
            self.state = 176
            self.match(Python3dParser.OPEN_PAREN)
            self.state = 177
            self.expr(0)
            self.state = 178
            self.match(Python3dParser.T__11)
            self.state = 179
            self.expr(0)
            self.state = 180
            self.match(Python3dParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Python3dParser.ExprContext)
            else:
                return self.getTypedRuleContext(Python3dParser.ExprContext,i)


        def comp_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Python3dParser.Comp_opContext)
            else:
                return self.getTypedRuleContext(Python3dParser.Comp_opContext,i)


        def getRuleIndex(self):
            return Python3dParser.RULE_test

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTest" ):
                listener.enterTest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTest" ):
                listener.exitTest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTest" ):
                return visitor.visitTest(self)
            else:
                return visitor.visitChildren(self)




    def test(self):

        localctx = Python3dParser.TestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_test)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.expr(0)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Python3dParser.T__13) | (1 << Python3dParser.T__14) | (1 << Python3dParser.T__15) | (1 << Python3dParser.T__16) | (1 << Python3dParser.T__17) | (1 << Python3dParser.T__18))) != 0):
                self.state = 183
                self.comp_op()
                self.state = 184
                self.expr(0)
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(Python3dParser.OPEN_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(Python3dParser.ExprContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(Python3dParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return Python3dParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_stmt" ):
                return visitor.visitPrint_stmt(self)
            else:
                return visitor.visitChildren(self)




    def print_stmt(self):

        localctx = Python3dParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_print_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(Python3dParser.T__12)
            self.state = 192
            self.match(Python3dParser.OPEN_PAREN)
            self.state = 193
            self.expr(0)
            self.state = 194
            self.match(Python3dParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comp_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Python3dParser.RULE_comp_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp_op" ):
                listener.enterComp_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp_op" ):
                listener.exitComp_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp_op" ):
                return visitor.visitComp_op(self)
            else:
                return visitor.visitChildren(self)




    def comp_op(self):

        localctx = Python3dParser.Comp_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_comp_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Python3dParser.T__13) | (1 << Python3dParser.T__14) | (1 << Python3dParser.T__15) | (1 << Python3dParser.T__16) | (1 << Python3dParser.T__17) | (1 << Python3dParser.T__18))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(Python3dParser.NAME, 0)

        def STRING(self):
            return self.getToken(Python3dParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(Python3dParser.NUMBER, 0)

        def db_reference(self):
            return self.getTypedRuleContext(Python3dParser.Db_referenceContext,0)


        def OPEN_PAREN(self):
            return self.getToken(Python3dParser.OPEN_PAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Python3dParser.ExprContext)
            else:
                return self.getTypedRuleContext(Python3dParser.ExprContext,i)


        def CLOSE_PAREN(self):
            return self.getToken(Python3dParser.CLOSE_PAREN, 0)

        def OPEN_BRACK(self):
            return self.getToken(Python3dParser.OPEN_BRACK, 0)

        def CLOSE_BRACK(self):
            return self.getToken(Python3dParser.CLOSE_BRACK, 0)

        def comp_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Python3dParser.Comp_opContext)
            else:
                return self.getTypedRuleContext(Python3dParser.Comp_opContext,i)


        def getRuleIndex(self):
            return Python3dParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Python3dParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 199
                self.match(Python3dParser.NAME)
                pass

            elif la_ == 2:
                self.state = 200
                self.match(Python3dParser.STRING)
                pass

            elif la_ == 3:
                self.state = 201
                self.match(Python3dParser.NUMBER)
                pass

            elif la_ == 4:
                self.state = 202
                self.db_reference()
                pass

            elif la_ == 5:
                self.state = 203
                self.match(Python3dParser.OPEN_PAREN)
                self.state = 204
                self.expr(0)
                self.state = 205
                self.match(Python3dParser.CLOSE_PAREN)
                pass

            elif la_ == 6:
                self.state = 207
                self.match(Python3dParser.OPEN_BRACK)
                self.state = 208
                self.expr(0)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Python3dParser.T__13) | (1 << Python3dParser.T__14) | (1 << Python3dParser.T__15) | (1 << Python3dParser.T__16) | (1 << Python3dParser.T__17) | (1 << Python3dParser.T__18))) != 0):
                    self.state = 209
                    self.comp_op()
                    self.state = 210
                    self.expr(0)
                    self.state = 216
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 217
                self.match(Python3dParser.CLOSE_BRACK)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 239
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = Python3dParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 221
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 222
                        self.match(Python3dParser.T__23)
                        self.state = 223
                        self.expr(3)
                        pass

                    elif la_ == 2:
                        localctx = Python3dParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 224
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 225
                        self.match(Python3dParser.T__11)
                        self.state = 226
                        self.expr(2)
                        pass

                    elif la_ == 3:
                        localctx = Python3dParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 227
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 230 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 228
                                _la = self._input.LA(1)
                                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Python3dParser.T__19) | (1 << Python3dParser.T__20) | (1 << Python3dParser.T__21) | (1 << Python3dParser.T__22))) != 0)):
                                    self._errHandler.recoverInline(self)
                                else:
                                    self._errHandler.reportMatch(self)
                                    self.consume()
                                self.state = 229
                                self.expr(0)

                            else:
                                raise NoViableAltException(self)
                            self.state = 232 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                        pass

                    elif la_ == 4:
                        localctx = Python3dParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 234
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 235
                        self.match(Python3dParser.OPEN_PAREN)
                        self.state = 236
                        self.expr(0)
                        self.state = 237
                        self.match(Python3dParser.CLOSE_PAREN)
                        pass

             
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Python3dParser.RULE_typ

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyp" ):
                listener.enterTyp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyp" ):
                listener.exitTyp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = Python3dParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Python3dParser.T__24) | (1 << Python3dParser.T__25) | (1 << Python3dParser.T__26) | (1 << Python3dParser.T__27))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_charsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self, i:int=None):
            if i is None:
                return self.getTokens(Python3dParser.OPEN_PAREN)
            else:
                return self.getToken(Python3dParser.OPEN_PAREN, i)

        def CLOSE_PAREN(self, i:int=None):
            if i is None:
                return self.getTokens(Python3dParser.CLOSE_PAREN)
            else:
                return self.getToken(Python3dParser.CLOSE_PAREN, i)

        def OPEN_BRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Python3dParser.OPEN_BRACK)
            else:
                return self.getToken(Python3dParser.OPEN_BRACK, i)

        def CLOSE_BRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Python3dParser.CLOSE_BRACK)
            else:
                return self.getToken(Python3dParser.CLOSE_BRACK, i)

        def OPEN_BRACE(self, i:int=None):
            if i is None:
                return self.getTokens(Python3dParser.OPEN_BRACE)
            else:
                return self.getToken(Python3dParser.OPEN_BRACE, i)

        def CLOSE_BRACE(self, i:int=None):
            if i is None:
                return self.getTokens(Python3dParser.CLOSE_BRACE)
            else:
                return self.getToken(Python3dParser.CLOSE_BRACE, i)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(Python3dParser.NAME)
            else:
                return self.getToken(Python3dParser.NAME, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(Python3dParser.STRING)
            else:
                return self.getToken(Python3dParser.STRING, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(Python3dParser.NUMBER)
            else:
                return self.getToken(Python3dParser.NUMBER, i)

        def ASSIGN_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(Python3dParser.ASSIGN_EQUAL)
            else:
                return self.getToken(Python3dParser.ASSIGN_EQUAL, i)

        def getRuleIndex(self):
            return Python3dParser.RULE_all_chars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAll_chars" ):
                listener.enterAll_chars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAll_chars" ):
                listener.exitAll_chars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_chars" ):
                return visitor.visitAll_chars(self)
            else:
                return visitor.visitChildren(self)




    def all_chars(self):

        localctx = Python3dParser.All_charsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_all_chars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 246
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Python3dParser.T__0) | (1 << Python3dParser.T__11) | (1 << Python3dParser.T__13) | (1 << Python3dParser.T__14) | (1 << Python3dParser.T__15) | (1 << Python3dParser.T__16) | (1 << Python3dParser.T__17) | (1 << Python3dParser.T__18) | (1 << Python3dParser.T__19) | (1 << Python3dParser.T__20) | (1 << Python3dParser.T__21) | (1 << Python3dParser.T__22) | (1 << Python3dParser.T__23) | (1 << Python3dParser.T__28) | (1 << Python3dParser.STRING) | (1 << Python3dParser.NUMBER) | (1 << Python3dParser.NAME) | (1 << Python3dParser.OPEN_PAREN) | (1 << Python3dParser.CLOSE_PAREN) | (1 << Python3dParser.OPEN_BRACK) | (1 << Python3dParser.CLOSE_BRACK) | (1 << Python3dParser.OPEN_BRACE) | (1 << Python3dParser.CLOSE_BRACE) | (1 << Python3dParser.ASSIGN_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 249 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Python3dParser.T__0) | (1 << Python3dParser.T__11) | (1 << Python3dParser.T__13) | (1 << Python3dParser.T__14) | (1 << Python3dParser.T__15) | (1 << Python3dParser.T__16) | (1 << Python3dParser.T__17) | (1 << Python3dParser.T__18) | (1 << Python3dParser.T__19) | (1 << Python3dParser.T__20) | (1 << Python3dParser.T__21) | (1 << Python3dParser.T__22) | (1 << Python3dParser.T__23) | (1 << Python3dParser.T__28) | (1 << Python3dParser.STRING) | (1 << Python3dParser.NUMBER) | (1 << Python3dParser.NAME) | (1 << Python3dParser.OPEN_PAREN) | (1 << Python3dParser.CLOSE_PAREN) | (1 << Python3dParser.OPEN_BRACK) | (1 << Python3dParser.CLOSE_BRACK) | (1 << Python3dParser.OPEN_BRACE) | (1 << Python3dParser.CLOSE_BRACE) | (1 << Python3dParser.ASSIGN_EQUAL))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Db_referenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(Python3dParser.NAME)
            else:
                return self.getToken(Python3dParser.NAME, i)

        def getRuleIndex(self):
            return Python3dParser.RULE_db_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDb_reference" ):
                listener.enterDb_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDb_reference" ):
                listener.exitDb_reference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDb_reference" ):
                return visitor.visitDb_reference(self)
            else:
                return visitor.visitChildren(self)




    def db_reference(self):

        localctx = Python3dParser.Db_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_db_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(Python3dParser.NAME)
            self.state = 252
            self.match(Python3dParser.T__23)
            self.state = 253
            self.match(Python3dParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[22] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




