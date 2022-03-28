from antlr4 import *

import sys
sys.path.append('..')

from ANTLR.MMADLParser import MMADLParser
from MMADLTranslatorVisitor import MMADLTranslatorVisitor

from LaTeXTranslator.TexTable import TexTable


class TexCodePrinter:
    def __init__(self, code_color: str = 'black', key_word_color: str = 'blue', comment_color: str = 'green') -> None:
        self.code_color = code_color
        self.key_word_color = key_word_color
        self.comment_color = comment_color

    def print(self, token: TerminalNode) -> str:
        return token.__str__() + ' \ ' if token is not None else ''

    def printCodeText(self, token: TerminalNode) -> str:
        if token is None:
            return ''
        return '\\textcolor{' + self.code_color + '}{' + self._to_tex_string(token.__str__()) + '} \ '

    def printKeyWord(self, token: TerminalNode) -> str:
        if token is None:
            return ''
        return '\\textbf{\\textcolor{' + self.key_word_color + '}{' + self._to_tex_string(token.__str__()) + '}} \ '

    def printComment(self, token: TerminalNode) -> str:
        if token is None:
            return ''
        return '\\textsl{\\textcolor{' + self.comment_color + '}{' + self._to_tex_string(token.__str__()) + '}} \ '

    def _to_tex_string(self, s: str) -> str:
        return s.replace('_', '\\_')


