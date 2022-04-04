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
                    "</head>\n" \
                    "<div>"
        self.tail = "</div>" \
                    "</html>\n"


class MMADLTranslatorHTMLVisitor(MMADLTranslatorVisitor):
    def __init__(self):
        super().__init__()
        self.printer = HTMLPrinter()
        self.intent = 0
        self.str_intent = "  "
        self.code = self.printer.head

    def get_code(self) -> str:
        self.code += self.printer.tail
        return self.code

    def add_code_lexem(self, code_str: TerminalNode):
        self.code += str(code_str) + " "

    def add_comment(self, comment_str: TerminalNode):
        self.code += '<span style="color: green;">' + "$" + str(comment_str) + "$ " + '</span>'
        self.add_new_line()

    def add_key_word(self, key_word: TerminalNode):
        self.code += '<span  style="color: blue;">' + str(key_word) + " " + '</span>'

    def add_new_line(self): self.code += '</div>\n<div style="padding: 0 {0}px">'.format(self.intent * 10)

    def delete_last_line(self): self.code = self.code[: self.code.rfind('<div')]

    def visitMMADL(self, ctx: MMADLParser.MmadlContext):
        self.visitChildren(ctx)

    def visitHeader(self, ctx: MMADLParser.HeaderContext):
        self.visitChildren(ctx)

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
        self.add_new_line()

    def visitEnsure(self, ctx: MMADLParser.EnsureContext): self.add_key_word(ctx.OUTPUT())

    def visitOutput_params(self, ctx: MMADLParser.Output_paramsContext):
        if ctx.param_type() is not None:
            self.visit(ctx.param_type(0))

        for i in range(len(ctx.COMMA())):
            self.add_code_lexem(ctx.COMMA(i))
            self.visit(ctx.param_type(i + 1))

        self.add_new_line()

    def visitBody(self, ctx: MMADLParser.BodyContext):
        self.visitChildren(ctx)

    def visitParam_name(self, ctx: MMADLParser.Param_nameContext):
        self.add_code_lexem(ctx.STRING())
        if ctx.index() is not None:
            for i in range(len(ctx.index())):
                self.visit(ctx.index(i))

    def visitParam_type(self, ctx: MMADLParser.Param_typeContext):
        if ctx.POINTER() is not None:
            self.add_code_lexem("&#x2191")
            if ctx.composite_param_type() is not None:
                self.visit(ctx.composite_param_type())
            else:
                self.add_code_lexem(ctx.STRING())
        else:
            self.add_code_lexem(ctx.STRING())

    def visitComposite_param_type(self, ctx: MMADLParser.Composite_param_typeContext):
        self.add_code_lexem(ctx.LE())
        self.visit(ctx.param_type(0))
        if ctx.COMMA() is not None:
            for i in range(len(ctx.COMMA())):
                self.add_code_lexem(ctx.COMMA(i))
                self.visit(ctx.param_type(i + 1))
        self.add_code_lexem(ctx.GT())

    def visitComment(self, ctx: MMADLParser.CommentContext):
        self.add_comment(ctx.CUSTOM_STRING())

    def visitOperators_list(self, ctx: MMADLParser.Operators_listContext):
        self.visit(ctx.operator(0))
        if ctx.SEMICOLON() is not None:
            for i in range(len(ctx.SEMICOLON())):
                self.add_code_lexem(ctx.SEMICOLON(i))
                self.visit(ctx.operator(i + 1))
        self.add_new_line()


    def visitOperator(self, ctx: MMADLParser.OperatorContext): self.visitChildren(ctx)

    def visitSimple_operator(self, ctx: MMADLParser.Simple_operatorContext): self.visitChildren(ctx)

    def visitAssignment_operator(self, ctx: MMADLParser.Assignment_operatorContext):
        self.visit(ctx.param_name(0))
        if ctx.param_type() is not None:
            self.visit(ctx.param_type())
        self.add_code_lexem("&#8592")
        if ctx.expression() is not None:
            self.visit(ctx.expression())
        else:
            self.visit(ctx.param_name(1))

    def visitControl_operator(self, ctx: MMADLParser.Control_operatorContext): self.visitChildren(ctx)

    def visitVar_definition_operator(self, ctx: MMADLParser.Var_definition_operatorContext):
        self.visit(ctx.param_name(0))
        self.add_code_lexem(ctx.COLON(0))
        self.visit(ctx.param_type(0))

    def visitExpression(self, ctx: MMADLParser.ExpressionContext): self.visitChildren(ctx)

    def visitExit_operator(self, ctx: MMADLParser.Exit_operatorContext):
        if ctx.RETURN() is not None:
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
            self.add_code_lexem(ctx.CONTINUE(0))
        else:
            self.add_code_lexem(ctx.BREAK(0))

    def visitMath_expression(self, ctx: MMADLParser.Math_expressionContext):
        if ctx.MATH_EXPRESSION_SIGN() is not None and len(ctx.MATH_EXPRESSION_SIGN()) > 0:
            self.visit(ctx.param_name(0))
            if ctx.MATH_BINARY_OPERAIONS() is not None and len(ctx.MATH_BINARY_OPERAIONS()) > 0:
                for i in range(len(ctx.MATH_BINARY_OPERAIONS())):
                    self.add_code_lexem(ctx.MATH_BINARY_OPERAIONS(i))
                    self.visit(ctx.param_name(i + 1))
        elif ctx.CUSTOM_STRING() is not None:
            self.add_code_lexem(ctx.CUSTOM_STRING())
        else:
            self.add_code_lexem(ctx.NUMBER())

    def visitFunction_call(self, ctx: MMADLParser.Function_callContext):
        self.add_code_lexem(ctx.STRING())
        self.add_code_lexem(ctx.OPENPARENTHESIS())
        self.visit(ctx.variables_list())
        self.add_code_lexem(ctx.CLOSEPARENTHESIS())

    def visitVariables_list(self, ctx: MMADLParser.Variables_listContext):
        if ctx.param_name() is not None:
            for i in range(len(ctx.param_name())):
                self.visit(ctx.param_name(i))
                if ctx.COMMA(i) is not None:
                    self.add_code_lexem(ctx.COMMA(i))

    def visitKnown_lexem(self, ctx: MMADLParser.Known_lexemContext):
        if ctx.NIL() is not None:
            self.add_code_lexem(ctx.NIL())
        else:
            self.visit(ctx.bool_value())

    def visitBool_value(self, ctx: MMADLParser.Bool_valueContext):
        if ctx.TRUE() is not None:
            self.add_key_word(ctx.TRUE())
        else:
            self.add_key_word(ctx.FALSE())

    def visitComposite_operator(self, ctx: MMADLParser.Composite_operatorContext): self.visitChildren(ctx)

    def visitIf_operator(self, ctx: MMADLParser.If_operatorContext):
        self.add_key_word(ctx.IF())
        self.visit(ctx.condition(0))
        self.add_key_word(ctx.THEN(0))
        self.intent += 1
        self.add_new_line()
        self.intent -= 1
        self.visit(ctx.body(0))
        count = 0
        if ctx.ELSEIF() is not None:
            for i in range(len(ctx.ELSEIF())):
                self.add_key_word(ctx.ELSEIF(i))
                self.visit(ctx.condition(i + 1))
                self.add_key_word(ctx.THEN(i + 1))
                self.intent += 1
                self.add_new_line()
                self.intent -= 1
                self.visit(ctx.body(i + 1))
                count += 1
        if ctx.ELSE() is not None:
            self.add_key_word(ctx.ELSE())
            self.intent += 1
            self.add_new_line()
            self.intent -= 1
            self.visit(ctx.body(count))
        self.add_key_word(ctx.ENDIF())

    def visitLoop_operator(self, ctx: MMADLParser.Loop_operatorContext): self.visitChildren(ctx)

    def visitFor_operator(self, ctx: MMADLParser.For_operatorContext):
        self.add_key_word(ctx.FOR())
        self.visit(ctx.for_range())
        self.add_key_word(ctx.DO())
        self.intent += 1
        self.add_new_line()
        self.visit(ctx.body())
        self.intent -= 1
        self.delete_last_line()
        self.add_new_line()
        self.add_key_word(ctx.ENDFOR())

    def visitWhile_operator(self, ctx: MMADLParser.While_operatorContext):
        self.add_key_word(ctx.WHILE())
        self.visit(ctx.condition())
        self.add_key_word(ctx.DO())
        self.intent += 1
        self.add_new_line()
        self.visit(ctx.body())
        self.intent -= 1
        self.delete_last_line()
        self.add_new_line()
        self.add_key_word(ctx.ENDWHILE())

    def visitFor_range(self, ctx: MMADLParser.For_rangeContext): self.visitChildren(ctx)

    def visitIndex(self, ctx: MMADLParser.IndexContext):
        self.add_code_lexem(ctx.OPEN_BRACKET())
        self.add_code_lexem(ctx.STRING())
        self.add_code_lexem(ctx.CLOSE_BRACKET())

    def visitInclude(self, ctx: MMADLParser.IncludeContext):
        self.visit(ctx.param_name())
        self.add_code_lexem("&#8712")
        self.visit(ctx.math_expression())

    def visitIteration(self, ctx: MMADLParser.IterationContext):
        self.visit(ctx.param_name())
        self.add_key_word(ctx.FROM())
        self.visit(ctx.math_expression(0))
        if ctx.TO() is not None:
            self.add_key_word(ctx.TO())
        else:
            self.add_key_word(ctx.DOWNTO())
        self.visit(ctx.math_expression(1))

    def visitCondition(self, ctx: MMADLParser.ConditionContext):
        self.visit(ctx.simple_condition(0))
        if ctx.logic_connective() is not None:
            for i in range(len(ctx.logic_connective())):
                self.visit(ctx.logic_connective(i))
                self.visit(ctx.simple_condition(i + 1))

    def visitLogic_connective(self, ctx: MMADLParser.Logic_connectiveContext): self.add_code_lexem(ctx.children[0])

    def visitOrder_relation(self, ctx: MMADLParser.Order_relationContext):
        self.visit(ctx.children[0])
        self.visit(ctx.children[1])
        self.visit(ctx.children[2])

    def visitBinary_relation(self, ctx: MMADLParser.Binary_relationContext): self.add_code_lexem(ctx.children[0])
