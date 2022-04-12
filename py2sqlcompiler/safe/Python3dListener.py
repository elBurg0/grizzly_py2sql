# Generated from grammar/Python3d.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Python3dParser import Python3dParser
else:
    from Python3dParser import Python3dParser

# This class defines a complete listener for a parse tree produced by Python3dParser.
class Python3dListener(ParseTreeListener):

    # Enter a parse tree produced by Python3dParser#single_input.
    def enterSingle_input(self, ctx:Python3dParser.Single_inputContext):
        pass

    # Exit a parse tree produced by Python3dParser#single_input.
    def exitSingle_input(self, ctx:Python3dParser.Single_inputContext):
        pass


    # Enter a parse tree produced by Python3dParser#file_input.
    def enterFile_input(self, ctx:Python3dParser.File_inputContext):
        pass

    # Exit a parse tree produced by Python3dParser#file_input.
    def exitFile_input(self, ctx:Python3dParser.File_inputContext):
        pass


    # Enter a parse tree produced by Python3dParser#stmt.
    def enterStmt(self, ctx:Python3dParser.StmtContext):
        pass

    # Exit a parse tree produced by Python3dParser#stmt.
    def exitStmt(self, ctx:Python3dParser.StmtContext):
        pass


    # Enter a parse tree produced by Python3dParser#simple_stmt.
    def enterSimple_stmt(self, ctx:Python3dParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by Python3dParser#simple_stmt.
    def exitSimple_stmt(self, ctx:Python3dParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by Python3dParser#small_stmt.
    def enterSmall_stmt(self, ctx:Python3dParser.Small_stmtContext):
        pass

    # Exit a parse tree produced by Python3dParser#small_stmt.
    def exitSmall_stmt(self, ctx:Python3dParser.Small_stmtContext):
        pass


    # Enter a parse tree produced by Python3dParser#grizzly_stmt.
    def enterGrizzly_stmt(self, ctx:Python3dParser.Grizzly_stmtContext):
        pass

    # Exit a parse tree produced by Python3dParser#grizzly_stmt.
    def exitGrizzly_stmt(self, ctx:Python3dParser.Grizzly_stmtContext):
        pass


    # Enter a parse tree produced by Python3dParser#assignment_stmt.
    def enterAssignment_stmt(self, ctx:Python3dParser.Assignment_stmtContext):
        pass

    # Exit a parse tree produced by Python3dParser#assignment_stmt.
    def exitAssignment_stmt(self, ctx:Python3dParser.Assignment_stmtContext):
        pass


    # Enter a parse tree produced by Python3dParser#grizzly_assignment.
    def enterGrizzly_assignment(self, ctx:Python3dParser.Grizzly_assignmentContext):
        pass

    # Exit a parse tree produced by Python3dParser#grizzly_assignment.
    def exitGrizzly_assignment(self, ctx:Python3dParser.Grizzly_assignmentContext):
        pass


    # Enter a parse tree produced by Python3dParser#initialization.
    def enterInitialization(self, ctx:Python3dParser.InitializationContext):
        pass

    # Exit a parse tree produced by Python3dParser#initialization.
    def exitInitialization(self, ctx:Python3dParser.InitializationContext):
        pass


    # Enter a parse tree produced by Python3dParser#declaration.
    def enterDeclaration(self, ctx:Python3dParser.DeclarationContext):
        pass

    # Exit a parse tree produced by Python3dParser#declaration.
    def exitDeclaration(self, ctx:Python3dParser.DeclarationContext):
        pass


    # Enter a parse tree produced by Python3dParser#nontype_initialization.
    def enterNontype_initialization(self, ctx:Python3dParser.Nontype_initializationContext):
        pass

    # Exit a parse tree produced by Python3dParser#nontype_initialization.
    def exitNontype_initialization(self, ctx:Python3dParser.Nontype_initializationContext):
        pass


    # Enter a parse tree produced by Python3dParser#flow_stmt.
    def enterFlow_stmt(self, ctx:Python3dParser.Flow_stmtContext):
        pass

    # Exit a parse tree produced by Python3dParser#flow_stmt.
    def exitFlow_stmt(self, ctx:Python3dParser.Flow_stmtContext):
        pass


    # Enter a parse tree produced by Python3dParser#break_stmt.
    def enterBreak_stmt(self, ctx:Python3dParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by Python3dParser#break_stmt.
    def exitBreak_stmt(self, ctx:Python3dParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by Python3dParser#continue_stmt.
    def enterContinue_stmt(self, ctx:Python3dParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by Python3dParser#continue_stmt.
    def exitContinue_stmt(self, ctx:Python3dParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by Python3dParser#return_stmt.
    def enterReturn_stmt(self, ctx:Python3dParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by Python3dParser#return_stmt.
    def exitReturn_stmt(self, ctx:Python3dParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by Python3dParser#compound_stmt.
    def enterCompound_stmt(self, ctx:Python3dParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by Python3dParser#compound_stmt.
    def exitCompound_stmt(self, ctx:Python3dParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by Python3dParser#if_stmt.
    def enterIf_stmt(self, ctx:Python3dParser.If_stmtContext):
        pass

    # Exit a parse tree produced by Python3dParser#if_stmt.
    def exitIf_stmt(self, ctx:Python3dParser.If_stmtContext):
        pass


    # Enter a parse tree produced by Python3dParser#while_stmt.
    def enterWhile_stmt(self, ctx:Python3dParser.While_stmtContext):
        pass

    # Exit a parse tree produced by Python3dParser#while_stmt.
    def exitWhile_stmt(self, ctx:Python3dParser.While_stmtContext):
        pass


    # Enter a parse tree produced by Python3dParser#for_stmt.
    def enterFor_stmt(self, ctx:Python3dParser.For_stmtContext):
        pass

    # Exit a parse tree produced by Python3dParser#for_stmt.
    def exitFor_stmt(self, ctx:Python3dParser.For_stmtContext):
        pass


    # Enter a parse tree produced by Python3dParser#suite.
    def enterSuite(self, ctx:Python3dParser.SuiteContext):
        pass

    # Exit a parse tree produced by Python3dParser#suite.
    def exitSuite(self, ctx:Python3dParser.SuiteContext):
        pass


    # Enter a parse tree produced by Python3dParser#rang.
    def enterRang(self, ctx:Python3dParser.RangContext):
        pass

    # Exit a parse tree produced by Python3dParser#rang.
    def exitRang(self, ctx:Python3dParser.RangContext):
        pass


    # Enter a parse tree produced by Python3dParser#test.
    def enterTest(self, ctx:Python3dParser.TestContext):
        pass

    # Exit a parse tree produced by Python3dParser#test.
    def exitTest(self, ctx:Python3dParser.TestContext):
        pass


    # Enter a parse tree produced by Python3dParser#print_stmt.
    def enterPrint_stmt(self, ctx:Python3dParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by Python3dParser#print_stmt.
    def exitPrint_stmt(self, ctx:Python3dParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by Python3dParser#comp_op.
    def enterComp_op(self, ctx:Python3dParser.Comp_opContext):
        pass

    # Exit a parse tree produced by Python3dParser#comp_op.
    def exitComp_op(self, ctx:Python3dParser.Comp_opContext):
        pass


    # Enter a parse tree produced by Python3dParser#expr.
    def enterExpr(self, ctx:Python3dParser.ExprContext):
        pass

    # Exit a parse tree produced by Python3dParser#expr.
    def exitExpr(self, ctx:Python3dParser.ExprContext):
        pass


    # Enter a parse tree produced by Python3dParser#typ.
    def enterTyp(self, ctx:Python3dParser.TypContext):
        pass

    # Exit a parse tree produced by Python3dParser#typ.
    def exitTyp(self, ctx:Python3dParser.TypContext):
        pass


    # Enter a parse tree produced by Python3dParser#all_chars.
    def enterAll_chars(self, ctx:Python3dParser.All_charsContext):
        pass

    # Exit a parse tree produced by Python3dParser#all_chars.
    def exitAll_chars(self, ctx:Python3dParser.All_charsContext):
        pass


    # Enter a parse tree produced by Python3dParser#db_reference.
    def enterDb_reference(self, ctx:Python3dParser.Db_referenceContext):
        pass

    # Exit a parse tree produced by Python3dParser#db_reference.
    def exitDb_reference(self, ctx:Python3dParser.Db_referenceContext):
        pass



del Python3dParser