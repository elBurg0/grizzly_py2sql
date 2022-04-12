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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u00ff\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\3\2")
        buf.write("\3\2\3\2\3\2\5\2@\n\2\3\3\3\3\7\3D\n\3\f\3\16\3G\13\3")
        buf.write("\3\3\3\3\3\4\3\4\5\4M\n\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\5\6W\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7`\n\7\3\b")
        buf.write("\3\b\3\b\3\b\5\bf\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\5\tq\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\r\3\r\5\r\u0083\n\r\3\16\3\16\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\5\21\u008f\n\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u009a")
        buf.write("\n\22\f\22\16\22\u009d\13\22\3\22\3\22\3\22\5\22\u00a2")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00b7")
        buf.write("\n\24\3\25\3\25\3\25\3\25\6\25\u00bd\n\25\r\25\16\25\u00be")
        buf.write("\3\25\3\25\5\25\u00c3\n\25\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\27\3\27\3\27\3\27\7\27\u00d0\n\27\f\27\16\27")
        buf.write("\u00d3\13\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u00e6")
        buf.write("\n\32\3\32\3\32\3\32\6\32\u00eb\n\32\r\32\16\32\u00ec")
        buf.write("\7\32\u00ef\n\32\f\32\16\32\u00f2\13\32\3\33\3\33\3\34")
        buf.write("\6\34\u00f7\n\34\r\34\16\34\u00f8\3\35\3\35\3\35\3\35")
        buf.write("\3\35\2\3\62\36\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668\2\6\3\2\22\27\3\2\30\33\3\2\34")
        buf.write("\37\b\2\5\5\20\20\22\33 #((+\61\2\u0101\2?\3\2\2\2\4E")
        buf.write("\3\2\2\2\6L\3\2\2\2\bN\3\2\2\2\nV\3\2\2\2\f_\3\2\2\2\16")
        buf.write("e\3\2\2\2\20p\3\2\2\2\22r\3\2\2\2\24x\3\2\2\2\26|\3\2")
        buf.write("\2\2\30\u0082\3\2\2\2\32\u0084\3\2\2\2\34\u0086\3\2\2")
        buf.write("\2\36\u0088\3\2\2\2 \u008e\3\2\2\2\"\u0090\3\2\2\2$\u00a3")
        buf.write("\3\2\2\2&\u00b6\3\2\2\2(\u00c2\3\2\2\2*\u00c4\3\2\2\2")
        buf.write(",\u00cb\3\2\2\2.\u00d4\3\2\2\2\60\u00d9\3\2\2\2\62\u00e5")
        buf.write("\3\2\2\2\64\u00f3\3\2\2\2\66\u00f6\3\2\2\28\u00fa\3\2")
        buf.write("\2\2:@\7&\2\2;@\5\b\5\2<=\5 \21\2=>\7&\2\2>@\3\2\2\2?")
        buf.write(":\3\2\2\2?;\3\2\2\2?<\3\2\2\2@\3\3\2\2\2AD\7&\2\2BD\5")
        buf.write("\6\4\2CA\3\2\2\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2")
        buf.write("\2FH\3\2\2\2GE\3\2\2\2HI\7\2\2\3I\5\3\2\2\2JM\5\b\5\2")
        buf.write("KM\5 \21\2LJ\3\2\2\2LK\3\2\2\2M\7\3\2\2\2NO\5\n\6\2OP")
        buf.write("\7&\2\2P\t\3\2\2\2QW\5\f\7\2RW\5\16\b\2SW\5\30\r\2TW\5")
        buf.write(".\30\2UW\5\36\20\2VQ\3\2\2\2VR\3\2\2\2VS\3\2\2\2VT\3\2")
        buf.write("\2\2VU\3\2\2\2W\13\3\2\2\2XY\7\'\2\2Y`\5\66\34\2Z[\7\3")
        buf.write("\2\2[\\\7+\2\2\\]\5\66\34\2]^\7,\2\2^`\3\2\2\2_X\3\2\2")
        buf.write("\2_Z\3\2\2\2`\r\3\2\2\2af\5\20\t\2bf\5\24\13\2cf\5\26")
        buf.write("\f\2df\5\22\n\2ea\3\2\2\2eb\3\2\2\2ec\3\2\2\2ed\3\2\2")
        buf.write("\2f\17\3\2\2\2gh\7\'\2\2hi\7\61\2\2iq\5\62\32\2jk\7\'")
        buf.write("\2\2kl\7\61\2\2lm\7\4\2\2mn\7+\2\2no\7\"\2\2oq\7,\2\2")
        buf.write("pg\3\2\2\2pj\3\2\2\2q\21\3\2\2\2rs\7(\2\2st\7\5\2\2tu")
        buf.write("\5\64\33\2uv\7\61\2\2vw\5\62\32\2w\23\3\2\2\2xy\7(\2\2")
        buf.write("yz\7\5\2\2z{\5\64\33\2{\25\3\2\2\2|}\7(\2\2}~\7\61\2\2")
        buf.write("~\177\5\62\32\2\177\27\3\2\2\2\u0080\u0083\5\32\16\2\u0081")
        buf.write("\u0083\5\34\17\2\u0082\u0080\3\2\2\2\u0082\u0081\3\2\2")
        buf.write("\2\u0083\31\3\2\2\2\u0084\u0085\7\6\2\2\u0085\33\3\2\2")
        buf.write("\2\u0086\u0087\7\7\2\2\u0087\35\3\2\2\2\u0088\u0089\7")
        buf.write("\b\2\2\u0089\u008a\5\62\32\2\u008a\37\3\2\2\2\u008b\u008f")
        buf.write("\5\"\22\2\u008c\u008f\5$\23\2\u008d\u008f\5&\24\2\u008e")
        buf.write("\u008b\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008d\3\2\2\2")
        buf.write("\u008f!\3\2\2\2\u0090\u0091\7\t\2\2\u0091\u0092\5,\27")
        buf.write("\2\u0092\u0093\7\5\2\2\u0093\u009b\5(\25\2\u0094\u0095")
        buf.write("\7\n\2\2\u0095\u0096\5,\27\2\u0096\u0097\7\5\2\2\u0097")
        buf.write("\u0098\5(\25\2\u0098\u009a\3\2\2\2\u0099\u0094\3\2\2\2")
        buf.write("\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3")
        buf.write("\2\2\2\u009c\u00a1\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u009f")
        buf.write("\7\13\2\2\u009f\u00a0\7\5\2\2\u00a0\u00a2\5(\25\2\u00a1")
        buf.write("\u009e\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2#\3\2\2\2\u00a3")
        buf.write("\u00a4\7\f\2\2\u00a4\u00a5\5,\27\2\u00a5\u00a6\7\5\2\2")
        buf.write("\u00a6\u00a7\5(\25\2\u00a7%\3\2\2\2\u00a8\u00a9\7\r\2")
        buf.write("\2\u00a9\u00aa\5\62\32\2\u00aa\u00ab\7\16\2\2\u00ab\u00ac")
        buf.write("\5*\26\2\u00ac\u00ad\7\5\2\2\u00ad\u00ae\5(\25\2\u00ae")
        buf.write("\u00b7\3\2\2\2\u00af\u00b0\7\r\2\2\u00b0\u00b1\5\62\32")
        buf.write("\2\u00b1\u00b2\7\16\2\2\u00b2\u00b3\5\62\32\2\u00b3\u00b4")
        buf.write("\7\5\2\2\u00b4\u00b5\5(\25\2\u00b5\u00b7\3\2\2\2\u00b6")
        buf.write("\u00a8\3\2\2\2\u00b6\u00af\3\2\2\2\u00b7\'\3\2\2\2\u00b8")
        buf.write("\u00c3\5\b\5\2\u00b9\u00ba\7&\2\2\u00ba\u00bc\7\64\2\2")
        buf.write("\u00bb\u00bd\5\6\4\2\u00bc\u00bb\3\2\2\2\u00bd\u00be\3")
        buf.write("\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c0")
        buf.write("\3\2\2\2\u00c0\u00c1\7\65\2\2\u00c1\u00c3\3\2\2\2\u00c2")
        buf.write("\u00b8\3\2\2\2\u00c2\u00b9\3\2\2\2\u00c3)\3\2\2\2\u00c4")
        buf.write("\u00c5\7\17\2\2\u00c5\u00c6\7+\2\2\u00c6\u00c7\5\62\32")
        buf.write("\2\u00c7\u00c8\7\20\2\2\u00c8\u00c9\5\62\32\2\u00c9\u00ca")
        buf.write("\7,\2\2\u00ca+\3\2\2\2\u00cb\u00d1\5\62\32\2\u00cc\u00cd")
        buf.write("\5\60\31\2\u00cd\u00ce\5\62\32\2\u00ce\u00d0\3\2\2\2\u00cf")
        buf.write("\u00cc\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2")
        buf.write("\u00d1\u00d2\3\2\2\2\u00d2-\3\2\2\2\u00d3\u00d1\3\2\2")
        buf.write("\2\u00d4\u00d5\7\21\2\2\u00d5\u00d6\7+\2\2\u00d6\u00d7")
        buf.write("\5\62\32\2\u00d7\u00d8\7,\2\2\u00d8/\3\2\2\2\u00d9\u00da")
        buf.write("\t\2\2\2\u00da\61\3\2\2\2\u00db\u00dc\b\32\1\2\u00dc\u00e6")
        buf.write("\7(\2\2\u00dd\u00e6\7\"\2\2\u00de\u00e6\7#\2\2\u00df\u00e6")
        buf.write("\7\'\2\2\u00e0\u00e6\58\35\2\u00e1\u00e2\7+\2\2\u00e2")
        buf.write("\u00e3\5\62\32\2\u00e3\u00e4\7,\2\2\u00e4\u00e6\3\2\2")
        buf.write("\2\u00e5\u00db\3\2\2\2\u00e5\u00dd\3\2\2\2\u00e5\u00de")
        buf.write("\3\2\2\2\u00e5\u00df\3\2\2\2\u00e5\u00e0\3\2\2\2\u00e5")
        buf.write("\u00e1\3\2\2\2\u00e6\u00f0\3\2\2\2\u00e7\u00ea\f\t\2\2")
        buf.write("\u00e8\u00e9\t\3\2\2\u00e9\u00eb\5\62\32\2\u00ea\u00e8")
        buf.write("\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec")
        buf.write("\u00ed\3\2\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00e7\3\2\2\2")
        buf.write("\u00ef\u00f2\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3")
        buf.write("\2\2\2\u00f1\63\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3\u00f4")
        buf.write("\t\4\2\2\u00f4\65\3\2\2\2\u00f5\u00f7\t\5\2\2\u00f6\u00f5")
        buf.write("\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8")
        buf.write("\u00f9\3\2\2\2\u00f9\67\3\2\2\2\u00fa\u00fb\7(\2\2\u00fb")
        buf.write("\u00fc\7!\2\2\u00fc\u00fd\7(\2\2\u00fd9\3\2\2\2\26?CE")
        buf.write("LV_ep\u0082\u008e\u009b\u00a1\u00b6\u00be\u00c2\u00d1")
        buf.write("\u00e5\u00ec\u00f0\u00f8")
        return buf.getvalue()


