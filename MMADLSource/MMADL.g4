grammar MMADL;

programm
    : (header)? body
    ;

header
    : require input_params newline ensure output_params
    ;

require
    : INPUT
    ;
input_params
    : (param_name COLON param_type COMMA?)*
    ;

ensure
    : OUTPUT
    ;
output_params
    : (param_type COMMA?)*
    ;

param_name
    : STRING
    ;
param_type
    : STRING
    ;

body
    : (operators_list
    | comment
    | newline)*
    ;

comment
    : STRING
    ;

operators_list
    : operator (SEMICOLON operator)*
    ;

operator
    : simple_operator
    | composite_operator
    ;

simple_operator
    : assignment_operator
    | control_operator
    | var_definition_operator
    | expression
    ;
assignment_operator
    : param_name param_type? ASSIGNMENT expression
    ;
control_operator
    : exit_operator
    | loop_control_operator
    ;
var_definition_operator
    : param_name COLON param_type
    ;
expression
    : math_expression
    | function_call
    ;

exit_operator
    : (RETURN | YIELD) (expression COMMA?)*
    ;
loop_control_operator
    : CONTINUE
    | BREAK
    ;

math_expression
    : MATH_EXPRESSION_SIGN STRING MATH_EXPRESSION_SIGN
    ;
function_call
    : STRING variables_list
    ;

variables_list
    : (param_name COMMA?)*
    ;

composite_operator
    : STRING
    ;

newline
    : NEWLINE
    ;





NEWLINE
    : '\r'? '\n'
    ;

STRING
    : [A-Za-z][A-Za-z0-9]*
    ;

INPUT
    : 'Input'
    ;
OUTPUT
    : 'Output'
    ;

RETURN
    : 'return'
    ;
YIELD
    : 'yield'
    ;

CONTINUE
    : 'continue'
    ;
BREAK
    : 'break'
    ;

MATH_EXPRESSION_SIGN
    : '$'
    ;

COMMA
    : ','
    ;
COLON
    : ':'
    ;
SEMICOLON
    : ';'
    ;

ASSIGNMENT
    : '<-'
    ;
