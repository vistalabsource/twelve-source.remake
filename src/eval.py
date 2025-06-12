from antlr4 import *
from Lexer_Parser.twelveLexer import twelveLexer
from Lexer_Parser.twelveParser import twelveParser
from Lexer_Parser.twelveVisitor import twelveVisitor

class EvalVisitor(twelveVisitor):

    def visitPrintl(self, ctx:twelveParser.PrintlContext):
        code = ctx.EXPR().getText()
        content = code[1:-1]
        print(content)
        return None