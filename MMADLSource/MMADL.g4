grammar MMADL;

mmadl
    : (header)? body
    ;

header
    : require input_params ensure output_params
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
    : POINTER? STRING
    ;

body
    : (operators_list
    | comment)*
    ;

comment
    : OPENCOMMENT CUSTOM_STRING CLOSECOMMENT
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
    | known_lexem
    ;

exit_operator
    : (RETURN | YIELD) (expression COMMA?)*
    ;
loop_control_operator
    : CONTINUE
    | BREAK
    ;

math_expression
    : (MATH_EXPRESSION_SIGN STRING MATH_EXPRESSION_SIGN)
    | NUMBER
    ;
function_call
    : STRING variables_list
    ;

variables_list
    : (param_name COMMA?)*
    ;

known_lexem
    : bool_value
    | NIL
    ;
bool_value
    : FALSE
    | TRUE
    ;

composite_operator
    : if_operator
    | loop_operator
    ;
if_operator
    : IF condition THEN 
    body
    (ELSEIF condition THEN
    body)*
    ENDIF
    ;
loop_operator
    : (WHILE condition DO
    body
    ENDWHILE)
    | (FOR condition DO
    body
    ENDFOR)
    ;

condition
    : simple_condition (logic_connective simple_condition)*
    ;
simple_condition
    : (OPENPARENTHESIS condition CLOSEPARENTHESIS)
    | (bool_value | math_expression | order_relation)
    ;
logic_connective
    : AND
    | OR
    | BYTEAND
    | BYTEOR
    | XOR
    ;

order_relation
    : (param_name | expression) binary_relation (param_name | expression)
    ;
binary_relation
    : EQ
    | NEQ
    | GT
    | LE
    | GEQ
    | LEQ
    ;

NUMBER
    : [1-9][0-9]*
    | [0]
    ;
STRING
    : [A-Za-z][A-Za-z0-9_]*
    ;
CUSTOM_STRING
    : ~[$]
    ;

INPUT
    : '\u0412\u0425\u041E\u0414:'
    ;
OUTPUT
    : '\u0412\u042B\u0425\u041E\u0414:'
    ;

IF
    : 'if'
    ;
THEN
    : 'then'
    ;
ELSEIF
    : 'elseif'
    ;
ENDIF
    : 'end if'
    ;

WHILE
    : 'while'
    ;
ENDWHILE
    : 'end while'
    ;
FOR
    : 'for'
    ;
ENDFOR
    : 'end for'
    ;
DO
    : 'do'
    ;

NIL
    : 'nil'
    ;
FALSE
    : 'False'
    ;
TRUE
    : 'True'
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

OPENPARENTHESIS
    : '('
    ;
CLOSEPARENTHESIS
    : ')'
    ;

AND
    : 'and'
    ;
OR
    : 'or'
    ;
BYTEAND
    : '&'
    ;
BYTEOR
    : '|'
    ;
XOR
    : 'xor'
    ;

EQ
    : '='
    ;
NEQ
    : '!='
    ;
GT
    : '>'
    ;
LE
    : '<'
    ;
GEQ
    : '>='
    ;
LEQ
    : '<='
    ;

POINTER
    : '\\pointer'
    ;

OPENCOMMENT
    : '<\\cb>'
    ;
CLOSECOMMENT
    : '<\\ce>'
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
