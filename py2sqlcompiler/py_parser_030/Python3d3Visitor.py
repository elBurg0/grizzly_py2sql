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
    from .Python3d3Parser import Python3d3Parser
else:
    from Python3d3Parser import Python3d3Parser

# This class defines a complete generic visitor for a parse tree produced by Python3Parser.
#statements = []


class Python3d3Visitor(ParseTreeVisitor):
    @staticmethod
    def evaluate(to_eval):
        _var = ""
        _qry = ""

        for i, line in enumerate(to_eval):
            if "=" in line:
                exec(line)
                _var = line.split("=")[0].replace(" ", "")
                if i == len(to_eval)-1:
                    _qry = eval(_var + '.generateQuery()')
            elif ".use" in line:
                exec(line)
            else:
                _qry = eval(line)
        return _qry, _var
        
    def __init__(self, templates):
        self.pre = []
        self.statements = []
        self.assignments = {}
        self.cursor = []
        self.exceptions = []
        self.to_eval = []
        self.templates = templates

    # Visit a parse tree produced by Python3Parser#single_input.
    def visitSingle_input(self, ctx: Python3d3Parser.Single_inputContext):
        self.statements.append("BEGIN")
        self.visitChildren(ctx)
        self.statements.append("END;")

    # Visit a parse tree produced by Python3Parser#file_input.
    def visitFile_input(self, ctx: Python3d3Parser.File_inputContext):
        self.statements.append("BEGIN")
        self.visitChildren(ctx)
        self.statements.append("END;")

    # Visit a parse tree produced by Python3d3Parser#stmt.
    def visitStmt(self, ctx: Python3d3Parser.StmtContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by Python3d3Parser#exception_stmt.
    def visitException_stmt(self, ctx:Python3d3Parser.Exception_stmtContext):
        # TODO Handle else, finally
        self.statements.append('BEGIN')
        self.visitChildren(ctx.suite()[0])
        self.statements.append('EXCEPTION')

        # Iterate through each exception handling
        for i, exception_stmt in enumerate(ctx.except_stmt()):
            if exception_stmt.expr():
                if type(exception_stmt.expr()) == list:
                    exception_text = exception_stmt.expr()[0].getText()
                else:
                    exception_text = exception_stmt.expr().getText()

                # Try to map error type
                try:
                    exception_text = self.templates[exception_text]
                except ValueError:
                    pass
                
                # TODO no use of exceptions (as e) in sql
                self.statements.append('WHEN ' + exception_text + ' THEN')
            else:
                self.statements.append('WHEN OTHERS THEN')
            self.visitChildren(ctx.suite()[i+1])
        self.statements.append('END;')

    # Visit a parse tree produced by Python3d3Parser#simple_stmt.
    def visitSimple_stmt(self, ctx: Python3d3Parser.Simple_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d3Parser#small_stmt.
    def visitSmall_stmt(self, ctx: Python3d3Parser.Small_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d3Parser#assignment_stmt.
    def visitAssignment_stmt(self, ctx: Python3d3Parser.Assignment_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d3Parser#initialization.
    def visitInitialization(self, ctx:Python3d3Parser.InitializationContext):
        # i: int = 0
        # TODO Errorhandling
        self.assignments[ctx.NAME().getText()] = self.templates[ctx.typ().getText()]
        self.statements.append(f"{ctx.NAME().getText()} := {self.visitChildren(ctx)};")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3d3Parser#declaration.
    def visitDeclaration(self, ctx:Python3d3Parser.DeclarationContext):
        # i: int
        # TODO Errorhandling
        self.assignments[ctx.NAME().getText()] = self.templates[ctx.typ().getText()]
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3d3Parser#nontype_initialization.
    def visitNontype_initialization(self, ctx:Python3d3Parser.Nontype_initializationContext):
        # i = 3 / g_df1 = grizzly.read('table')
        if ctx.GRZLYNAME():
            self.to_eval.append(ctx.getText())
            return self.visitChildren(ctx)

        # If assignment isn't an grizzly statement
        assignment = self.visitChildren(ctx)
        var = ctx.NAME().getText()

        # Check if variable name is not already in assignments (of types)
        if var not in (item for temp_list in self.assignments for item in temp_list[0]):
            # If the expression is a string
            if ctx.expr().STRING():
                var_type = self.templates['str']
            # If expression is a number check whether its a float or not
            elif ctx.expr().NUMBER():
                var_type = self.templates['int']
            elif ctx.expr().FLOAT():
                var_type = self.templates['float']
            else:
                raise NotImplementedError(f'Type mapping for expression "{assignment}" not implemented')
                var_type = '<UNDEFINED>'
            self.assignments[var] = var_type
        
        self.statements.append(f"{var} := {assignment};")

    # Visit a parse tree produced by Python3d3Parser#flow_stmt.
    def visitFlow_stmt(self, ctx: Python3d3Parser.Flow_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d3Parser#break_stmt.
    def visitBreak_stmt(self, ctx: Python3d3Parser.Break_stmtContext):
        self.statements.append('EXIT;')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d3Parser#continue_stmt.
    def visitContinue_stmt(self, ctx: Python3d3Parser.Continue_stmtContext):
        self.statements.append('CONTINUE;')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d3Parser#return_stmt.
    def visitReturn_stmt(self, ctx: Python3d3Parser.Return_stmtContext):
        #returns = ctx.expr().getText().replace('"',"'")
        returns = self.visitChildren(ctx)
        self.statements.append(f"RETURN {returns};")
        return f"RETURN {returns};"
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d3Parser#raise_stmt.
    def visitRaise_stmt(self, ctx:Python3d3Parser.Raise_stmtContext):
        if self.templates.profile == 'oracle':
            self.exceptions.append(f'{ctx.NAME()} EXCEPTION;')
            self.statements.append(f'RAISE {ctx.NAME()};')

        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by Python3d3Parser#try_stmt.
    def visitTry_stmt(self, ctx:Python3d3Parser.Try_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Python3d3Parser#except_stmt.
    def visitExcept_stmt(self, ctx:Python3d3Parser.Except_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d3Parser#compound_stmt.
    def visitCompound_stmt(self, ctx: Python3d3Parser.Compound_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d3Parser#if_stmt.
    def visitIf_stmt(self, ctx: Python3d3Parser.If_stmtContext):
        test_counter = 0
        # TODO simplify
        # Iterate through all tests and suites
        for i, suite in enumerate(ctx.suite()):
            if i == 0:
                test = ctx.test()[test_counter].getText().replace('==', '=')
                self.statements.append(f"IF {test} THEN")
                test_counter += 1
            elif i == len(ctx.suite())-1 and "else" in ctx.getText():
                self.statements.append(f"ELSE")
            elif "elif" in ctx.getText():
                test = ctx.test()[test_counter].getText().replace('==', '=')
                self.statements.append(f"ELSIF {test} THEN")
                test_counter += 1
            self.visitChildren(suite)
        
        self.statements.append("END IF;")

    # Visit a parse tree produced by Python3d3Parser#while_stmt.
    def visitWhile_stmt(self, ctx: Python3d3Parser.While_stmtContext):
        self.statements.append(f'WHILE {ctx.test().getText()}')
        self.statements.append('LOOP')
        self.visitChildren(ctx.suite())
        self.statements.append('END LOOP;')

    # Visit a parse tree produced by Python3d3Parser#for_stmt.
    def visitFor_stmt(self, ctx: Python3d3Parser.For_stmtContext):
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
                _qry, _var = Python3d3Visitor.evaluate(self.to_eval)
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

    # Visit a parse tree produced by Python3d3Parser#suite.
    def visitSuite(self, ctx: Python3d3Parser.SuiteContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d3Parser#test.
    def visitTest(self, ctx:Python3d3Parser.TestContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d3Parser#print_stmt.
    def visitPrint_stmt(self, ctx: Python3d3Parser.Print_stmtContext):
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

    # Visit a parse tree produced by Python3d3Parser#range.
    def visitRange(self, ctx: Python3d3Parser.RangContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d3Parser#comprehension.
    def visitComp_op(self, ctx: Python3d3Parser.Comp_opContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Python3d3Parser#expr.
    def visitExpr(self, ctx: Python3d3Parser.ExprContext):
        if '+' in ctx.getText():
            l = ctx.expr()[0].getText().replace('"', "'")
            r = ctx.expr()[1].getText().replace('"', "'")

            # Check if a variable is in equasion and if one of these variables is a string (lookup at assignment dict)
            if ctx.expr()[0].NAME():
                if self.assignments.get(str(ctx.expr()[0].NAME())) == self.templates['str']:
                    return (f'CONCAT({l}, {r})') 
            if ctx.expr()[1].NAME():
                if self.assignments.get(str(ctx.expr()[1].NAME())) == self.templates['str']:
                    return (f'CONCAT({l}, {r})')
            
            # Check if one expressing is a clear string
            if ctx.expr()[0].STRING() or ctx.expr()[1].STRING():
                return (f'CONCAT({l}, {r})')
        
        elif '%' in ctx.getText():
            l = ctx.expr()[0].getText().replace('"', "'")
            r = ctx.expr()[1].getText().replace('"', "'")
            return f'MOD({l},{r})'

        return str(ctx.getText().replace('"', "'").replace('==', '='))

    # Visit a parse tree produced by Python3d3Parser#typ.
    def visitTyp(self, ctx:Python3d3Parser.TypContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by Python3d3Parser#db_reference.
    def visitDb_reference(self, ctx:Python3d3Parser.Db_referenceContext):
        return self.visitChildren(ctx)

del Python3d3Parser
