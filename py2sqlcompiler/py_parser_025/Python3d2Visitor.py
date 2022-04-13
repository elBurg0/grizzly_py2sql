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
    from .Python3d2Parser import Python3d2Parser
else:
    from Python3d2Parser import Python3d2Parser

# This class defines a complete generic visitor for a parse tree produced by Python3Parser.
#statements = []


class Python3d2Visitor(ParseTreeVisitor):
    @staticmethod
    def evaluate(to_eval):
        _var = ""
        _df = ""

        for i, line in enumerate(to_eval):
            if "=" in line:
                exec(line)
                _var = line.split("=")[0].replace(" ", "")
                if i == len(to_eval)-1:
                    _df = eval(_var + '.generateQuery()')
                
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
    def visitSingle_input(self, ctx: Python3d2Parser.Single_inputContext):
        self.statements.append("BEGIN")
        self.visitChildren(ctx)
        self.statements.append("END;")

    # Visit a parse tree produced by Python3Parser#file_input.
    def visitFile_input(self, ctx: Python3d2Parser.File_inputContext):
        self.statements.append("BEGIN")
        self.visitChildren(ctx)
        self.statements.append("END;")

    # Visit a parse tree produced by Python3d2Parser#stmt.
    def visitStmt(self, ctx: Python3d2Parser.StmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d2Parser#simple_stmt.
    def visitSimple_stmt(self, ctx: Python3d2Parser.Simple_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d2Parser#small_stmt.
    def visitSmall_stmt(self, ctx: Python3d2Parser.Small_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d2Parser#assignment_stmt.
    def visitAssignment_stmt(self, ctx: Python3d2Parser.Assignment_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d2Parser#initialization.
    def visitInitialization(self, ctx:Python3d2Parser.InitializationContext):
        self.assignments[ctx.NAME().getText()] = ctx.typ().getText()
        self.statements.append(f"{ctx.NAME().getText()} := {self.visitChildren(ctx)};")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3d2Parser#declaration.
    def visitDeclaration(self, ctx:Python3d2Parser.DeclarationContext):
        self.assignments[ctx.NAME().getText()] = ctx.typ().getText()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3d2Parser#nontype_initialization.
    def visitNontype_initialization(self, ctx:Python3d2Parser.Nontype_initializationContext):
        if ctx.GRZLYNAME():
            self.to_eval.append(ctx.getText())
        else:
            assignment = self.visitChildren(ctx)
            var = ctx.NAME().getText()

            if var not in (item for temp_list in self.assignments for item in temp_list[0]):
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
                self.assignments[var] = var_type

            self.statements.append(f"{var} := {assignment};")

        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d2Parser#flow_stmt.
    def visitFlow_stmt(self, ctx: Python3d2Parser.Flow_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d2Parser#break_stmt.
    def visitBreak_stmt(self, ctx: Python3d2Parser.Break_stmtContext):
        self.statements.append('EXIT;')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d2Parser#continue_stmt.
    def visitContinue_stmt(self, ctx: Python3d2Parser.Continue_stmtContext):
        self.statements.append('CONTINUE;')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d2Parser#return_stmt.
    def visitReturn_stmt(self, ctx: Python3d2Parser.Return_stmtContext):
        #returns = ctx.expr().getText().replace('"',"'")
        returns = self.visitChildren(ctx)
        self.statements.append(f"RETURN {returns};")
        return f"RETURN {returns};"
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d2Parser#compound_stmt.
    def visitCompound_stmt(self, ctx: Python3d2Parser.Compound_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d2Parser#if_stmt.
    def visitIf_stmt(self, ctx: Python3d2Parser.If_stmtContext):
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

    # Visit a parse tree produced by Python3d2Parser#while_stmt.
    def visitWhile_stmt(self, ctx: Python3d2Parser.While_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d2Parser#for_stmt.
    def visitFor_stmt(self, ctx: Python3d2Parser.For_stmtContext):
        if ctx.rang():
            self.statements.append("FOR " + str(ctx.expr()[0].NAME()) + " IN " + str(
                ctx.rang().expr()[0].getText()) + ".." + str(ctx.rang().expr()[1].getText()))
            self.statements.append("LOOP")
            self.visitSuite(ctx)
            # TODO Fix visit children -> just visit children with indent
            self.statements.append("END LOOP;")
        else:
            if ctx.GRZLYNAME:
                template = self.templates['cursor']
                _qry, _var = Python3d2Visitor.evaluate(self.to_eval)
                self.to_eval = []
                if type(_qry) == grizzly.expression.ColRef:
                    _qry = _qry.generateQuery()
                
                self.cursor.append(template.replace('$$var$$', _var).replace('$$qry$$', _qry))

                #self.statements.append(f'OPEN {str(ctx.expr()[1].getText())};')
                self.statements.append("FOR " + str(ctx.expr()[0].getText()) + " IN " + str(ctx.GRZLYNAME()))
                self.statements.append("LOOP")
                self.visitSuite(ctx)
                self.statements.append("END LOOP;")
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d2Parser#suite.
    def visitSuite(self, ctx: Python3d2Parser.SuiteContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d2Parser#test.
    def visitTest(self, ctx:Python3d2Parser.TestContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d2Parser#print_stmt.
    def visitPrint_stmt(self, ctx: Python3d2Parser.Print_stmtContext):
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

    # Visit a parse tree produced by Python3d2Parser#range.
    def visitRange(self, ctx: Python3d2Parser.RangContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d2Parser#comprehension.
    def visitComp_op(self, ctx: Python3d2Parser.Comp_opContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d2Parser#expr.
    def visitExpr(self, ctx: Python3d2Parser.ExprContext):
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

    # Visit a parse tree produced by Python3d2Parser#typ.
    def visitTyp(self, ctx:Python3d2Parser.TypContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by Python3d2Parser#db_reference.
    def visitDb_reference(self, ctx:Python3d2Parser.Db_referenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d2Parser#all_chars.
    def visitAll_chars(self, ctx:Python3d2Parser.All_charsContext):
        return self.visitChildren(ctx)


del Python3d2Parser
