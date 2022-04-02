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

        self.code_level = -1
        self.tex_level = 1

        self.newline = False

        self.code_printer = TexCodePrinter()

        self.table = TexTable()

    def addToken(self, token: str) -> None:
        if token is not None:
            self.code += token.__str__()
            self.code += ' '

    def addNewline(self) -> None:
        self.code += '$ \n\\newline\n $ \\null ' + (self.code_level if self.code_level > 0 else 0) * '\\quad '

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

        return

    # Visit a parse tree produced by MMADLParser#param_name.
    def visitParam_name(self, ctx:MMADLParser.Param_nameContext):
        self.addToken(self.code_printer.printCodeText(ctx.STRING()))

        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#param_type.
    def visitParam_type(self, ctx:MMADLParser.Param_typeContext):
        for i in range(len(ctx.POINTER())):
            self.addToken(self.code_printer.print(
                self.table.getToken(ctx.POINTER(i))
                )
            )

        self.addToken(self.code_printer.printKeyWord(ctx.STRING()))
        return

        # Visit a parse tree produced by MMADLParser#index.
    def visitIndex(self, ctx:MMADLParser.IndexContext):
        self.addToken(self.code_printer.printCodeText(ctx.OPENBRACKET()))
        self.visit(ctx.indexed_expression())
        self.addToken(self.code_printer.printCodeText(ctx.CLOSEBRACKET()))
        return

    def visitIndexed_expression(self, ctx:MMADLParser.Indexed_expressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#body.
    def visitBody(self, ctx:MMADLParser.BodyContext):
        self.code_level += 1
        self.addNewline()
        res = self.visitChildren(ctx)
        self.code_level -= 1
        self.addNewline()
        return res

    # Visit a parse tree produced by MMADLParser#end_of_line.
    def visitEnd_of_line(self, ctx:MMADLParser.End_of_lineContext):
        self.addNewline()
        self.newline = True
        return

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
        self.addToken(self.code_printer.printKeyWord(ctx.getChild(0)))

        for i in range(len(ctx.exit_value())):
            self.visit(ctx.exit_value(i))
            self.addToken(self.code_printer.printCodeText(ctx.COMMA(i)))

    def visitExit_value(self, ctx:MMADLParser.Exit_valueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#loop_control_operator.
    def visitLoop_control_operator(self, ctx:MMADLParser.Loop_control_operatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#math_expression.
    def visitMath_expression(self, ctx:MMADLParser.Math_expressionContext):
        return self.visitChildren(ctx)
    
    def visitMath_string(self, ctx:MMADLParser.Math_stringContext):
        self.addToken(self.code_printer.print(ctx.MATH_STRING().__str__().replace('$', '')))

    # Visit a parse tree produced by MMADLParser#number.
    def visitNumber(self, ctx:MMADLParser.NumberContext):
        self.addToken(ctx.NUMBER())

    # Visit a parse tree produced by MMADLParser#function_call.
    def visitFunction_call(self, ctx:MMADLParser.Function_callContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#variables_list.
    def visitVariables_list(self, ctx:MMADLParser.Variables_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#known_lexem.
    def visitKnown_lexem(self, ctx:MMADLParser.Known_lexemContext):
        self.addToken(self.code_printer.printKeyWord(ctx.getText()))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#bool_value.
    def visitBool_value(self, ctx:MMADLParser.Bool_valueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#composite_operator.
    def visitComposite_operator(self, ctx:MMADLParser.Composite_operatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#if_operator.
    def visitIf_operator(self, ctx:MMADLParser.If_operatorContext):
        self.addToken(self.code_printer.printKeyWord(ctx.IF()))
        self.visit(ctx.condition(0))
        self.addToken(self.code_printer.printKeyWord(ctx.THEN(0)))

        self.visit(ctx.body(0))

        for i in range(len(ctx.ELSEIF())):
            self.addToken(self.code_printer.printKeyWord(ctx.ELSEIF(i)))
            self.visit(ctx.condition(i + 1))
            self.addToken(self.code_printer.printKeyWord(ctx.THEN(i + 1)))
            self.visit(ctx.body(i + 1))

        if ctx.ELSE() is not None:
            self.addToken(self.code_printer.printKeyWord(ctx.ELSE()))
            self.visit(ctx.body()[-1])

        self.addToken(self.code_printer.printKeyWord(ctx.ENDIF()))

    # Visit a parse tree produced by MMADLParser#loop_operator.
    def visitLoop_operator(self, ctx:MMADLParser.Loop_operatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#for_operator.
    def visitFor_operator(self, ctx:MMADLParser.For_operatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#for_symbol.
    def visitFor_symbol(self, ctx:MMADLParser.For_symbolContext):
        self.addToken(self.code_printer.printKeyWord(ctx.FOR()))
        return

    # Visit a parse tree produced by MMADLParser#endfor_symbol.
    def visitEndfor_symbol(self, ctx:MMADLParser.Endfor_symbolContext):
        self.addToken(self.code_printer.printKeyWord(ctx.ENDFOR()))
        return

    # Visit a parse tree produced by MMADLParser#while_operator.
    def visitWhile_operator(self, ctx:MMADLParser.While_operatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#while_symbol.
    def visitWhile_symbol(self, ctx:MMADLParser.While_symbolContext):
        self.addToken(self.code_printer.printKeyWord(ctx.WHILE()))
        return

    # Visit a parse tree produced by MMADLParser#endwhile_symbol.
    def visitEndwhile_symbol(self, ctx:MMADLParser.Endwhile_symbolContext):
        self.addToken(self.code_printer.printKeyWord(ctx.ENDWHILE()))
        return

    # Visit a parse tree produced by MMADLParser#do_symbol.
    def visitDo_symbol(self, ctx:MMADLParser.Do_symbolContext):
        self.addToken(self.code_printer.printKeyWord(ctx.DO()))
        return

    # Visit a parse tree produced by MMADLParser#for_range.
    def visitFor_range(self, ctx:MMADLParser.For_rangeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#include.
    def visitInclude(self, ctx:MMADLParser.IncludeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#iteration.
    def visitIteration(self, ctx:MMADLParser.IterationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#from_symbol.
    def visitFrom_symbol(self, ctx:MMADLParser.From_symbolContext):
        self.addToken(self.code_printer.printKeyWord(ctx.FROM()))
        return

    # Visit a parse tree produced by MMADLParser#iteration_end.
    def visitIteration_end(self, ctx:MMADLParser.Iteration_endContext):
        self.addToken(self.code_printer.printKeyWord(ctx.getText()))
        return

    # Visit a parse tree produced by MMADLParser#iteration_elem.
    def visitIteration_elem(self, ctx:MMADLParser.Iteration_elemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MMADLParser#condition.
    def visitCondition(self, ctx:MMADLParser.ConditionContext):
        self.visit(ctx.simple_condition(0))

        for i in range(len(ctx.logic_connective())):
            self.visit(ctx.logic_connective(i))
            self.visit(ctx.simple_condition(i + 1))

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
        self.addToken(self.code_printer.printKeyWord(ctx.getText()))

    # Visit a parse tree produced by MMADLParser#order_relation.
    def visitOrder_relation(self, ctx:MMADLParser.Order_relationContext):
        self.visit(ctx.getChild(0))

        # self.addToken(ctx.binary_relation().getText())
        self.addToken(self.code_printer.printCodeText(
            self.table.getToken(ctx.binary_relation().getText())
            )
        )

        self.visit(ctx.getChild(2))

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
                '\\begin{document}\n'\
                '\\noindent\n'

        tail = '\\end{document}\n'

        return head, tail


del MMADLParser
