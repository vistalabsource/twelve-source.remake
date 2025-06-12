# Generated from grammar/twelve.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,4,21,2,0,7,0,2,1,7,1,2,2,7,2,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,0,0,3,0,2,4,0,0,18,0,9,1,0,0,
        0,2,14,1,0,0,0,4,16,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,11,1,0,0,0,
        9,7,1,0,0,0,9,10,1,0,0,0,10,12,1,0,0,0,11,9,1,0,0,0,12,13,5,0,0,
        1,13,1,1,0,0,0,14,15,3,4,2,0,15,3,1,0,0,0,16,17,5,1,0,0,17,18,5,
        2,0,0,18,19,5,3,0,0,19,5,1,0,0,0,1,9
    ]

class twelveParser ( Parser ):

    grammarFileName = "twelve.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'printl'", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "PRINTL", "EXPR", "SEMI", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_printl = 2

    ruleNames =  [ "program", "statement", "printl" ]

    EOF = Token.EOF
    PRINTL=1
    EXPR=2
    SEMI=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(twelveParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(twelveParser.StatementContext)
            else:
                return self.getTypedRuleContext(twelveParser.StatementContext,i)


        def getRuleIndex(self):
            return twelveParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = twelveParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 6
                self.statement()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 12
            self.match(twelveParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printl(self):
            return self.getTypedRuleContext(twelveParser.PrintlContext,0)


        def getRuleIndex(self):
            return twelveParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = twelveParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.printl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTL(self):
            return self.getToken(twelveParser.PRINTL, 0)

        def EXPR(self):
            return self.getToken(twelveParser.EXPR, 0)

        def SEMI(self):
            return self.getToken(twelveParser.SEMI, 0)

        def getRuleIndex(self):
            return twelveParser.RULE_printl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintl" ):
                return visitor.visitPrintl(self)
            else:
                return visitor.visitChildren(self)




    def printl(self):

        localctx = twelveParser.PrintlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_printl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(twelveParser.PRINTL)
            self.state = 17
            self.match(twelveParser.EXPR)
            self.state = 18
            self.match(twelveParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





