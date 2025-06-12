# Generated from grammar/twelve.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .twelveParser import twelveParser
else:
    from twelveParser import twelveParser

# This class defines a complete generic visitor for a parse tree produced by twelveParser.

class twelveVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by twelveParser#program.
    def visitProgram(self, ctx:twelveParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twelveParser#statement.
    def visitStatement(self, ctx:twelveParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by twelveParser#printl.
    def visitPrintl(self, ctx:twelveParser.PrintlContext):
        return self.visitChildren(ctx)



del twelveParser