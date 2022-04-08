from antlr4 import *


class TexTable:
    def __init__(self) -> None:
        self.table = {
            '\\pointer' : '\\uparrow',
            '<\\cb>' : '/*',
            '<\\ce>' : '*/',
            '<-' : '\\leftarrow',
            '=' : '=',
            '!=' : '\\neq',
            '>' : '>',
            '<' : '<',
            '>=' : '\\geq',
            '<=' : '\\leq'
        }

    def getToken(self, token: TerminalNode) -> str:
        s = token.__str__()
        assert s in self.table

        return self.table[s]
