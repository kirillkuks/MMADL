grammar MMADL;

mmadl
    : header? body
    ;

header
    : require input_params end_of_line*
    ensure output_params end_of_line*
    ;

require
    : INPUT
    ;
input_params
    : (param_name colon param_type comment?)? (comma param_name colon param_type comment?)*
    ;

ensure
    : OUTPUT
    ;
output_params
    : param_type? comment? (comma param_type comment?)*
    ;

param_name
    : STRING (index)*
    ;

param_type
    : POINTER* STRING
    ;

index
    : OPENBRACKET indexed_expression CLOSEBRACKET
    ;

indexed_expression
    : param_name
    | expression
    ;

body
    : (operators_list
    | comment
    | end_of_line)*
    ;

end_of_line
    : EOL
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
    | param_name
    ;
loop_control_operator
    : CONTINUE
    | BREAK
    ;

math_expression
    : math_string
    | number
    ;

math_string
    : MATH_STRING
    ;

number
    : NUMBER
    ;

function_call
    : param_name OPENPARENTHESIS variables_list CLOSEPARENTHESIS
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
    : for_symbol for_range do_symbol
    body
    endfor_symbol
    ;
for_symbol
    : FOR
    ;
endfor_symbol
    : ENDFOR
    ;

while_operator
    : while_symbol condition do_symbol
    body
    endwhile_symbol
    ;
while_symbol
    : WHILE
    ;

do_symbol
    : DO
    ;

endwhile_symbol
    : ENDWHILE
    ;

for_range
    : include
    | iteration
    ;

include
    : param_name IN math_expression
    ;
iteration
    : param_name from_symbol iteration_elem iteration_end iteration_elem
    ;

from_symbol
    : FROM
    ;

iteration_end
    : TO
    | DOWNTO
    ;

iteration_elem
    : math_expression
    | param_name
    ;

condition
    : simple_condition (logic_connective simple_condition)*
    ;
simple_condition
    : (OPENPARENTHESIS condition CLOSEPARENTHESIS)
    | (bool_value | math_expression | order_relation | include)
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

colon
    : COLON
    ;
comma
    : COMMA
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

OPENBRACKET
    : '['
    ;

CLOSEBRACKET
    : ']'
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

EOL
    : '\n'
    ;

WS
    : [ \t\r]+ -> skip
    ;

NUMBER
    : [1-9][0-9]*
    | [0]
    ;
STRING
    : [A-Za-z0-9][A-Za-z0-9_.]*
    ;
CUSTOM_STRING
    : [a-zA-Z0-9\u0410-\u042F\u0430-\u044F]+
    ;
MATH_STRING
    : '$'(
        'a' .. 'z'
        | 'A' .. 'Z'
        | '0' .. '9'
        | '+' | '-' | '*' | '%' | '\\'
        | ' '
        | '[' | ']' | '(' | ')'
    )*'$'
    ;