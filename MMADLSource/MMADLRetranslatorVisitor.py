# Generated from MMADL.g4 by ANTLR 4.9
from lib2to3.pgen2.token import COMMA
from antlr4 import *

from ANTLR.MMADLParser import MMADLParser
from MMADLTranslatorVisitor import MMADLTranslatorVisitor

# This class defines a complete generic visitor for a parse tree produced by MMADLParser.

class MMADLRetranslatorVisitor(MMADLTranslatorVisitor):
    def __init__(self) -> None:
        super().__init__()

    def addToken(self, token: TerminalNode) -> None:
        if token is not None:
            self.code += token.__str__()
            self.code += ' '

    def addNewline(self) -> None:
        self.code += '\n'

    # Visit a parse tree produced by MMADLParser#mmadl.
    def visitMmadl(self, ctx:MMADLParser.MmadlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#header.
    def visitHeader(self, ctx:MMADLParser.HeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#require.
    def visitRequire(self, ctx:MMADLParser.RequireContext):
        self.addToken(ctx.INPUT())

        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#input_params.
    def visitInput_params(self, ctx:MMADLParser.Input_paramsContext):
        for i in range(len(ctx.param_name())):
            self.visit(ctx.param_name(i))
            self.addToken(ctx.COLON(i))
            self.visit(ctx.param_type(i))
            self.addToken(ctx.COMMA(i))
        
        self.addNewline()
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#ensure.
    def visitEnsure(self, ctx:MMADLParser.EnsureContext):
        self.addToken(ctx.OUTPUT())

        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#output_params.
    def visitOutput_params(self, ctx:MMADLParser.Output_paramsContext):
        for i in range(len(ctx.param_type())):
            self.visit(ctx.param_type(i))
            self.addToken(ctx.COMMA(i))

        self.addNewline()
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#param_name.
    def visitParam_name(self, ctx:MMADLParser.Param_nameContext):
        self.addToken(ctx.STRING())

        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#param_type.
    def visitParam_type(self, ctx:MMADLParser.Param_typeContext):
        self.addToken(ctx.POINTER())
        self.addToken(ctx.STRING())

        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#body.
    def visitBody(self, ctx:MMADLParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#comment.
    def visitComment(self, ctx:MMADLParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#operators_list.
    def visitOperators_list(self, ctx:MMADLParser.Operators_listContext):
        for i in range(len(ctx.operator())):
            self.visit(ctx.operator(i))
            self.addToken(ctx.SEMICOLON(i))

        self.addNewline()
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#operator.
    def visitOperator(self, ctx:MMADLParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#simple_operator.
    def visitSimple_operator(self, ctx:MMADLParser.Simple_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#assignment_operator.
    def visitAssignment_operator(self, ctx:MMADLParser.Assignment_operatorContext):
        self.visit(ctx.param_name(0))
        if ctx.param_type() is not None:
            self.visit(ctx.param_type())
        self.addToken(ctx.ASSIGNMENT())

        if ctx.param_name(1) is not None:
            self.visit(ctx.param_name(1))
        if ctx.expression() is not None:
            self.visit(ctx.expression())

        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#control_operator.
    def visitControl_operator(self, ctx:MMADLParser.Control_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#var_definition_operator.
    def visitVar_definition_operator(self, ctx:MMADLParser.Var_definition_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#expression.
    def visitExpression(self, ctx:MMADLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#exit_operator.
    def visitExit_operator(self, ctx:MMADLParser.Exit_operatorContext):
        self.addToken(ctx.getChild(0).getText())

        for i in range(len(ctx.exit_value())):
            self.visit(ctx.exit_value(i))
            self.addToken(ctx.COMMA(i))

        self.addNewline()


    # return self.visitChildren(ctx)
    def visitExit_value(self, ctx:MMADLParser.Exit_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#loop_control_operator.
    def visitLoop_control_operator(self, ctx:MMADLParser.Loop_control_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#math_expression.
    def visitMath_expression(self, ctx:MMADLParser.Math_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#function_call.
    def visitFunction_call(self, ctx:MMADLParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#variables_list.
    def visitVariables_list(self, ctx:MMADLParser.Variables_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#known_lexem.
    def visitKnown_lexem(self, ctx:MMADLParser.Known_lexemContext):
        self.addToken(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#bool_value.
    def visitBool_value(self, ctx:MMADLParser.Bool_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#composite_operator.
    def visitComposite_operator(self, ctx:MMADLParser.Composite_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#if_operator.
    def visitIf_operator(self, ctx:MMADLParser.If_operatorContext):
        self.addToken(ctx.IF())
        self.visit(ctx.condition(0))
        self.addToken(ctx.THEN(0))
        self.addNewline()

        self.visit(ctx.body(0))

        for i in range(len(ctx.ELSEIF())):
            self.addToken(ctx.ELSEIF(i))
            self.visit(ctx.condition(i + 1))
            self.addToken(ctx.THEN(i + 1))
            self.addNewline()
            self.visit(ctx.body(i + 1))

        if ctx.ELSE() is not None:
            self.addToken(ctx.ELSE())
            self.addNewline()
            self.visit(ctx.body()[-1])

        self.addToken(ctx.ENDIF())
        self.addNewline()

        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#loop_operator.
    def visitLoop_operator(self, ctx:MMADLParser.Loop_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#for_operator.
    def visitFor_operator(self, ctx:MMADLParser.For_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#while_operator.
    def visitWhile_operator(self, ctx:MMADLParser.While_operatorContext):
        self.addToken(ctx.WHILE())
        self.visit(ctx.condition())
        self.addToken(ctx.DO())
        self.addNewline()
        self.visit(ctx.body())
        self.addToken(ctx.ENDWHILE())
        self.addNewline()

        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#condition.
    def visitCondition(self, ctx:MMADLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#simple_condition.
    def visitSimple_condition(self, ctx:MMADLParser.Simple_conditionContext):
        if ctx.OPENPARENTHESIS() is not None:
            self.addToken(ctx.OPENPARENTHESIS())
            self.visit(ctx.condition())
            self.addToken(ctx.CLOSEPARENTHESIS())

            return

        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#logic_connective.
    def visitLogic_connective(self, ctx:MMADLParser.Logic_connectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#order_relation.
    def visitOrder_relation(self, ctx:MMADLParser.Order_relationContext):
        self.visit(ctx.getChild(0))

        self.addToken(ctx.binary_relation().getText())

        self.visit(ctx.getChild(2))

        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#binary_relation.
    def visitBinary_relation(self, ctx:MMADLParser.Binary_relationContext):
        return self.visitChildren(ctx)



del MMADLParser