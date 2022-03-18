# Generated from MMADL.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MMADLParser import MMADLParser
else:
    from MMADLParser import MMADLParser

# This class defines a complete listener for a parse tree produced by MMADLParser.
class MMADLListener(ParseTreeListener):

    # Enter a parse tree produced by MMADLParser#programm.
    def enterProgramm(self, ctx:MMADLParser.ProgrammContext):
        pass

    # Exit a parse tree produced by MMADLParser#programm.
    def exitProgramm(self, ctx:MMADLParser.ProgrammContext):
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


    # Enter a parse tree produced by MMADLParser#body.
    def enterBody(self, ctx:MMADLParser.BodyContext):
        pass

    # Exit a parse tree produced by MMADLParser#body.
    def exitBody(self, ctx:MMADLParser.BodyContext):
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


    # Enter a parse tree produced by MMADLParser#composite_operator.
    def enterComposite_operator(self, ctx:MMADLParser.Composite_operatorContext):
        pass

    # Exit a parse tree produced by MMADLParser#composite_operator.
    def exitComposite_operator(self, ctx:MMADLParser.Composite_operatorContext):
        pass


    # Enter a parse tree produced by MMADLParser#newline.
    def enterNewline(self, ctx:MMADLParser.NewlineContext):
        pass

    # Exit a parse tree produced by MMADLParser#newline.
    def exitNewline(self, ctx:MMADLParser.NewlineContext):
        pass



del MMADLParser