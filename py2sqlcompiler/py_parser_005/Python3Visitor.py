# Generated from grammar/Python3.g4 by ANTLR 4.9.2
from antlr4 import *
import grizzly

# Imports for grizzly code evaluation and execution
import sqlite3
import cx_Oracle
import psycopg2
from grizzly import sqlgenerator as SQLGenerator
from grizzly import relationaldbexecutor as RelationalExecutor

if __name__ is not None and "." in __name__:
    from .Python3Parser import Python3Parser
else:
    from Python3Parser import Python3Parser

# This class defines a complete generic visitor for a parse tree produced by Python3Parser.
#statements = []


class Python3Visitor(ParseTreeVisitor):
    @staticmethod
    def evaluate(to_eval):
        _var = ""
        _df = ""
        for line in to_eval:
            
            if "=" in line:
                exec(line)
                _var = line.split("=")[0].replace(" ", "")
            elif ".use" in line:
                exec(line)
            else:
                _df = eval(line)
            
        return _df, _var
        
    def __init__(self, templates):
        self.pre = []
        self.statements = []
        self.assignments = {}
        self.cursor = []
        self.to_eval = []
        self.templates = templates

    # Visit a parse tree produced by Python3Parser#single_input.
    def visitSingle_input(self, ctx: Python3Parser.Single_inputContext):
        self.statements.append("BEGIN")
        self.visitChildren(ctx)
        self.statements.append("END;")

    # Visit a parse tree produced by Python3Parser#file_input.
    def visitFile_input(self, ctx: Python3Parser.File_inputContext):
        self.statements.append("BEGIN")
        self.visitChildren(ctx)
        self.statements.append("END;")

    # Visit a parse tree produced by Python3Parser#stmt.
    def visitStmt(self, ctx: Python3Parser.StmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#simple_stmt.
    def visitSimple_stmt(self, ctx: Python3Parser.Simple_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#small_stmt.
    def visitSmall_stmt(self, ctx: Python3Parser.Small_stmtContext):
        return self.visitChildren(ctx)

     # Visit a parse tree produced by Python3Parser#grizzly_stmt.
    def visitGrizzly_stmt(self, ctx:Python3Parser.Grizzly_stmtContext):
        if "=" in ctx.getText() or ".use" in ctx.getText():
            self.to_eval.append(ctx.getText())
        else:
            template = self.templates['cursor']
            self.to_eval.append(ctx.getText())
            _qry, _var = Python3Visitor.evaluate(self.to_eval)
            self.to_eval = []
            if type(_qry) == grizzly.expression.ColRef:
                _qry = _qry.generateQuery()

            self.cursor.append(template.replace('$$var$$', _var).replace('$$qry$$', _qry))
                    
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3Parser#assignment_stmt.
    def visitAssignment_stmt(self, ctx: Python3Parser.Assignment_stmtContext):
        assignment = self.visitChildren(ctx)
        var = str(ctx.NAME())

        # If assignment includes type declaration (i: int = 2)
        if ctx.typ():
            var_type = self.templates[ctx.typ().getText()]
        # Else check for type manually
        else:
            # If the expression is a type
            if ctx.expr().STRING():
                var_type = self.templates['str']
            # If expression is a number check whether its a float or not
            elif ctx.expr().NUMBER():
                if '.' in assignment:
                    var_type = self.templates['float']
                else:
                    var_type = self.templates['int']
            else:
                var_type = '<UNDEFINED>'

        # Variables need to be declared before the BEGIN-Block so collect all variables and types once
        if var not in (item for temp_list in self.assignments for item in temp_list[0]):
            self.assignments[var] = var_type
        
        # Check if there is an actual assignment to display (excludes i: int declarations)
        if assignment:
            self.statements.append(f"{var} := {assignment};")

    # Visit a parse tree produced by Python3Parser#flow_stmt.
    def visitFlow_stmt(self, ctx: Python3Parser.Flow_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#break_stmt.
    def visitBreak_stmt(self, ctx: Python3Parser.Break_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#continue_stmt.
    def visitContinue_stmt(self, ctx: Python3Parser.Continue_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#return_stmt.
    def visitReturn_stmt(self, ctx: Python3Parser.Return_stmtContext):
        #returns = ctx.expr().getText().replace('"',"'")
        returns = self.visitChildren(ctx)
        self.statements.append(f"RETURN {returns};")
        return f"RETURN {returns};"
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#compound_stmt.
    def visitCompound_stmt(self, ctx: Python3Parser.Compound_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#if_stmt.
    def visitIf_stmt(self, ctx: Python3Parser.If_stmtContext):
        test_counter = 0
        for i, _ in enumerate(ctx.suite()):
            if i == 0:
                self.statements.append(f"IF {ctx.test()[test_counter].getText().replace('==', '=')} THEN")
                test_counter += 1
            elif i == len(ctx.suite())-1 and "else" in ctx.getText():
                self.statements.append(f"ELSE")
            elif "elif" in ctx.getText():
                self.statements.append(f"ELSIF {ctx.test()[test_counter].getText().replace('==', '=')} THEN")
                test_counter += 1

            self.visitChildren(ctx.suite()[i])

        self.statements.append("END IF;")

    # Visit a parse tree produced by Python3Parser#while_stmt.
    def visitWhile_stmt(self, ctx: Python3Parser.While_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#for_stmt.
    def visitFor_stmt(self, ctx: Python3Parser.For_stmtContext):
        if ctx.rang():
            self.statements.append("FOR " + str(ctx.expr()[0].NAME()) + " IN " + str(
                ctx.rang().expr()[0].getText()) + ".." + str(ctx.rang().expr()[1].getText()))
            self.statements.append("LOOP")
            self.visitSuite(ctx)
            # TODO Fix visit children -> just visit children with indent
            self.statements.append("END LOOP;")
        else:
            if ctx.expr()[1].GRZLYNAME():
                #self.statements.append(f'OPEN {str(ctx.expr()[1].getText())};')
                self.statements.append("FOR " + str(ctx.expr()[0].NAME()) + " IN " + str(ctx.expr()[1].getText()))
                self.statements.append("LOOP")
                self.visitSuite(ctx)
                self.statements.append("END LOOP;")
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#suite.
    def visitSuite(self, ctx: Python3Parser.SuiteContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#test.
    def visitTest(self, ctx:Python3Parser.TestContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#print_stmt.
    def visitPrint_stmt(self, ctx: Python3Parser.Print_stmtContext):
        if self.templates.profile == 'postgresql':
            if ctx.expr().STRING():
                template = self.templates['print_str']
            # TODO cases for row.attr references
            else:
                template = self.templates['print_var']
        else:
            template = self.templates['print']
        
        if '/' in template:
            self.pre.append(template.split('/')[0])
            self.statements.append(template.split('/')[1].replace('$$code$$', ctx.expr().getText()))
        else:
            self.statements.append(template.replace('$$code$$', ctx.expr().getText()))
        
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#range.
    def visitRange(self, ctx: Python3Parser.RangContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#comprehension.
    def visitComp_op(self, ctx: Python3Parser.Comp_opContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#expr.
    def visitExpr(self, ctx: Python3Parser.ExprContext):
        if "+" in ctx.getText():
            l = ctx.expr()[0].getText().replace('"', "'")
            r = ctx.expr()[1].getText().replace('"', "'")

            # Check if a variable is in equasion and if one of these variables is a string (lookup at assignment dict)
            if ctx.expr()[0].NAME():
                if self.assignments.get(str(ctx.expr()[0].NAME())) == self.templates['str']:
                    return (f"CONCAT({l}, {r})") 
            if ctx.expr()[1].NAME():
                if self.assignments.get(str(ctx.expr()[1].NAME())) == self.templates['str']:
                    return (f"CONCAT({l}, {r})")
            
            # Check if one expressing is a clear string
            if ctx.expr()[0].STRING() or ctx.expr()[1].STRING():
                return (f"CONCAT({l}, {r})")

        return str(ctx.getText().replace('"', "'").replace('==', '='))

    # Visit a parse tree produced by Python3Parser#typ.
    def visitTyp(self, ctx:Python3Parser.TypContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by Python3Parser#db_reference.
    def visitDb_reference(self, ctx:Python3Parser.Db_referenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3Parser#all_chars.
    def visitAll_chars(self, ctx:Python3Parser.All_charsContext):
        return self.visitChildren(ctx)


del Python3Parser
