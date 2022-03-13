# Generated from grammar/Python3.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Python3Parser import Python3Parser
else:
    from Python3Parser import Python3Parser

# This class defines a complete listener for a parse tree produced by Python3Parser.
class Python3Listener(ParseTreeListener):

    # Enter a parse tree produced by Python3Parser#single_input.
    def enterSingle_input(self, ctx:Python3Parser.Single_inputContext):
        pass

    # Exit a parse tree produced by Python3Parser#single_input.
    def exitSingle_input(self, ctx:Python3Parser.Single_inputContext):
        pass


    # Enter a parse tree produced by Python3Parser#file_input.
    def enterFile_input(self, ctx:Python3Parser.File_inputContext):
        pass

    # Exit a parse tree produced by Python3Parser#file_input.
    def exitFile_input(self, ctx:Python3Parser.File_inputContext):
        pass


    # Enter a parse tree produced by Python3Parser#stmt.
    def enterStmt(self, ctx:Python3Parser.StmtContext):
        pass

    # Exit a parse tree produced by Python3Parser#stmt.
    def exitStmt(self, ctx:Python3Parser.StmtContext):
        pass


    # Enter a parse tree produced by Python3Parser#simple_stmt.
    def enterSimple_stmt(self, ctx:Python3Parser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by Python3Parser#simple_stmt.
    def exitSimple_stmt(self, ctx:Python3Parser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by Python3Parser#small_stmt.
    def enterSmall_stmt(self, ctx:Python3Parser.Small_stmtContext):
        pass

    # Exit a parse tree produced by Python3Parser#small_stmt.
    def exitSmall_stmt(self, ctx:Python3Parser.Small_stmtContext):
        pass

    
    # Enter a parse tree produced by Python3Parser#assignment_stmt.
    def enterAssignment_stmt(self, ctx:Python3Parser.Assignment_stmtContext):
        if ctx.expr().NUMBER():
            print(str(ctx.NAME()) + " := " + str(ctx.expr().NUMBER()) + ";")
        else:
           print(str(ctx.NAME()) + " := " + str(ctx.expr().NAME()) + ";") 
        pass

    # Exit a parse tree produced by Python3Parser#assignment_stmt.
    def exitAssignment_stmt(self, ctx:Python3Parser.Assignment_stmtContext):
        pass


    # Enter a parse tree produced by Python3Parser#flow_stmt.
    def enterFlow_stmt(self, ctx:Python3Parser.Flow_stmtContext):
        pass

    # Exit a parse tree produced by Python3Parser#flow_stmt.
    def exitFlow_stmt(self, ctx:Python3Parser.Flow_stmtContext):
        pass


    # Enter a parse tree produced by Python3Parser#break_stmt.
    def enterBreak_stmt(self, ctx:Python3Parser.Break_stmtContext):
        pass

    # Exit a parse tree produced by Python3Parser#break_stmt.
    def exitBreak_stmt(self, ctx:Python3Parser.Break_stmtContext):
        pass


    # Enter a parse tree produced by Python3Parser#continue_stmt.
    def enterContinue_stmt(self, ctx:Python3Parser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by Python3Parser#continue_stmt.
    def exitContinue_stmt(self, ctx:Python3Parser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by Python3Parser#return_stmt.
    def enterReturn_stmt(self, ctx:Python3Parser.Return_stmtContext):
        pass

    # Exit a parse tree produced by Python3Parser#return_stmt.
    def exitReturn_stmt(self, ctx:Python3Parser.Return_stmtContext):
        pass


    # Enter a parse tree produced by Python3Parser#compound_stmt.
    def enterCompound_stmt(self, ctx:Python3Parser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by Python3Parser#compound_stmt.
    def exitCompound_stmt(self, ctx:Python3Parser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by Python3Parser#if_stmt.
    def enterIf_stmt(self, ctx:Python3Parser.If_stmtContext):
        pass

    # Exit a parse tree produced by Python3Parser#if_stmt.
    def exitIf_stmt(self, ctx:Python3Parser.If_stmtContext):
        pass


    # Enter a parse tree produced by Python3Parser#while_stmt.
    def enterWhile_stmt(self, ctx:Python3Parser.While_stmtContext):
        pass

    # Exit a parse tree produced by Python3Parser#while_stmt.
    def exitWhile_stmt(self, ctx:Python3Parser.While_stmtContext):
        pass


    # Enter a parse tree produced by Python3Parser#for_stmt.
    def enterFor_stmt(self, ctx:Python3Parser.For_stmtContext):
        if ctx.range():
            print("FOR " + str(ctx.expr().NAME()) + " IN " + str(ctx.range().expr()[0].NUMBER()) + ".." + str(ctx.range().expr()[1].NUMBER()))
            print('LOOP')
            ctx.suite()
        pass

    # Exit a parse tree produced by Python3Parser#for_stmt.
    def exitFor_stmt(self, ctx:Python3Parser.For_stmtContext):
        print("END LOOP;")
        pass



    # Enter a parse tree produced by Python3Parser#suite.
    def enterSuite(self, ctx:Python3Parser.SuiteContext):
        pass

    # Exit a parse tree produced by Python3Parser#suite.
    def exitSuite(self, ctx:Python3Parser.SuiteContext):
        pass


    # Enter a parse tree produced by Python3Parser#condition.
    def enterCondition(self, ctx:Python3Parser.ConditionContext):
        pass

    # Exit a parse tree produced by Python3Parser#condition.
    def exitCondition(self, ctx:Python3Parser.ConditionContext):
        pass


    # Enter a parse tree produced by Python3Parser#print_stmt.
    def enterPrint_stmt(self, ctx:Python3Parser.Print_stmtContext):
        pass

    # Exit a parse tree produced by Python3Parser#print_stmt.
    def exitPrint_stmt(self, ctx:Python3Parser.Print_stmtContext):
        pass


    # Enter a parse tree produced by Python3Parser#range.
    def enterRange(self, ctx:Python3Parser.RangeContext):
        pass

    # Exit a parse tree produced by Python3Parser#range.
    def exitRange(self, ctx:Python3Parser.RangeContext):
        pass


    # Enter a parse tree produced by Python3Parser#list.
    def enterList(self, ctx:Python3Parser.ListContext):
        pass

    # Exit a parse tree produced by Python3Parser#list.
    def exitList(self, ctx:Python3Parser.ListContext):
        pass


    # Enter a parse tree produced by Python3Parser#comprehension.
    def enterComprehension(self, ctx:Python3Parser.ComprehensionContext):
        pass

    # Exit a parse tree produced by Python3Parser#comprehension.
    def exitComprehension(self, ctx:Python3Parser.ComprehensionContext):
        pass


    # Enter a parse tree produced by Python3Parser#expr.
    def enterExpr(self, ctx:Python3Parser.ExprContext):
        pass

    # Exit a parse tree produced by Python3Parser#expr.
    def exitExpr(self, ctx:Python3Parser.ExprContext):
        pass



del Python3Parser