class MMADLTranslatorTexVisitor(MMADLTranslatorVisitor):
    def __init__(self) -> None:
        super().__init__()

        self.code_level = 0
        self.tex_level = 1

        self.code_printer = TexCodePrinter()

        self.table = TexTable()

    def addToken(self, token: str) -> None:
        if token is not None:
            self.code += token.__str__()
            self.code += ' '

    def addNewline(self) -> None:
        self.code += '$ \n\\newline\n $ \\null ' + self.code_level * '\\quad '

    # Visit a parse tree produced by MMADLParser#mmadl.
    def visitMmadl(self, ctx:MMADLParser.MmadlContext):
        head, tail = self.getTexCodeTemplete()

        self.code += head + ' $ '
        res = self.visitChildren(ctx)
        self.code += '$ \n' + tail
        
        return res

    # Visit a parse tree produced by MMADLParser#header.
    def visitHeader(self, ctx:MMADLParser.HeaderContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#require.
    def visitRequire(self, ctx:MMADLParser.RequireContext):
        self.addToken(self.code_printer.printKeyWord(ctx.INPUT()))

        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#input_params.
    def visitInput_params(self, ctx:MMADLParser.Input_paramsContext):
        for i in range(len(ctx.param_name())):
            self.visit(ctx.param_name(i))
            self.addToken(self.code_printer.printCodeText(ctx.COLON(i)))
            self.visit(ctx.param_type(i))
            self.addToken(self.code_printer.printCodeText(ctx.COMMA(i)))
        
        self.addNewline()
        return

    # Visit a parse tree produced by MMADLParser#ensure.
    def visitEnsure(self, ctx:MMADLParser.EnsureContext):
        self.addToken(self.code_printer.printKeyWord(ctx.OUTPUT()))

        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#output_params.
    def visitOutput_params(self, ctx:MMADLParser.Output_paramsContext):
        for i in range(len(ctx.param_type())):
            self.visit(ctx.param_type(i))
            self.addToken(self.code_printer.print(ctx.COMMA(i)))

        self.addNewline()
        return

    # Visit a parse tree produced by MMADLParser#param_name.
    def visitParam_name(self, ctx:MMADLParser.Param_nameContext):
        self.addToken(self.code_printer.printCodeText(ctx.STRING()))

        return
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#param_type.
    def visitParam_type(self, ctx:MMADLParser.Param_typeContext):
        for i in range(len(ctx.POINTER())):
            self.addToken(self.code_printer.print(
                self.table.getToken(ctx.POINTER(i))
                )
            )

        if ctx.STRING() is not None:
            self.addToken(self.code_printer.printKeyWord(ctx.STRING()))
        else:
            self.visit(ctx.composite_param_type())

        return
        # return self.visitChildren(ctx)

    def visitComposite_param_type(self, ctx:MMADLParser.Param_typeContext):
        self.addToken(self.code_printer.printKeyWord(ctx.LE()))
        self.visit(ctx.param_type(0))
        for i in range(len(ctx.COMMA())):
            self.addToken(self.code_printer.printKeyWord(ctx.COMMA(i)))
            self.visit(ctx.param_type(i + 1))
        self.addToken(self.code_printer.printKeyWord(ctx.GT()))
        return

    # Visit a parse tree produced by MMADLParser#body.
    def visitBody(self, ctx:MMADLParser.BodyContext):
        return self.visitChildren(ctx)

    def visitIndex(self, ctx:MMADLParser.BodyContext):
        self.addToken(self.code_printer.printKeyWord(ctx.OPEN_BRACKET()))
        self.addToken(self.code_printer.printKeyWord(ctx.STRING()))
        self.addToken(self.code_printer.printKeyWord(ctx.CLOSE_BRACKET()))

    # Visit a parse tree produced by MMADLParser#comment.
    def visitComment(self, ctx:MMADLParser.CommentContext):
        comment = ''
        comment += self.table.getToken(ctx.OPENCOMMENT())
        comment += ctx.CUSTOM_STRING().__str__()
        comment += self.table.getToken(ctx.CLOSECOMMENT())

        self.addToken(self.code_printer.printComment(comment))
        return

    # Visit a parse tree produced by MMADLParser#operators_list.
    def visitOperators_list(self, ctx:MMADLParser.Operators_listContext):
        for i in range(len(ctx.operator())):
            self.visit(ctx.operator(i))
            self.addToken(self.code_printer.printCodeText(ctx.SEMICOLON(i)))

        self.addNewline()

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
        self.addToken(self.code_printer.printCodeText( 
            self.table.getToken(ctx.ASSIGNMENT()))
        )

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
        self.addToken(' ')
        if ctx.CUSTOM_STRING() is not None:
            self.addToken(self.code_printer.printCodeText(ctx.CUSTOM_STRING()))
        elif ctx.NUMBER() is not None:
            self.addToken(self.code_printer.printCodeText(ctx.NUMBER()))
        else:
            self.visit(ctx.param_name(0))
            if ctx.MATH_BINARY_OPERAIONS() is not None:
                for i in range(len(ctx.MATH_BINARY_OPERAIONS())):
                    self.addToken(self.code_printer.printCodeText(ctx.MATH_BINARY_OPERAIONS(i)))
                    self.visit(ctx.param_name(i + 1))
        self.addToken(' ')


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
        loop = ctx.getChild(0)
        self.addToken(loop.getChild(0))
        self.visit(loop.getChild(1))
        self.addToken(loop.getChild(2))
        self.addNewline()
        self.visit(loop.getChild(3))
        self.addToken(loop.getChild(4))
        self.addNewline()
        # sreturn self.visitChildren(ctx)


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
        self.visit(ctx.simple_condition(0))

        for i in range(len(ctx.logic_connective())):
            self.visit(ctx.logic_connective(i))
            self.visit(ctx.simple_condition(i + 1))

        # return self.visitChildren(ctx)


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
        self.addToken(ctx.getText())
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#order_relation.
    def visitOrder_relation(self, ctx:MMADLParser.Order_relationContext):
        self.visit(ctx.getChild(0))

        self.addToken(ctx.binary_relation().getText())

        self.visit(ctx.getChild(2))

        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#binary_relation.
    def visitBinary_relation(self, ctx:MMADLParser.Binary_relationContext):
        return self.visitChildren(ctx)


    def getTexCodeTemplete(self):
        head = '\\documentclass[a4paper,12pt]{article}\n'\
                '\n'\
                '\\usepackage[hidelinks]{hyperref}\n'\
                '\\usepackage{amsmath}\n'\
                '\\usepackage{mathtools}\n'\
                '\\usepackage{shorttoc}\n'\
                '\\usepackage{cmap}\n'\
                '\\usepackage[T2A]{fontenc}\n'\
                '\\usepackage[utf8]{inputenc}\n'\
                '\\usepackage[english, russian]{babel}\n'\
                '\\usepackage{xcolor}\n'\
                '\\usepackage{graphicx}\n'\
                '\\usepackage{float}\n'\
                '\n'\
                '\\definecolor{linkcolor}{HTML}{000000}\n'\
                '\\definecolor{urlcolor}{HTML}{0085FF}\n'\
                '\\hypersetup{pdfstartview=FitH,  linkcolor=linkcolor,urlcolor=urlcolor, colorlinks=true}\n'\
                '\n'\
                '\\DeclarePairedDelimiter{\\floor}{\lfloor}{\\rfloor}\n'\
                '\n'\
                '\n'\
                '\\begin{document}\n'

        tail = '\\end{document}\n'

        return head, tail


del MMADLParser
