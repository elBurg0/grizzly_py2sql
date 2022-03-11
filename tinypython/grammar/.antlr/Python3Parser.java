// Generated from c:\Users\burge\Documents\coding\ANTLR py2sql\tinypython\grammar\Python3.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class Python3Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, STRING=22, NUMBER=23, INTEGER=24, 
		NEWLINE=25, NAME=26, STRING_LITERAL=27, DECIMAL_INTEGER=28, OPEN_PAREN=29, 
		CLOSE_PAREN=30, OPEN_BRACK=31, CLOSE_BRACK=32, OPEN_BRACE=33, CLOSE_BRACE=34, 
		SKIP_=35, UNKNOWN_CHAR=36, INDENT=37, DEDENT=38;
	public static final int
		RULE_single_input = 0, RULE_file_input = 1, RULE_stmt = 2, RULE_simple_stmt = 3, 
		RULE_small_stmt = 4, RULE_assignment_stmt = 5, RULE_flow_stmt = 6, RULE_break_stmt = 7, 
		RULE_continue_stmt = 8, RULE_compound_stmt = 9, RULE_if_stmt = 10, RULE_while_stmt = 11, 
		RULE_for_stmt = 12, RULE_suite = 13, RULE_condition = 14, RULE_print_stmt = 15, 
		RULE_range = 16, RULE_list = 17, RULE_comprehension = 18, RULE_expr = 19;
	private static String[] makeRuleNames() {
		return new String[] {
			"single_input", "file_input", "stmt", "simple_stmt", "small_stmt", "assignment_stmt", 
			"flow_stmt", "break_stmt", "continue_stmt", "compound_stmt", "if_stmt", 
			"while_stmt", "for_stmt", "suite", "condition", "print_stmt", "range", 
			"list", "comprehension", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "'break'", "'continue'", "'if'", "':'", "'elif'", "'else'", 
			"'while'", "'for'", "'in'", "'print'", "'range'", "','", "'<'", "'>'", 
			"'=='", "'>='", "'<='", "'!='", "'+'", "'-'", null, null, null, null, 
			null, null, null, "'('", "')'", "'['", "']'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, "STRING", 
			"NUMBER", "INTEGER", "NEWLINE", "NAME", "STRING_LITERAL", "DECIMAL_INTEGER", 
			"OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", 
			"CLOSE_BRACE", "SKIP_", "UNKNOWN_CHAR", "INDENT", "DEDENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Python3.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public Python3Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class Single_inputContext extends ParserRuleContext {
		public TerminalNode NEWLINE() { return getToken(Python3Parser.NEWLINE, 0); }
		public Simple_stmtContext simple_stmt() {
			return getRuleContext(Simple_stmtContext.class,0);
		}
		public Compound_stmtContext compound_stmt() {
			return getRuleContext(Compound_stmtContext.class,0);
		}
		public Single_inputContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_single_input; }
	}

	public final Single_inputContext single_input() throws RecognitionException {
		Single_inputContext _localctx = new Single_inputContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_single_input);
		try {
			setState(47);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NEWLINE:
				enterOuterAlt(_localctx, 1);
				{
				setState(40);
				match(NEWLINE);
				}
				break;
			case T__1:
			case T__2:
			case T__10:
			case NUMBER:
			case NAME:
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(41);
				simple_stmt();
				setState(42);
				match(NEWLINE);
				}
				break;
			case T__3:
			case T__7:
			case T__8:
				enterOuterAlt(_localctx, 3);
				{
				setState(44);
				compound_stmt();
				setState(45);
				match(NEWLINE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class File_inputContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(Python3Parser.EOF, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(Python3Parser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(Python3Parser.NEWLINE, i);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public File_inputContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_file_input; }
	}

	public final File_inputContext file_input() throws RecognitionException {
		File_inputContext _localctx = new File_inputContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_file_input);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__7) | (1L << T__8) | (1L << T__10) | (1L << NUMBER) | (1L << NEWLINE) | (1L << NAME) | (1L << OPEN_PAREN))) != 0)) {
				{
				setState(51);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case NEWLINE:
					{
					setState(49);
					match(NEWLINE);
					}
					break;
				case T__1:
				case T__2:
				case T__3:
				case T__7:
				case T__8:
				case T__10:
				case NUMBER:
				case NAME:
				case OPEN_PAREN:
					{
					setState(50);
					stmt();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(55);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(56);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StmtContext extends ParserRuleContext {
		public Simple_stmtContext simple_stmt() {
			return getRuleContext(Simple_stmtContext.class,0);
		}
		public Compound_stmtContext compound_stmt() {
			return getRuleContext(Compound_stmtContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_stmt);
		try {
			setState(60);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
			case T__2:
			case T__10:
			case NUMBER:
			case NAME:
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(58);
				simple_stmt();
				}
				break;
			case T__3:
			case T__7:
			case T__8:
				enterOuterAlt(_localctx, 2);
				{
				setState(59);
				compound_stmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Simple_stmtContext extends ParserRuleContext {
		public Small_stmtContext small_stmt() {
			return getRuleContext(Small_stmtContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(Python3Parser.NEWLINE, 0); }
		public Simple_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simple_stmt; }
	}

	public final Simple_stmtContext simple_stmt() throws RecognitionException {
		Simple_stmtContext _localctx = new Simple_stmtContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_simple_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			small_stmt();
			setState(63);
			match(NEWLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Small_stmtContext extends ParserRuleContext {
		public Assignment_stmtContext assignment_stmt() {
			return getRuleContext(Assignment_stmtContext.class,0);
		}
		public Flow_stmtContext flow_stmt() {
			return getRuleContext(Flow_stmtContext.class,0);
		}
		public Print_stmtContext print_stmt() {
			return getRuleContext(Print_stmtContext.class,0);
		}
		public Small_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_small_stmt; }
	}

	public final Small_stmtContext small_stmt() throws RecognitionException {
		Small_stmtContext _localctx = new Small_stmtContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_small_stmt);
		try {
			setState(68);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(65);
				assignment_stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(66);
				flow_stmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(67);
				print_stmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assignment_stmtContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(Python3Parser.NAME, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Assignment_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment_stmt; }
	}

	public final Assignment_stmtContext assignment_stmt() throws RecognitionException {
		Assignment_stmtContext _localctx = new Assignment_stmtContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_assignment_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(NAME);
			setState(71);
			match(T__0);
			setState(72);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Flow_stmtContext extends ParserRuleContext {
		public Break_stmtContext break_stmt() {
			return getRuleContext(Break_stmtContext.class,0);
		}
		public Continue_stmtContext continue_stmt() {
			return getRuleContext(Continue_stmtContext.class,0);
		}
		public Flow_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_flow_stmt; }
	}

	public final Flow_stmtContext flow_stmt() throws RecognitionException {
		Flow_stmtContext _localctx = new Flow_stmtContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_flow_stmt);
		try {
			setState(76);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
				enterOuterAlt(_localctx, 1);
				{
				setState(74);
				break_stmt();
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 2);
				{
				setState(75);
				continue_stmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Break_stmtContext extends ParserRuleContext {
		public Break_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_break_stmt; }
	}

	public final Break_stmtContext break_stmt() throws RecognitionException {
		Break_stmtContext _localctx = new Break_stmtContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_break_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Continue_stmtContext extends ParserRuleContext {
		public Continue_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continue_stmt; }
	}

	public final Continue_stmtContext continue_stmt() throws RecognitionException {
		Continue_stmtContext _localctx = new Continue_stmtContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_continue_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Compound_stmtContext extends ParserRuleContext {
		public If_stmtContext if_stmt() {
			return getRuleContext(If_stmtContext.class,0);
		}
		public While_stmtContext while_stmt() {
			return getRuleContext(While_stmtContext.class,0);
		}
		public For_stmtContext for_stmt() {
			return getRuleContext(For_stmtContext.class,0);
		}
		public Compound_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compound_stmt; }
	}

	public final Compound_stmtContext compound_stmt() throws RecognitionException {
		Compound_stmtContext _localctx = new Compound_stmtContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_compound_stmt);
		try {
			setState(85);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				enterOuterAlt(_localctx, 1);
				{
				setState(82);
				if_stmt();
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 2);
				{
				setState(83);
				while_stmt();
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 3);
				{
				setState(84);
				for_stmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_stmtContext extends ParserRuleContext {
		public List<ConditionContext> condition() {
			return getRuleContexts(ConditionContext.class);
		}
		public ConditionContext condition(int i) {
			return getRuleContext(ConditionContext.class,i);
		}
		public List<SuiteContext> suite() {
			return getRuleContexts(SuiteContext.class);
		}
		public SuiteContext suite(int i) {
			return getRuleContext(SuiteContext.class,i);
		}
		public If_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stmt; }
	}

	public final If_stmtContext if_stmt() throws RecognitionException {
		If_stmtContext _localctx = new If_stmtContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_if_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			match(T__3);
			setState(88);
			condition();
			setState(89);
			match(T__4);
			setState(90);
			suite();
			setState(98);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(91);
				match(T__5);
				setState(92);
				condition();
				setState(93);
				match(T__4);
				setState(94);
				suite();
				}
				}
				setState(100);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(104);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__6) {
				{
				setState(101);
				match(T__6);
				setState(102);
				match(T__4);
				setState(103);
				suite();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class While_stmtContext extends ParserRuleContext {
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public While_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_stmt; }
	}

	public final While_stmtContext while_stmt() throws RecognitionException {
		While_stmtContext _localctx = new While_stmtContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(T__7);
			setState(107);
			condition();
			setState(108);
			match(T__4);
			setState(109);
			suite();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class For_stmtContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public RangeContext range() {
			return getRuleContext(RangeContext.class,0);
		}
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public ListContext list() {
			return getRuleContext(ListContext.class,0);
		}
		public For_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_stmt; }
	}

	public final For_stmtContext for_stmt() throws RecognitionException {
		For_stmtContext _localctx = new For_stmtContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_for_stmt);
		try {
			setState(125);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(111);
				match(T__8);
				setState(112);
				expr(0);
				setState(113);
				match(T__9);
				setState(114);
				range();
				setState(115);
				match(T__4);
				setState(116);
				suite();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(118);
				match(T__8);
				setState(119);
				expr(0);
				setState(120);
				match(T__9);
				setState(121);
				list();
				setState(122);
				match(T__4);
				setState(123);
				suite();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SuiteContext extends ParserRuleContext {
		public Simple_stmtContext simple_stmt() {
			return getRuleContext(Simple_stmtContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(Python3Parser.NEWLINE, 0); }
		public TerminalNode INDENT() { return getToken(Python3Parser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(Python3Parser.DEDENT, 0); }
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public SuiteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_suite; }
	}

	public final SuiteContext suite() throws RecognitionException {
		SuiteContext _localctx = new SuiteContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_suite);
		int _la;
		try {
			setState(137);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
			case T__2:
			case T__10:
			case NUMBER:
			case NAME:
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(127);
				simple_stmt();
				}
				break;
			case NEWLINE:
				enterOuterAlt(_localctx, 2);
				{
				setState(128);
				match(NEWLINE);
				setState(129);
				match(INDENT);
				setState(131); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(130);
					stmt();
					}
					}
					setState(133); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__7) | (1L << T__8) | (1L << T__10) | (1L << NUMBER) | (1L << NAME) | (1L << OPEN_PAREN))) != 0) );
				setState(135);
				match(DEDENT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConditionContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<ComprehensionContext> comprehension() {
			return getRuleContexts(ComprehensionContext.class);
		}
		public ComprehensionContext comprehension(int i) {
			return getRuleContext(ComprehensionContext.class,i);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			expr(0);
			setState(145);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18))) != 0)) {
				{
				{
				setState(140);
				comprehension();
				setState(141);
				expr(0);
				}
				}
				setState(147);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Print_stmtContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(Python3Parser.STRING, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Print_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_stmt; }
	}

	public final Print_stmtContext print_stmt() throws RecognitionException {
		Print_stmtContext _localctx = new Print_stmtContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_print_stmt);
		try {
			setState(151);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
				enterOuterAlt(_localctx, 1);
				{
				setState(148);
				match(T__10);
				setState(149);
				match(STRING);
				}
				break;
			case NUMBER:
			case NAME:
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(150);
				expr(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RangeContext extends ParserRuleContext {
		public TerminalNode OPEN_PAREN() { return getToken(Python3Parser.OPEN_PAREN, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(Python3Parser.CLOSE_PAREN, 0); }
		public RangeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_range; }
	}

	public final RangeContext range() throws RecognitionException {
		RangeContext _localctx = new RangeContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_range);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			match(T__11);
			setState(154);
			match(OPEN_PAREN);
			setState(155);
			expr(0);
			setState(156);
			match(T__12);
			setState(157);
			expr(0);
			setState(158);
			match(CLOSE_PAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ListContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list; }
	}

	public final ListContext list() throws RecognitionException {
		ListContext _localctx = new ListContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ComprehensionContext extends ParserRuleContext {
		public ComprehensionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comprehension; }
	}

	public final ComprehensionContext comprehension() throws RecognitionException {
		ComprehensionContext _localctx = new ComprehensionContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_comprehension);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(Python3Parser.NAME, 0); }
		public TerminalNode NUMBER() { return getToken(Python3Parser.NUMBER, 0); }
		public TerminalNode OPEN_PAREN() { return getToken(Python3Parser.OPEN_PAREN, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(Python3Parser.CLOSE_PAREN, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 38;
		enterRecursionRule(_localctx, 38, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(171);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NAME:
				{
				setState(165);
				match(NAME);
				}
				break;
			case NUMBER:
				{
				setState(166);
				match(NUMBER);
				}
				break;
			case OPEN_PAREN:
				{
				setState(167);
				match(OPEN_PAREN);
				setState(168);
				expr(0);
				setState(169);
				match(CLOSE_PAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(182);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr);
					setState(173);
					if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
					setState(176); 
					_errHandler.sync(this);
					_alt = 1;
					do {
						switch (_alt) {
						case 1:
							{
							{
							setState(174);
							_la = _input.LA(1);
							if ( !(_la==T__19 || _la==T__20) ) {
							_errHandler.recoverInline(this);
							}
							else {
								if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
								_errHandler.reportMatch(this);
								consume();
							}
							setState(175);
							expr(0);
							}
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						setState(178); 
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
					} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
					}
					} 
				}
				setState(184);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 19:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3(\u00bc\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\62\n\2"+
		"\3\3\3\3\7\3\66\n\3\f\3\16\39\13\3\3\3\3\3\3\4\3\4\5\4?\n\4\3\5\3\5\3"+
		"\5\3\6\3\6\3\6\5\6G\n\6\3\7\3\7\3\7\3\7\3\b\3\b\5\bO\n\b\3\t\3\t\3\n\3"+
		"\n\3\13\3\13\3\13\5\13X\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\fc"+
		"\n\f\f\f\16\ff\13\f\3\f\3\f\3\f\5\fk\n\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16"+
		"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u0080"+
		"\n\16\3\17\3\17\3\17\3\17\6\17\u0086\n\17\r\17\16\17\u0087\3\17\3\17\5"+
		"\17\u008c\n\17\3\20\3\20\3\20\3\20\7\20\u0092\n\20\f\20\16\20\u0095\13"+
		"\20\3\21\3\21\3\21\5\21\u009a\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22"+
		"\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00ae\n\25"+
		"\3\25\3\25\3\25\6\25\u00b3\n\25\r\25\16\25\u00b4\7\25\u00b7\n\25\f\25"+
		"\16\25\u00ba\13\25\3\25\2\3(\26\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36"+
		" \"$&(\2\4\3\2\20\25\3\2\26\27\2\u00bc\2\61\3\2\2\2\4\67\3\2\2\2\6>\3"+
		"\2\2\2\b@\3\2\2\2\nF\3\2\2\2\fH\3\2\2\2\16N\3\2\2\2\20P\3\2\2\2\22R\3"+
		"\2\2\2\24W\3\2\2\2\26Y\3\2\2\2\30l\3\2\2\2\32\177\3\2\2\2\34\u008b\3\2"+
		"\2\2\36\u008d\3\2\2\2 \u0099\3\2\2\2\"\u009b\3\2\2\2$\u00a2\3\2\2\2&\u00a4"+
		"\3\2\2\2(\u00ad\3\2\2\2*\62\7\33\2\2+,\5\b\5\2,-\7\33\2\2-\62\3\2\2\2"+
		"./\5\24\13\2/\60\7\33\2\2\60\62\3\2\2\2\61*\3\2\2\2\61+\3\2\2\2\61.\3"+
		"\2\2\2\62\3\3\2\2\2\63\66\7\33\2\2\64\66\5\6\4\2\65\63\3\2\2\2\65\64\3"+
		"\2\2\2\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28:\3\2\2\29\67\3\2\2\2:;\7"+
		"\2\2\3;\5\3\2\2\2<?\5\b\5\2=?\5\24\13\2><\3\2\2\2>=\3\2\2\2?\7\3\2\2\2"+
		"@A\5\n\6\2AB\7\33\2\2B\t\3\2\2\2CG\5\f\7\2DG\5\16\b\2EG\5 \21\2FC\3\2"+
		"\2\2FD\3\2\2\2FE\3\2\2\2G\13\3\2\2\2HI\7\34\2\2IJ\7\3\2\2JK\5(\25\2K\r"+
		"\3\2\2\2LO\5\20\t\2MO\5\22\n\2NL\3\2\2\2NM\3\2\2\2O\17\3\2\2\2PQ\7\4\2"+
		"\2Q\21\3\2\2\2RS\7\5\2\2S\23\3\2\2\2TX\5\26\f\2UX\5\30\r\2VX\5\32\16\2"+
		"WT\3\2\2\2WU\3\2\2\2WV\3\2\2\2X\25\3\2\2\2YZ\7\6\2\2Z[\5\36\20\2[\\\7"+
		"\7\2\2\\d\5\34\17\2]^\7\b\2\2^_\5\36\20\2_`\7\7\2\2`a\5\34\17\2ac\3\2"+
		"\2\2b]\3\2\2\2cf\3\2\2\2db\3\2\2\2de\3\2\2\2ej\3\2\2\2fd\3\2\2\2gh\7\t"+
		"\2\2hi\7\7\2\2ik\5\34\17\2jg\3\2\2\2jk\3\2\2\2k\27\3\2\2\2lm\7\n\2\2m"+
		"n\5\36\20\2no\7\7\2\2op\5\34\17\2p\31\3\2\2\2qr\7\13\2\2rs\5(\25\2st\7"+
		"\f\2\2tu\5\"\22\2uv\7\7\2\2vw\5\34\17\2w\u0080\3\2\2\2xy\7\13\2\2yz\5"+
		"(\25\2z{\7\f\2\2{|\5$\23\2|}\7\7\2\2}~\5\34\17\2~\u0080\3\2\2\2\177q\3"+
		"\2\2\2\177x\3\2\2\2\u0080\33\3\2\2\2\u0081\u008c\5\b\5\2\u0082\u0083\7"+
		"\33\2\2\u0083\u0085\7\'\2\2\u0084\u0086\5\6\4\2\u0085\u0084\3\2\2\2\u0086"+
		"\u0087\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\3\2"+
		"\2\2\u0089\u008a\7(\2\2\u008a\u008c\3\2\2\2\u008b\u0081\3\2\2\2\u008b"+
		"\u0082\3\2\2\2\u008c\35\3\2\2\2\u008d\u0093\5(\25\2\u008e\u008f\5&\24"+
		"\2\u008f\u0090\5(\25\2\u0090\u0092\3\2\2\2\u0091\u008e\3\2\2\2\u0092\u0095"+
		"\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\37\3\2\2\2\u0095"+
		"\u0093\3\2\2\2\u0096\u0097\7\r\2\2\u0097\u009a\7\30\2\2\u0098\u009a\5"+
		"(\25\2\u0099\u0096\3\2\2\2\u0099\u0098\3\2\2\2\u009a!\3\2\2\2\u009b\u009c"+
		"\7\16\2\2\u009c\u009d\7\37\2\2\u009d\u009e\5(\25\2\u009e\u009f\7\17\2"+
		"\2\u009f\u00a0\5(\25\2\u00a0\u00a1\7 \2\2\u00a1#\3\2\2\2\u00a2\u00a3\5"+
		"(\25\2\u00a3%\3\2\2\2\u00a4\u00a5\t\2\2\2\u00a5\'\3\2\2\2\u00a6\u00a7"+
		"\b\25\1\2\u00a7\u00ae\7\34\2\2\u00a8\u00ae\7\31\2\2\u00a9\u00aa\7\37\2"+
		"\2\u00aa\u00ab\5(\25\2\u00ab\u00ac\7 \2\2\u00ac\u00ae\3\2\2\2\u00ad\u00a6"+
		"\3\2\2\2\u00ad\u00a8\3\2\2\2\u00ad\u00a9\3\2\2\2\u00ae\u00b8\3\2\2\2\u00af"+
		"\u00b2\f\6\2\2\u00b0\u00b1\t\3\2\2\u00b1\u00b3\5(\25\2\u00b2\u00b0\3\2"+
		"\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5"+
		"\u00b7\3\2\2\2\u00b6\u00af\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2"+
		"\2\2\u00b8\u00b9\3\2\2\2\u00b9)\3\2\2\2\u00ba\u00b8\3\2\2\2\23\61\65\67"+
		">FNWdj\177\u0087\u008b\u0093\u0099\u00ad\u00b4\u00b8";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}