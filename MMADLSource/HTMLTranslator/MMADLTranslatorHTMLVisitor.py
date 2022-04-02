from antlr4 import *

import sys
sys.path.append('..')

from ANTLR.MMADLParser import MMADLParser
from MMADLTranslatorVisitor import MMADLTranslatorVisitor

code_color = "black"
key_word_color = "blue"
comment_color = "green"

class HTMLPrinter:
    def __init__(self):
        self.head = "<!DOCTYPE html>\n" \
                    "<html>\n" \
                    "<head> \n" \
                    '<meta charset="utf-8" />\n' \
                    "<title>HTML Document</title>\n" \
                    "</head>\n"
        self.tail = "</html>\n"


class MMADLTranslatorHTMLVisitor(MMADLTranslatorVisitor):
    def __init__(self):
        super().__init__()
        self.printer = HTMLPrinter()
        self.intent = 0
        self.code = self.printer.head

    def add_code_lexem(self, code_str: str = ''):
        self.code += '<p style="color:rgb(255,0,0);">' + code_str + '<\p>\n'

    def add_comment(self, comment_str: str = ''):
        self.code += '<p style="color:rgb(255,0,0);">' + comment_str + '<\p>\n'

    def add_key_word(self, key_word: str = ''):
        self.code += '<p style="color:rgb(255,0,0);">' + key_word + '<\p>'

    def add_new_line(self): self.code += "<br>"

    def visitMMADL(self, ctx: MMADLParser.MmadlContext):
        self.visitChildren(ctx)
        self.code += self.printer.tail

    def visitHeader(self): self.visitChildren()

    def visitRequire(self, ctx: MMADLParser.RequireContext): self.add_key_word(ctx.INPUT())

    def visitInput_params(self, ctx: MMADLParser.Input_paramsContext):
        if ctx.param_name() is not None:
            self.visit(ctx.param_name(0))
            self.add_code_lexem(ctx.COLON(0))
            self.visit(ctx.param_type(0))

        for i in range(len(ctx.COMMA())):
            self.add_code_lexem(ctx.COMMA(i))
            self.visit(ctx.param_name(i + 1))
            self.add_code_lexem(ctx.COLON(i + 1))
            self.visit(ctx.param_type(i + 1))

    def visitEnsure(self, ctx: MMADLParser.EnsureContext): self.add_key_word(ctx.OUTPUT())

    def visitOutput_params(self, ctx: MMADLParser.Output_paramsContext):
        if ctx.param_type() is not None:
            self.visit(ctx.param_type(0))

        for i in range(len(ctx.COMMA())):
            self.add_code_lexem(ctx.COMMA(i))
            self.visit(ctx.param_type(i + 1))

    def visitBody(self, ctx: MMADLParser.BodyContext): self.visitChildren(ctx)

    def visitParam_name(self, ctx: MMADLParser.Param_nameContext):
        self.add_code_lexem(ctx.STRING(0))
        if ctx.index() is not None:
            for i in range(len(ctx.index())):
                self.visit(ctx.index(i))

    def visitParam_type(self, ctx: MMADLParser.Param_typeContext):
        if ctx.POINTER() is not None:
            self.add_code_lexem(ctx.POINTER(0))
            if ctx.composite_param_type() is not None:
                self.visit(ctx.composite_param_type())
            else:
                self.add_code_lexem(ctx.STRING(0))
        else:
            self.add_code_lexem(ctx.STRING(0))

    def visitComposite_param_type(self, ctx: MMADLParser.Composite_param_typeContext):
        self.add_code_lexem(ctx.LE(0))
        self.visit(ctx.param_type(0))
        if ctx.COMMA() is not None:
            for i in range(len(ctx.COMMA())):
                self.add_code_lexem(ctx.COMMA(i))
                self.visit(ctx.param_type(i + 1))
        self.add_code_lexem(ctx.GT(0))

    def visitComment(self, ctx: MMADLParser.CommentContext): self.add_comment(ctx.CUSTOM_STRING(0))

    def visitOperators_list(self, ctx: MMADLParser.Operators_listContext):
        self.visit(ctx.operator(0))
        if ctx.SEMICOLON() is not None:
            for i in range(len(ctx.SEMICOLON())):
                self.add_code_lexem(ctx.SEMICOLON(i))
                self.visit(ctx.operator(i + 1))


    def visitOperator(self, ctx: MMADLParser.OperatorContext): self.visitChildren(ctx)

    def visitSimple_operator(self, ctx: MMADLParser.Simple_operatorContext): self.visitChildren(ctx)

    def visitAssignment_operator(self, ctx: MMADLParser.Assignment_operatorContext):
        self.visit(ctx.param_name())
        if ctx.param_type is not None:
            self.visit(ctx.param_type())
        self.add_code_lexem(ctx.ASSIGNMENT())
        self.visit(ctx.childrens.last())

    def visitControl_operator(self, ctx: MMADLParser.Control_operatorContext): self.visitChildren(ctx)

    def visitVar_definition_operator(self, ctx: MMADLParser.Var_definition_operatorContext):
        self.visit(ctx.param_name())
        self.add_code_lexem(ctx.COLON())
        self.visit(ctx.param_type())

    def visitExpression(self, ctx: MMADLParser.ExpressionContext): self.visitChildren(ctx)

    def visitExit_operator(self, ctx: MMADLParser.Exit_operatorContext):
        if ctx.RETURN is not NONE:
            self.add_key_word(ctx.RETURN())
        else:
            self.add_key_word(ctx.YIELD())

        if ctx.COMMA() is not None:
            for i in range(len(ctx.COMMA())):
                self.visit(ctx.exit_value(i))
                self.add_code_lexem(ctx.COMMA(i))

    def visitExit_value(self, ctx: MMADLParser.Exit_valueContext): self.visitChildren(ctx)

    def visitLoop_control_operator(self, ctx: MMADLParser.Loop_control_operatorContext):
        if ctx.CONTINUE() is not None:
            self.add_code_lexem(ctx.CONTINUE())
        else:
            self.add_code_lexem(ctx.BREAK())

    def visitMath_expression(self, ctx: MMADLParser.Math_expressionContext):
        if ctx.MATH_EXPRESSION_SIGN() is not None:
            self.visit(ctx.param_name(0))
            if ctx.MATH_BINARY_OPERATIONS() is not None:
                for i in range(len(ctx.MATH_BINARY_OPERATIONS())):
                    self.add_code_lexem(ctx.MATH_BINARY_OPERATIONS(i))
                    self.visit(ctx.param_name(i + 1))
        elif ctx.CUSTOM_STRING() is not None:
            self.add_code_lexem(ctx.CUSTOM_STRING())
        else:
            self.add_code_lexem(ctx.NUMBER())

    #def visitFunctional_call(self, ctx: MMADLParser.FunctionalCallContext):

