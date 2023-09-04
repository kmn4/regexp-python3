# Generated from Regex.g4 by ANTLR 4.13.1
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
        4,1,5,36,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,1,5,1,16,8,1,10,1,12,1,19,9,1,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,27,8,2,1,2,1,2,5,2,31,8,2,10,2,12,2,34,9,2,1,2,0,1,4,3,0,2,4,
        0,0,36,0,6,1,0,0,0,2,17,1,0,0,0,4,26,1,0,0,0,6,11,3,2,1,0,7,8,5,
        1,0,0,8,10,3,2,1,0,9,7,1,0,0,0,10,13,1,0,0,0,11,9,1,0,0,0,11,12,
        1,0,0,0,12,1,1,0,0,0,13,11,1,0,0,0,14,16,3,4,2,0,15,14,1,0,0,0,16,
        19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,3,1,0,0,0,19,17,1,0,0,
        0,20,21,6,2,-1,0,21,22,5,3,0,0,22,23,3,0,0,0,23,24,5,4,0,0,24,27,
        1,0,0,0,25,27,5,5,0,0,26,20,1,0,0,0,26,25,1,0,0,0,27,32,1,0,0,0,
        28,29,10,3,0,0,29,31,5,2,0,0,30,28,1,0,0,0,31,34,1,0,0,0,32,30,1,
        0,0,0,32,33,1,0,0,0,33,5,1,0,0,0,34,32,1,0,0,0,4,11,17,26,32
    ]

class RegexParser ( Parser ):

    grammarFileName = "Regex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|'", "'*'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "CHAR" ]

    RULE_regex = 0
    RULE_alternative = 1
    RULE_block = 2

    ruleNames =  [ "regex", "alternative", "block" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    CHAR=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RegexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegexParser.RULE_regex

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AltContext(RegexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegexParser.RegexContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def alternative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegexParser.AlternativeContext)
            else:
                return self.getTypedRuleContext(RegexParser.AlternativeContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlt" ):
                return visitor.visitAlt(self)
            else:
                return visitor.visitChildren(self)



    def regex(self):

        localctx = RegexParser.RegexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_regex)
        self._la = 0 # Token type
        try:
            localctx = RegexParser.AltContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.alternative()
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 7
                self.match(RegexParser.T__0)
                self.state = 8
                self.alternative()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlternativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegexParser.RULE_alternative

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CatContext(AlternativeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegexParser.AlternativeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegexParser.BlockContext)
            else:
                return self.getTypedRuleContext(RegexParser.BlockContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCat" ):
                return visitor.visitCat(self)
            else:
                return visitor.visitChildren(self)



    def alternative(self):

        localctx = RegexParser.AlternativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_alternative)
        self._la = 0 # Token type
        try:
            localctx = RegexParser.CatContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==5:
                self.state = 14
                self.block(0)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegexParser.RULE_block

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParContext(BlockContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegexParser.BlockContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def regex(self):
            return self.getTypedRuleContext(RegexParser.RegexContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPar" ):
                return visitor.visitPar(self)
            else:
                return visitor.visitChildren(self)


    class ChrContext(BlockContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegexParser.BlockContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(RegexParser.CHAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChr" ):
                return visitor.visitChr(self)
            else:
                return visitor.visitChildren(self)


    class RepContext(BlockContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegexParser.BlockContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def block(self):
            return self.getTypedRuleContext(RegexParser.BlockContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRep" ):
                return visitor.visitRep(self)
            else:
                return visitor.visitChildren(self)



    def block(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RegexParser.BlockContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_block, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = RegexParser.ParContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 21
                self.match(RegexParser.T__2)
                self.state = 22
                self.regex()
                self.state = 23
                self.match(RegexParser.T__3)
                pass
            elif token in [5]:
                localctx = RegexParser.ChrContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(RegexParser.CHAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RegexParser.RepContext(self, RegexParser.BlockContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_block)
                    self.state = 28
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 29
                    self.match(RegexParser.T__1) 
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.block_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def block_sempred(self, localctx:BlockContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