class Python3dParser ( Parser ):

    grammarFileName = "Python3d.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'grizzly.use'", "'grizzly.read_table'", 
                     "':'", "'break'", "'continue'", "'return'", "'if'", 
                     "'elif'", "'else'", "'while'", "'for'", "'in'", "'range'", 
                     "','", "'print'", "'<'", "'>'", "'=='", "'>='", "'<='", 
                     "'!='", "'+'", "'-'", "'*'", "'/'", "'int'", "'str'", 
                     "'list'", "'float'", "'\"'", "'.'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "STRING", "NUMBER", "FLOAT", "INTEGER", "NEWLINE", 
                      "GRZLYNAME", "NAME", "STRING_LITERAL", "DECIMAL_INTEGER", 
                      "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", 
                      "OPEN_BRACE", "CLOSE_BRACE", "ASSIGN_EQUAL", "SKIP_", 
                      "UNKNOWN_CHAR", "INDENT", "DEDENT" ]

    RULE_single_input = 0
    RULE_file_input = 1
    RULE_stmt = 2
    RULE_simple_stmt = 3
    RULE_small_stmt = 4
    RULE_grizzly_stmt = 5
    RULE_assignment_stmt = 6
    RULE_grizzly_assignment = 7
    RULE_initialization = 8
    RULE_declaration = 9
    RULE_nontype_initialization = 10
    RULE_flow_stmt = 11
    RULE_break_stmt = 12
    RULE_continue_stmt = 13
    RULE_return_stmt = 14
    RULE_compound_stmt = 15
    RULE_if_stmt = 16
    RULE_while_stmt = 17
    RULE_for_stmt = 18
    RULE_suite = 19
    RULE_rang = 20
    RULE_test = 21
    RULE_print_stmt = 22
    RULE_comp_op = 23
    RULE_expr = 24
    RULE_typ = 25
    RULE_all_chars = 26
    RULE_db_reference = 27

    ruleNames =  [ "single_input", "file_input", "stmt", "simple_stmt", 
                   "small_stmt", "grizzly_stmt", "assignment_stmt", "grizzly_assignment", 
                   "initialization", "declaration", "nontype_initialization", 
                   "flow_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "compound_stmt", "if_stmt", "while_stmt", "for_stmt", 
                   "suite", "rang", "test", "print_stmt", "comp_op", "expr", 
                   "typ", "all_chars", "db_reference" ]

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
    T__29=30
    T__30=31
    STRING=32
    NUMBER=33
    FLOAT=34
    INTEGER=35
    NEWLINE=36
    GRZLYNAME=37
    NAME=38
    STRING_LITERAL=39
    DECIMAL_INTEGER=40
    OPEN_PAREN=41
    CLOSE_PAREN=42
    OPEN_BRACK=43
    CLOSE_BRACK=44
    OPEN_BRACE=45
    CLOSE_BRACE=46
    ASSIGN_EQUAL=47
    SKIP_=48
    UNKNOWN_CHAR=49
    INDENT=50
    DEDENT=51

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
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Python3dParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(Python3dParser.NEWLINE)
                pass
            elif token in [Python3dParser.T__0, Python3dParser.T__3, Python3dParser.T__4, Python3dParser.T__5, Python3dParser.T__14, Python3dParser.GRZLYNAME, Python3dParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.simple_stmt()
                pass
            elif token in [Python3dParser.T__6, Python3dParser.T__9, Python3dParser.T__10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.compound_stmt()
                self.state = 59
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
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Python3dParser.T__0) | (1 << Python3dParser.T__3) | (1 << Python3dParser.T__4) | (1 << Python3dParser.T__5) | (1 << Python3dParser.T__6) | (1 << Python3dParser.T__9) | (1 << Python3dParser.T__10) | (1 << Python3dParser.T__14) | (1 << Python3dParser.NEWLINE) | (1 << Python3dParser.GRZLYNAME) | (1 << Python3dParser.NAME))) != 0):
                self.state = 65
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [Python3dParser.NEWLINE]:
                    self.state = 63
                    self.match(Python3dParser.NEWLINE)
                    pass
                elif token in [Python3dParser.T__0, Python3dParser.T__3, Python3dParser.T__4, Python3dParser.T__5, Python3dParser.T__6, Python3dParser.T__9, Python3dParser.T__10, Python3dParser.T__14, Python3dParser.GRZLYNAME, Python3dParser.NAME]:
                    self.state = 64
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
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
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Python3dParser.T__0, Python3dParser.T__3, Python3dParser.T__4, Python3dParser.T__5, Python3dParser.T__14, Python3dParser.GRZLYNAME, Python3dParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.simple_stmt()
                pass
            elif token in [Python3dParser.T__6, Python3dParser.T__9, Python3dParser.T__10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
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
            self.state = 76
            self.small_stmt()
            self.state = 77
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

        def grizzly_stmt(self):
            return self.getTypedRuleContext(Python3dParser.Grizzly_stmtContext,0)


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
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.grizzly_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.assignment_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.flow_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.print_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 83
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Grizzly_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GRZLYNAME(self):
            return self.getToken(Python3dParser.GRZLYNAME, 0)

        def all_chars(self):
            return self.getTypedRuleContext(Python3dParser.All_charsContext,0)


        def OPEN_PAREN(self):
            return self.getToken(Python3dParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(Python3dParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return Python3dParser.RULE_grizzly_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrizzly_stmt" ):
                listener.enterGrizzly_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrizzly_stmt" ):
                listener.exitGrizzly_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrizzly_stmt" ):
                return visitor.visitGrizzly_stmt(self)
            else:
                return visitor.visitChildren(self)




    def grizzly_stmt(self):

        localctx = Python3dParser.Grizzly_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_grizzly_stmt)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Python3dParser.GRZLYNAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(Python3dParser.GRZLYNAME)
                self.state = 87
                self.all_chars()
                pass
            elif token in [Python3dParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.match(Python3dParser.T__0)
                self.state = 89
                self.match(Python3dParser.OPEN_PAREN)
                self.state = 90
                self.all_chars()
                self.state = 91
                self.match(Python3dParser.CLOSE_PAREN)
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

        def grizzly_assignment(self):
            return self.getTypedRuleContext(Python3dParser.Grizzly_assignmentContext,0)


        def declaration(self):
            return self.getTypedRuleContext(Python3dParser.DeclarationContext,0)


        def nontype_initialization(self):
            return self.getTypedRuleContext(Python3dParser.Nontype_initializationContext,0)


        def initialization(self):
            return self.getTypedRuleContext(Python3dParser.InitializationContext,0)


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
        self.enterRule(localctx, 12, self.RULE_assignment_stmt)
        try:
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.grizzly_assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.nontype_initialization()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.initialization()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Grizzly_assignmentContext(ParserRuleContext):
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


        def OPEN_PAREN(self):
            return self.getToken(Python3dParser.OPEN_PAREN, 0)

        def STRING(self):
            return self.getToken(Python3dParser.STRING, 0)

        def CLOSE_PAREN(self):
            return self.getToken(Python3dParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return Python3dParser.RULE_grizzly_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrizzly_assignment" ):
                listener.enterGrizzly_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrizzly_assignment" ):
                listener.exitGrizzly_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrizzly_assignment" ):
                return visitor.visitGrizzly_assignment(self)
            else:
                return visitor.visitChildren(self)




    def grizzly_assignment(self):

        localctx = Python3dParser.Grizzly_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_grizzly_assignment)
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.match(Python3dParser.GRZLYNAME)
                self.state = 102
                self.match(Python3dParser.ASSIGN_EQUAL)
                self.state = 103
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(Python3dParser.GRZLYNAME)
                self.state = 105
                self.match(Python3dParser.ASSIGN_EQUAL)
                self.state = 106
                self.match(Python3dParser.T__1)
                self.state = 107
                self.match(Python3dParser.OPEN_PAREN)
                self.state = 108
                self.match(Python3dParser.STRING)
                self.state = 109
                self.match(Python3dParser.CLOSE_PAREN)
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
        self.enterRule(localctx, 16, self.RULE_initialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(Python3dParser.NAME)
            self.state = 113
            self.match(Python3dParser.T__2)
            self.state = 114
            self.typ()
            self.state = 115
            self.match(Python3dParser.ASSIGN_EQUAL)
            self.state = 116
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
        self.enterRule(localctx, 18, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(Python3dParser.NAME)
            self.state = 119
            self.match(Python3dParser.T__2)
            self.state = 120
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

        def NAME(self):
            return self.getToken(Python3dParser.NAME, 0)

        def ASSIGN_EQUAL(self):
            return self.getToken(Python3dParser.ASSIGN_EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(Python3dParser.ExprContext,0)


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
        self.enterRule(localctx, 20, self.RULE_nontype_initialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(Python3dParser.NAME)
            self.state = 123
            self.match(Python3dParser.ASSIGN_EQUAL)
            self.state = 124
            self.expr(0)
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
        self.enterRule(localctx, 22, self.RULE_flow_stmt)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Python3dParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.break_stmt()
                pass
            elif token in [Python3dParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
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
        self.enterRule(localctx, 24, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(Python3dParser.T__3)
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
        self.enterRule(localctx, 26, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(Python3dParser.T__4)
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
        self.enterRule(localctx, 28, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(Python3dParser.T__5)
            self.state = 135
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
        self.enterRule(localctx, 30, self.RULE_compound_stmt)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Python3dParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.if_stmt()
                pass
            elif token in [Python3dParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.while_stmt()
                pass
            elif token in [Python3dParser.T__10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
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
        self.enterRule(localctx, 32, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(Python3dParser.T__6)
            self.state = 143
            self.test()
            self.state = 144
            self.match(Python3dParser.T__2)
            self.state = 145
            self.suite()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Python3dParser.T__7:
                self.state = 146
                self.match(Python3dParser.T__7)
                self.state = 147
                self.test()
                self.state = 148
                self.match(Python3dParser.T__2)
                self.state = 149
                self.suite()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Python3dParser.T__8:
                self.state = 156
                self.match(Python3dParser.T__8)
                self.state = 157
                self.match(Python3dParser.T__2)
                self.state = 158
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
        self.enterRule(localctx, 34, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(Python3dParser.T__9)
            self.state = 162
            self.test()
            self.state = 163
            self.match(Python3dParser.T__2)
            self.state = 164
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
        self.enterRule(localctx, 36, self.RULE_for_stmt)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(Python3dParser.T__10)
                self.state = 167
                self.expr(0)
                self.state = 168
                self.match(Python3dParser.T__11)
                self.state = 169
                self.rang()
                self.state = 170
                self.match(Python3dParser.T__2)
                self.state = 171
                self.suite()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(Python3dParser.T__10)
                self.state = 174
                self.expr(0)
                self.state = 175
                self.match(Python3dParser.T__11)
                self.state = 176
                self.expr(0)
                self.state = 177
                self.match(Python3dParser.T__2)
                self.state = 178
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
        self.enterRule(localctx, 38, self.RULE_suite)
        self._la = 0 # Token type
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Python3dParser.T__0, Python3dParser.T__3, Python3dParser.T__4, Python3dParser.T__5, Python3dParser.T__14, Python3dParser.GRZLYNAME, Python3dParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.simple_stmt()
                pass
            elif token in [Python3dParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.match(Python3dParser.NEWLINE)
                self.state = 184
                self.match(Python3dParser.INDENT)
                self.state = 186 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 185
                    self.stmt()
                    self.state = 188 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Python3dParser.T__0) | (1 << Python3dParser.T__3) | (1 << Python3dParser.T__4) | (1 << Python3dParser.T__5) | (1 << Python3dParser.T__6) | (1 << Python3dParser.T__9) | (1 << Python3dParser.T__10) | (1 << Python3dParser.T__14) | (1 << Python3dParser.GRZLYNAME) | (1 << Python3dParser.NAME))) != 0)):
                        break

                self.state = 190
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
        self.enterRule(localctx, 40, self.RULE_rang)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(Python3dParser.T__12)
            self.state = 195
            self.match(Python3dParser.OPEN_PAREN)
            self.state = 196
            self.expr(0)
            self.state = 197
            self.match(Python3dParser.T__13)
            self.state = 198
            self.expr(0)
            self.state = 199
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
        self.enterRule(localctx, 42, self.RULE_test)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.expr(0)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Python3dParser.T__15) | (1 << Python3dParser.T__16) | (1 << Python3dParser.T__17) | (1 << Python3dParser.T__18) | (1 << Python3dParser.T__19) | (1 << Python3dParser.T__20))) != 0):
                self.state = 202
                self.comp_op()
                self.state = 203
                self.expr(0)
                self.state = 209
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
        self.enterRule(localctx, 44, self.RULE_print_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(Python3dParser.T__14)
            self.state = 211
            self.match(Python3dParser.OPEN_PAREN)
            self.state = 212
            self.expr(0)
            self.state = 213
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
        self.enterRule(localctx, 46, self.RULE_comp_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Python3dParser.T__15) | (1 << Python3dParser.T__16) | (1 << Python3dParser.T__17) | (1 << Python3dParser.T__18) | (1 << Python3dParser.T__19) | (1 << Python3dParser.T__20))) != 0)):
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

        def GRZLYNAME(self):
            return self.getToken(Python3dParser.GRZLYNAME, 0)

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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 218
                self.match(Python3dParser.NAME)
                pass

            elif la_ == 2:
                self.state = 219
                self.match(Python3dParser.STRING)
                pass

            elif la_ == 3:
                self.state = 220
                self.match(Python3dParser.NUMBER)
                pass

            elif la_ == 4:
                self.state = 221
                self.match(Python3dParser.GRZLYNAME)
                pass

            elif la_ == 5:
                self.state = 222
                self.db_reference()
                pass

            elif la_ == 6:
                self.state = 223
                self.match(Python3dParser.OPEN_PAREN)
                self.state = 224
                self.expr(0)
                self.state = 225
                self.match(Python3dParser.CLOSE_PAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 238
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Python3dParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 229
                    if not self.precpred(self._ctx, 7):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                    self.state = 232 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 230
                            _la = self._input.LA(1)
                            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Python3dParser.T__21) | (1 << Python3dParser.T__22) | (1 << Python3dParser.T__23) | (1 << Python3dParser.T__24))) != 0)):
                                self._errHandler.recoverInline(self)
                            else:
                                self._errHandler.reportMatch(self)
                                self.consume()
                            self.state = 231
                            self.expr(0)

                        else:
                            raise NoViableAltException(self)
                        self.state = 234 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
             
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        self.enterRule(localctx, 50, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Python3dParser.T__25) | (1 << Python3dParser.T__26) | (1 << Python3dParser.T__27) | (1 << Python3dParser.T__28))) != 0)):
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
        self.enterRule(localctx, 52, self.RULE_all_chars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 243
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Python3dParser.T__2) | (1 << Python3dParser.T__13) | (1 << Python3dParser.T__15) | (1 << Python3dParser.T__16) | (1 << Python3dParser.T__17) | (1 << Python3dParser.T__18) | (1 << Python3dParser.T__19) | (1 << Python3dParser.T__20) | (1 << Python3dParser.T__21) | (1 << Python3dParser.T__22) | (1 << Python3dParser.T__23) | (1 << Python3dParser.T__24) | (1 << Python3dParser.T__29) | (1 << Python3dParser.T__30) | (1 << Python3dParser.STRING) | (1 << Python3dParser.NUMBER) | (1 << Python3dParser.NAME) | (1 << Python3dParser.OPEN_PAREN) | (1 << Python3dParser.CLOSE_PAREN) | (1 << Python3dParser.OPEN_BRACK) | (1 << Python3dParser.CLOSE_BRACK) | (1 << Python3dParser.OPEN_BRACE) | (1 << Python3dParser.CLOSE_BRACE) | (1 << Python3dParser.ASSIGN_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 246 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 54, self.RULE_db_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(Python3dParser.NAME)
            self.state = 249
            self.match(Python3dParser.T__30)
            self.state = 250
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
        self._predicates[24] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         




