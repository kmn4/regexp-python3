# Generated from Regex.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RegexParser import RegexParser
else:
    from RegexParser import RegexParser

# This class defines a complete generic visitor for a parse tree produced by RegexParser.

class RegexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RegexParser#Alt.
    def visitAlt(self, ctx:RegexParser.AltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#Cat.
    def visitCat(self, ctx:RegexParser.CatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#Par.
    def visitPar(self, ctx:RegexParser.ParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#Chr.
    def visitChr(self, ctx:RegexParser.ChrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#Rep.
    def visitRep(self, ctx:RegexParser.RepContext):
        return self.visitChildren(ctx)



del RegexParser