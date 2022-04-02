# Generated from MMADL.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MMADLParser import MMADLParser
else:
    from MMADLParser import MMADLParser

# This class defines a complete listener for a parse tree produced by MMADLParser.
class MMADLListener(ParseTreeListener):

    # Enter a parse tree produced by MMADLParser#mmadl.
    def enterMmadl(self, ctx:MMADLParser.MmadlContext):
        pass

    # Exit a parse tree produced by MMADLParser#mmadl.
    def exitMmadl(self, ctx:MMADLParser.MmadlContext):
        pass


    # Enter a parse tree produced by MMADLParser#header.
    def enterHeader(self, ctx:MMADLParser.HeaderContext):
        pass

    # Exit a parse tree produced by MMADLParser#header.
    def exitHeader(self, ctx:MMADLParser.HeaderContext):
        pass


    # Enter a parse tree produced by MMADLParser#require.
    def enterRequire(self, ctx:MMADLParser.RequireContext):
        pass

    # Exit a parse tree produced by MMADLParser#require.
    def exitRequire(self, ctx:MMADLParser.RequireContext):
        pass


    # Enter a parse tree produced by MMADLParser#input_params.
    def enterInput_params(self, ctx:MMADLParser.Input_paramsContext):
        pass

    # Exit a parse tree produced by MMADLParser#input_params.
    def exitInput_params(self, ctx:MMADLParser.Input_paramsContext):
        pass


    # Enter a parse tree produced by MMADLParser#ensure.
    def enterEnsure(self, ctx:MMADLParser.EnsureContext):
        pass

    # Exit a parse tree produced by MMADLParser#ensure.
    def exitEnsure(self, ctx:MMADLParser.EnsureContext):
        pass


    # Enter a parse tree produced by MMADLParser#output_params.
    def enterOutput_params(self, ctx:MMADLParser.Output_paramsContext):
        pass

    # Exit a parse tree produced by MMADLParser#output_params.
    def exitOutput_params(self, ctx:MMADLParser.Output_paramsContext):
        pass


    # Enter a parse tree produced by MMADLParser#param_name.
    def enterParam_name(self, ctx:MMADLParser.Param_nameContext):
        pass

    # Exit a parse tree produced by MMADLParser#param_name.
    def exitParam_name(self, ctx:MMADLParser.Param_nameContext):
        pass


    # Enter a parse tree produced by MMADLParser#param_type.
    def enterParam_type(self, ctx:MMADLParser.Param_typeContext):
        pass

    # Exit a parse tree produced by MMADLParser#param_type.
    def exitParam_type(self, ctx:MMADLParser.Param_typeContext):
        pass


    # Enter a parse tree produced by MMADLParser#index.
    def enterIndex(self, ctx:MMADLParser.IndexContext):
        pass

    # Exit a parse tree produced by MMADLParser#index.
    def exitIndex(self, ctx:MMADLParser.IndexContext):
        pass


    # Enter a parse tree produced by MMADLParser#indexed_expression.
    def enterIndexed_expression(self, ctx:MMADLParser.Indexed_expressionContext):
        pass

    # Exit a parse tree produced by MMADLParser#indexed_expression.
    def exitIndexed_expression(self, ctx:MMADLParser.Indexed_expressionContext):
        pass


    # Enter a parse tree produced by MMADLParser#body.
    def enterBody(self, ctx:MMADLParser.BodyContext):
        pass

    # Exit a parse tree produced by MMADLParser#body.
    def exitBody(self, ctx:MMADLParser.BodyContext):
        pass


    # Enter a parse tree produced by MMADLParser#end_of_line.
    def enterEnd_of_line(self, ctx:MMADLParser.End_of_lineContext):
        pass

    # Exit a parse tree produced by MMADLParser#end_of_line.
    def exitEnd_of_line(self, ctx:MMADLParser.End_of_lineContext):
        pass


    # Enter a parse tree produced by MMADLParser#comment.
    def enterComment(self, ctx:MMADLParser.CommentContext):
        pass

    # Exit a parse tree produced by MMADLParser#comment.
    def exitComment(self, ctx:MMADLParser.CommentContext):
        pass


    # Enter a parse tree produced by MMADLParser#operators_list.
    def enterOperators_list(self, ctx:MMADLParser.Operators_listContext):
        pass

    # Exit a parse tree produced by MMADLParser#operators_list.
    def exitOperators_list(self, ctx:MMADLParser.Operators_listContext):
        pass


    # Enter a parse tree produced by MMADLParser#operator.
    def enterOperator(self, ctx:MMADLParser.OperatorContext):
        pass

    # Exit a parse tree produced by MMADLParser#operator.
    def exitOperator(self, ctx:MMADLParser.OperatorContext):
        pass


    # Enter a parse tree produced by MMADLParser#simple_operator.
    def enterSimple_operator(self, ctx:MMADLParser.Simple_operatorContext):
        pass

    # Exit a parse tree produced by MMADLParser#simple_operator.
    def exitSimple_operator(self, ctx:MMADLParser.Simple_operatorContext):
        pass


    # Enter a parse tree produced by MMADLParser#assignment_operator.
    def enterAssignment_operator(self, ctx:MMADLParser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by MMADLParser#assignment_operator.
    def exitAssignment_operator(self, ctx:MMADLParser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by MMADLParser#control_operator.
    def enterControl_operator(self, ctx:MMADLParser.Control_operatorContext):
        pass

    # Exit a parse tree produced by MMADLParser#control_operator.
    def exitControl_operator(self, ctx:MMADLParser.Control_operatorContext):
        pass


    # Enter a parse tree produced by MMADLParser#var_definition_operator.
    def enterVar_definition_operator(self, ctx:MMADLParser.Var_definition_operatorContext):
        pass

    # Exit a parse tree produced by MMADLParser#var_definition_operator.
    def exitVar_definition_operator(self, ctx:MMADLParser.Var_definition_operatorContext):
        pass


    # Enter a parse tree produced by MMADLParser#expression.
    def enterExpression(self, ctx:MMADLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MMADLParser#expression.
    def exitExpression(self, ctx:MMADLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MMADLParser#exit_operator.
    def enterExit_operator(self, ctx:MMADLParser.Exit_operatorContext):
        pass

    # Exit a parse tree produced by MMADLParser#exit_operator.
    def exitExit_operator(self, ctx:MMADLParser.Exit_operatorContext):
        pass


    # Enter a parse tree produced by MMADLParser#exit_value.
    def enterExit_value(self, ctx:MMADLParser.Exit_valueContext):
        pass

    # Exit a parse tree produced by MMADLParser#exit_value.
    def exitExit_value(self, ctx:MMADLParser.Exit_valueContext):
        pass


    # Enter a parse tree produced by MMADLParser#loop_control_operator.
    def enterLoop_control_operator(self, ctx:MMADLParser.Loop_control_operatorContext):
        pass

    # Exit a parse tree produced by MMADLParser#loop_control_operator.
    def exitLoop_control_operator(self, ctx:MMADLParser.Loop_control_operatorContext):
        pass


    # Enter a parse tree produced by MMADLParser#math_expression.
    def enterMath_expression(self, ctx:MMADLParser.Math_expressionContext):
        pass

    # Exit a parse tree produced by MMADLParser#math_expression.
    def exitMath_expression(self, ctx:MMADLParser.Math_expressionContext):
        pass


    # Enter a parse tree produced by MMADLParser#math_string.
    def enterMath_string(self, ctx:MMADLParser.Math_stringContext):
        pass

    # Exit a parse tree produced by MMADLParser#math_string.
    def exitMath_string(self, ctx:MMADLParser.Math_stringContext):
        pass


    # Enter a parse tree produced by MMADLParser#number.
    def enterNumber(self, ctx:MMADLParser.NumberContext):
        pass

    # Exit a parse tree produced by MMADLParser#number.
    def exitNumber(self, ctx:MMADLParser.NumberContext):
        pass


    # Enter a parse tree produced by MMADLParser#function_call.
    def enterFunction_call(self, ctx:MMADLParser.Function_callContext):
        pass

    # Exit a parse tree produced by MMADLParser#function_call.
    def exitFunction_call(self, ctx:MMADLParser.Function_callContext):
        pass


    # Enter a parse tree produced by MMADLParser#variables_list.
    def enterVariables_list(self, ctx:MMADLParser.Variables_listContext):
        pass

    # Exit a parse tree produced by MMADLParser#variables_list.
    def exitVariables_list(self, ctx:MMADLParser.Variables_listContext):
        pass


    # Enter a parse tree produced by MMADLParser#known_lexem.
    def enterKnown_lexem(self, ctx:MMADLParser.Known_lexemContext):
        pass

    # Exit a parse tree produced by MMADLParser#known_lexem.
    def exitKnown_lexem(self, ctx:MMADLParser.Known_lexemContext):
        pass


    # Enter a parse tree produced by MMADLParser#bool_value.
    def enterBool_value(self, ctx:MMADLParser.Bool_valueContext):
        pass

    # Exit a parse tree produced by MMADLParser#bool_value.
    def exitBool_value(self, ctx:MMADLParser.Bool_valueContext):
        pass


    # Enter a parse tree produced by MMADLParser#composite_operator.
    def enterComposite_operator(self, ctx:MMADLParser.Composite_operatorContext):
        pass

    # Exit a parse tree produced by MMADLParser#composite_operator.
    def exitComposite_operator(self, ctx:MMADLParser.Composite_operatorContext):
        pass


    # Enter a parse tree produced by MMADLParser#if_operator.
    def enterIf_operator(self, ctx:MMADLParser.If_operatorContext):
        pass

    # Exit a parse tree produced by MMADLParser#if_operator.
    def exitIf_operator(self, ctx:MMADLParser.If_operatorContext):
        pass


    # Enter a parse tree produced by MMADLParser#loop_operator.
    def enterLoop_operator(self, ctx:MMADLParser.Loop_operatorContext):
        pass

    # Exit a parse tree produced by MMADLParser#loop_operator.
    def exitLoop_operator(self, ctx:MMADLParser.Loop_operatorContext):
        pass


    # Enter a parse tree produced by MMADLParser#for_operator.
    def enterFor_operator(self, ctx:MMADLParser.For_operatorContext):
        pass

    # Exit a parse tree produced by MMADLParser#for_operator.
    def exitFor_operator(self, ctx:MMADLParser.For_operatorContext):
        pass


    # Enter a parse tree produced by MMADLParser#for_symbol.
    def enterFor_symbol(self, ctx:MMADLParser.For_symbolContext):
        pass

    # Exit a parse tree produced by MMADLParser#for_symbol.
    def exitFor_symbol(self, ctx:MMADLParser.For_symbolContext):
        pass


    # Enter a parse tree produced by MMADLParser#endfor_symbol.
    def enterEndfor_symbol(self, ctx:MMADLParser.Endfor_symbolContext):
        pass

    # Exit a parse tree produced by MMADLParser#endfor_symbol.
    def exitEndfor_symbol(self, ctx:MMADLParser.Endfor_symbolContext):
        pass


    # Enter a parse tree produced by MMADLParser#while_operator.
    def enterWhile_operator(self, ctx:MMADLParser.While_operatorContext):
        pass

    # Exit a parse tree produced by MMADLParser#while_operator.
    def exitWhile_operator(self, ctx:MMADLParser.While_operatorContext):
        pass


    # Enter a parse tree produced by MMADLParser#while_symbol.
    def enterWhile_symbol(self, ctx:MMADLParser.While_symbolContext):
        pass

    # Exit a parse tree produced by MMADLParser#while_symbol.
    def exitWhile_symbol(self, ctx:MMADLParser.While_symbolContext):
        pass


    # Enter a parse tree produced by MMADLParser#do_symbol.
    def enterDo_symbol(self, ctx:MMADLParser.Do_symbolContext):
        pass

    # Exit a parse tree produced by MMADLParser#do_symbol.
    def exitDo_symbol(self, ctx:MMADLParser.Do_symbolContext):
        pass


    # Enter a parse tree produced by MMADLParser#endwhile_symbol.
    def enterEndwhile_symbol(self, ctx:MMADLParser.Endwhile_symbolContext):
        pass

    # Exit a parse tree produced by MMADLParser#endwhile_symbol.
    def exitEndwhile_symbol(self, ctx:MMADLParser.Endwhile_symbolContext):
        pass


    # Enter a parse tree produced by MMADLParser#for_range.
    def enterFor_range(self, ctx:MMADLParser.For_rangeContext):
        pass

    # Exit a parse tree produced by MMADLParser#for_range.
    def exitFor_range(self, ctx:MMADLParser.For_rangeContext):
        pass


    # Enter a parse tree produced by MMADLParser#include.
    def enterInclude(self, ctx:MMADLParser.IncludeContext):
        pass

    # Exit a parse tree produced by MMADLParser#include.
    def exitInclude(self, ctx:MMADLParser.IncludeContext):
        pass


    # Enter a parse tree produced by MMADLParser#iteration.
    def enterIteration(self, ctx:MMADLParser.IterationContext):
        pass

    # Exit a parse tree produced by MMADLParser#iteration.
    def exitIteration(self, ctx:MMADLParser.IterationContext):
        pass


    # Enter a parse tree produced by MMADLParser#from_symbol.
    def enterFrom_symbol(self, ctx:MMADLParser.From_symbolContext):
        pass

    # Exit a parse tree produced by MMADLParser#from_symbol.
    def exitFrom_symbol(self, ctx:MMADLParser.From_symbolContext):
        pass


    # Enter a parse tree produced by MMADLParser#iteration_end.
    def enterIteration_end(self, ctx:MMADLParser.Iteration_endContext):
        pass

    # Exit a parse tree produced by MMADLParser#iteration_end.
    def exitIteration_end(self, ctx:MMADLParser.Iteration_endContext):
        pass


    # Enter a parse tree produced by MMADLParser#iteration_elem.
    def enterIteration_elem(self, ctx:MMADLParser.Iteration_elemContext):
        pass

    # Exit a parse tree produced by MMADLParser#iteration_elem.
    def exitIteration_elem(self, ctx:MMADLParser.Iteration_elemContext):
        pass


    # Enter a parse tree produced by MMADLParser#condition.
    def enterCondition(self, ctx:MMADLParser.ConditionContext):
        pass

    # Exit a parse tree produced by MMADLParser#condition.
    def exitCondition(self, ctx:MMADLParser.ConditionContext):
        pass


    # Enter a parse tree produced by MMADLParser#simple_condition.
    def enterSimple_condition(self, ctx:MMADLParser.Simple_conditionContext):
        pass

    # Exit a parse tree produced by MMADLParser#simple_condition.
    def exitSimple_condition(self, ctx:MMADLParser.Simple_conditionContext):
        pass


    # Enter a parse tree produced by MMADLParser#logic_connective.
    def enterLogic_connective(self, ctx:MMADLParser.Logic_connectiveContext):
        pass

    # Exit a parse tree produced by MMADLParser#logic_connective.
    def exitLogic_connective(self, ctx:MMADLParser.Logic_connectiveContext):
        pass


    # Enter a parse tree produced by MMADLParser#order_relation.
    def enterOrder_relation(self, ctx:MMADLParser.Order_relationContext):
        pass

    # Exit a parse tree produced by MMADLParser#order_relation.
    def exitOrder_relation(self, ctx:MMADLParser.Order_relationContext):
        pass


    # Enter a parse tree produced by MMADLParser#binary_relation.
    def enterBinary_relation(self, ctx:MMADLParser.Binary_relationContext):
        pass

    # Exit a parse tree produced by MMADLParser#binary_relation.
    def exitBinary_relation(self, ctx:MMADLParser.Binary_relationContext):
        pass



del MMADLParser