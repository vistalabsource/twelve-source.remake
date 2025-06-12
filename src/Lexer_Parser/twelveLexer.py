# Generated from grammar/twelve.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,4,34,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,1,1,1,1,2,1,2,1,
        3,4,3,29,8,3,11,3,12,3,30,1,3,1,3,0,0,4,1,1,3,2,5,3,7,4,1,0,2,2,
        0,10,10,13,13,3,0,9,10,13,13,32,32,35,0,1,1,0,0,0,0,3,1,0,0,0,0,
        5,1,0,0,0,0,7,1,0,0,0,1,9,1,0,0,0,3,16,1,0,0,0,5,25,1,0,0,0,7,28,
        1,0,0,0,9,10,5,112,0,0,10,11,5,114,0,0,11,12,5,105,0,0,12,13,5,110,
        0,0,13,14,5,116,0,0,14,15,5,108,0,0,15,2,1,0,0,0,16,20,5,34,0,0,
        17,19,8,0,0,0,18,17,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,0,20,21,1,
        0,0,0,21,23,1,0,0,0,22,20,1,0,0,0,23,24,5,34,0,0,24,4,1,0,0,0,25,
        26,5,59,0,0,26,6,1,0,0,0,27,29,7,1,0,0,28,27,1,0,0,0,29,30,1,0,0,
        0,30,28,1,0,0,0,30,31,1,0,0,0,31,32,1,0,0,0,32,33,6,3,0,0,33,8,1,
        0,0,0,3,0,20,30,1,6,0,0
    ]

class twelveLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PRINTL = 1
    EXPR = 2
    SEMI = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'printl'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "PRINTL", "EXPR", "SEMI", "WS" ]

    ruleNames = [ "PRINTL", "EXPR", "SEMI", "WS" ]

    grammarFileName = "twelve.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


