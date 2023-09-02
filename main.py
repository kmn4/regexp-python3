from functools import reduce
from typing import Callable, List, Set

# automata

class Automaton:
    def __init__(self, n_states: int, transition: List[Callable[[str], Set[int]]], eps_transition: List[Set[int]], initial_state: int, accepting_state: int) -> None:
        self.initial_state = initial_state
        self.accepting_state = accepting_state
        self.n_states = n_states
        self.transition = transition
        self.eps_transition = eps_transition
        self._closure_set = self._fix_closure()

    def _fix_closure(self):
        prev = [set() for i in range(0, self.n_states)]
        closure = [{i} for i in range(0, self.n_states)]
        # TODO: fixing closure one by one might be faster
        while closure != prev:
            prev = closure
            # Scala-style equivalent: closure.map(x => x.flatMap(i => self.eps_transition[i]))
            step_eps = lambda x : reduce(lambda acc, i : acc | self.eps_transition[i], x, set())
            closure = [x | step_eps(x) for x in closure]
        return closure

    def _closure(self, states):
        # ネストした集合は作れない (set が hashable じゃないから) ので、
        # _closure_set の適用と平坦化を同時に行っている。
        return reduce(lambda acc, i : acc | self._closure_set[i], states, set())

    def _step(self, current_states, char):
        hop = reduce(lambda acc, i: acc | self.transition[i](char), current_states, set())
        return self._closure(hop)

    def _iterate(self, current_states, word):
        if len(word) == 0: return current_states
        head = word[0]
        tail = word[1:]
        return self._iterate(self._step(current_states, head), tail)

    def accepts(self, word) -> bool:
        initial = self._closure({self.initial_state})
        reached_states = self._iterate(initial, word)
        return self.accepting_state in reached_states

# regex

class Regex:
    def compile(self):
        return Compile().apply(self)
    
class Eps(Regex):
    def accept(self, vis):
        return vis.visitEps(self)

class Chr(Regex):
    def __init__(self, letter):
        self.letter = letter

    def accept(self, vis):
        return vis.visitChr(self)

class Cat(Regex):
    def __init__(self, former, latter):
        self.former = former
        self.latter = latter

    def accept(self, vis):
        return vis.visitCat(self)

class Alt(Regex):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def accept(self, vis):
        return vis.visitAlt(self)

class Rep(Regex):
    def __init__(self, subexp):
        self.subexp = subexp

    def accept(self, vis):
        return vis.visitRep(self)

# parser

# conversion

class Compile:

    def __init__(self):
        self._bot = lambda _ : set()
        self._counter = -1

    def _new_state(self):
        self._counter += 1
        return self._counter
    
    def apply(self, exp):
        aux_dict = self._apply(exp)
        n_states = self._counter+1
        flatten = lambda mapping, default : [mapping.get(i) or default for i in range(n_states)]
        return Automaton(
            n_states,
            flatten(aux_dict["transition"], lambda c : set()),
            flatten(aux_dict["eps_transition"], set()),
            aux_dict["initial_state"],
            aux_dict["accepting_state"],
        )
    
    # compile to dictionary

    def _apply(self, exp):
        return exp.accept(self)
    
    # visitor methods

    def visitEps(self, exp):
        init = self._new_state()
        acpt = self._new_state()
        return {
            "initial_state": init,
            "accepting_state": acpt,
            "transition": {
                init: self._bot,
                acpt: self._bot,
            },
            "eps_transition": {
                init: {acpt},
                acpt: set(),
            },
        }

    def visitChr(self, exp):
        init = self._new_state()
        acpt = self._new_state()
        return {
            "initial_state": init,
            "accepting_state": acpt,
            "transition": {
                init: lambda c : {acpt} if c == exp.letter else set(),
                acpt: self._bot,
            },
            "eps_transition": {
                init: set(),
                acpt: set(),
            },
        }
    
    def visitCat(self, exp):
        aut1 = self._apply(exp.former)
        aut2 = self._apply(exp.latter)
        return {
            "initial_state": aut1["initial_state"],
            "accepting_state": aut2["accepting_state"],
            "transition": aut1["transition"] | aut2["transition"],
            # NOTE: 受理状態からの遷移は元のオートマトンに存在しないことを仮定してよい
            "eps_transition": aut1["eps_transition"] | aut2["eps_transition"] | {
                aut1["accepting_state"]: {aut2["initial_state"]}
            }
        }

    def visitAlt(self, exp):
        init = self._new_state()
        acpt = self._new_state()
        aut1 = self._apply(exp.first)
        aut2 = self._apply(exp.second)
        return {
            "initial_state": init,
            "accepting_state": acpt,
            "transition": aut1["transition"] | aut2["transition"],
            "eps_transition": aut1["eps_transition"] | aut2["eps_transition"] | {
                init: {aut1["initial_state"], aut2["initial_state"]},
                aut1["accepting_state"]: {acpt},
                aut2["accepting_state"]: {acpt},
            },
        }

    def visitRep(self, exp):
        init = self._new_state()
        acpt = self._new_state()
        aut = self._apply(exp.subexp)
        return {
            "initial_state": init,
            "accepting_state": acpt,
            "transition": aut["transition"],
            "eps_transition": aut["eps_transition"] | {
                init: {aut["initial_state"], acpt},
                aut["accepting_state"]: {acpt, aut["initial_state"]},
            },
        }

# examples

if __name__ == "__main__":
    # exp = parse("a(a|b)(ab)*")
    exp = Cat(Cat(Chr("a"), Alt(Chr("a"), Chr("b"))), Rep(Cat(Chr("a"), Chr("b"))))
    aut = exp.compile()
    assert aut.accepts("ab")
    assert aut.accepts("abab")
    assert not aut.accepts("")
    assert not aut.accepts("aba")
    assert aut.accepts("aa")
    assert not aut.accepts("aaaa")
    print("done")
