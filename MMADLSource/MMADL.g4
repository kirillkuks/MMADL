grammar MMADL;

mmadl
    : header? body
    ;

header
    : require input_params ensure output_params
    ;

require
    : INPUT
    ;
input_params
    : (param_name COLON param_type)? (COMMA param_name COLON param_type)*
    ;

ensure
    : OUTPUT
    ;
output_params
    : param_type? (COMMA param_type)*
    ;

param_name
    : STRING
    ;
param_type
    : POINTER* STRING
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
    : param_name param_type? ASSIGNMENT (param_name | expression)
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
    | known_lexem
    | function_call
    ;

exit_operator
    : (RETURN | YIELD) (exit_value COMMA?)*
    ;
exit_value
    : expression
    | condition
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
    : STRING OPENPARENTHESIS variables_list CLOSEPARENTHESIS
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
    (ELSE body)?
    ENDIF
    ;
loop_operator
    : for_operator
    | while_operator
    ;

for_operator 
    : FOR for_range DO
    body
    ENDFOR
    ;
while_operator
    : WHILE condition DO
    body
    ENDWHILE
    ;

for_range
    : include
    | iteration
    ;

include
    : param_name IN math_expression
    ;
iteration
    : param_name FROM math_expression (TO | DOWNTO) math_expression
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

INPUT
    : '\u0412\u0445\u043E\u0434:'
    ;
OUTPUT
    : '\u0412\u044B\u0445\u043E\u0434:'
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
ELSE
    : 'else'
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

FROM
    : 'from'
    ;
TO
    : 'to'
    ;
DOWNTO
    : 'downto'
    ;

IN
    : 'in'
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

NUMBER
    : [1-9][0-9]*
    | [0]
    ;
STRING
    : [A-Za-z][A-Za-z0-9_.]*
    ;
CUSTOM_STRING
    : [a-zA-Z0-9\u0410-\u042F\u0430-\u044F]+
    ;
