# Generated from MMADL.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MMADLParser import MMADLParser
else:
    from MMADLParser import MMADLParser

# This class defines a complete generic visitor for a parse tree produced by MMADLParser.

class MMADLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MMADLParser#mmadl.
    def visitMmadl(self, ctx:MMADLParser.MmadlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#header.
    def visitHeader(self, ctx:MMADLParser.HeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#require.
    def visitRequire(self, ctx:MMADLParser.RequireContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#input_params.
    def visitInput_params(self, ctx:MMADLParser.Input_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#ensure.
    def visitEnsure(self, ctx:MMADLParser.EnsureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#output_params.
    def visitOutput_params(self, ctx:MMADLParser.Output_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#param_name.
    def visitParam_name(self, ctx:MMADLParser.Param_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#param_type.
    def visitParam_type(self, ctx:MMADLParser.Param_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#index.
    def visitIndex(self, ctx:MMADLParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#indexed_expression.
    def visitIndexed_expression(self, ctx:MMADLParser.Indexed_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#body.
    def visitBody(self, ctx:MMADLParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#end_of_line.
    def visitEnd_of_line(self, ctx:MMADLParser.End_of_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#comment.
    def visitComment(self, ctx:MMADLParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#operators_list.
    def visitOperators_list(self, ctx:MMADLParser.Operators_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#operator.
    def visitOperator(self, ctx:MMADLParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#simple_operator.
    def visitSimple_operator(self, ctx:MMADLParser.Simple_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#assignment_operator.
    def visitAssignment_operator(self, ctx:MMADLParser.Assignment_operatorContext):
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#exit_value.
    def visitExit_value(self, ctx:MMADLParser.Exit_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#loop_control_operator.
    def visitLoop_control_operator(self, ctx:MMADLParser.Loop_control_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#math_expression.
    def visitMath_expression(self, ctx:MMADLParser.Math_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#math_string.
    def visitMath_string(self, ctx:MMADLParser.Math_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#number.
    def visitNumber(self, ctx:MMADLParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#function_call.
    def visitFunction_call(self, ctx:MMADLParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#variables_list.
    def visitVariables_list(self, ctx:MMADLParser.Variables_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#known_lexem.
    def visitKnown_lexem(self, ctx:MMADLParser.Known_lexemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#bool_value.
    def visitBool_value(self, ctx:MMADLParser.Bool_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#composite_operator.
    def visitComposite_operator(self, ctx:MMADLParser.Composite_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#if_operator.
    def visitIf_operator(self, ctx:MMADLParser.If_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#loop_operator.
    def visitLoop_operator(self, ctx:MMADLParser.Loop_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#for_operator.
    def visitFor_operator(self, ctx:MMADLParser.For_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#for_symbol.
    def visitFor_symbol(self, ctx:MMADLParser.For_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#endfor_symbol.
    def visitEndfor_symbol(self, ctx:MMADLParser.Endfor_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#while_operator.
    def visitWhile_operator(self, ctx:MMADLParser.While_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#while_symbol.
    def visitWhile_symbol(self, ctx:MMADLParser.While_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#do_symbol.
    def visitDo_symbol(self, ctx:MMADLParser.Do_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#endwhile_symbol.
    def visitEndwhile_symbol(self, ctx:MMADLParser.Endwhile_symbolContext):
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#iteration_end.
    def visitIteration_end(self, ctx:MMADLParser.Iteration_endContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#iteration_elem.
    def visitIteration_elem(self, ctx:MMADLParser.Iteration_elemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#condition.
    def visitCondition(self, ctx:MMADLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#simple_condition.
    def visitSimple_condition(self, ctx:MMADLParser.Simple_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#logic_connective.
    def visitLogic_connective(self, ctx:MMADLParser.Logic_connectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#order_relation.
    def visitOrder_relation(self, ctx:MMADLParser.Order_relationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#binary_relation.
    def visitBinary_relation(self, ctx:MMADLParser.Binary_relationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#colon.
    def visitColon(self, ctx:MMADLParser.ColonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MMADLParser#comma.
    def visitComma(self, ctx:MMADLParser.CommaContext):
        return self.visitChildren(ctx)



del MMADLParser