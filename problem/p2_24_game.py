# The 24 Game tests a person's mental arithmetic.

# The aim of the game is to arrange four numbers in a way that when evaluated, the result is 24.

# Implement a function that takes a string of four digits as its argument, with each digit from 1 to 9 (inclusive) with repetitions allowed, and returns an arithmetic expression that evaluates to the number 24. If no such solution exists, return "no solution exists".

# Rules:

# Only the following operators/functions are allowed: multiplication, division, addition, subtraction.
# Division should use floating point or rational arithmetic, etc, to preserve remainders.
# Forming multiple digit numbers from the supplied digits is disallowed. (So an answer of 12+12 when given 1, 2, 2, and 1 is wrong).
# The order of the digits when given does not have to be preserved.

############################################################

# brute force: we have 4 single-digit numbers and 4 kinds of operations. We can use 4 numbers (in any order) and 3 any operators (with parentheses) to get 24. 

# So we need to check 
# 1) the permutation of 4 numbers (4! = 24 possible ways)
# 2) the permutation of 3 operators (4 ^ 3 = 64 possible ways)
# 3) all possible parentheses (operators order) (5 possible ways)
# if we got 24, add the solution to collection, and return all solutions at end; if at last we cannot find a solution, return a message.

# other consideration: use fractions library to avoid floating-point rounding errors.
from fractions import Fraction
from itertools import permutations

def solve24(digits):
    if len(digits) != 4 or any(c < '1' or c > '9' for c in digits):
        raise ValueError("Input must be a string of four digits 1–9.")

    nums = [int(c) for c in digits]
    solutions = set()

    # permutation 4 digits (24 ways); wrap in tuple: (value, expression, is_atom)
    # is_atom: True - don't need parentheses' False - need to add parentheses
    for a, b, c, d in set(permutations(nums)):
        A = (Fraction(a, 1), str(a), True)
        B = (Fraction(b, 1), str(b), True)
        C = (Fraction(c, 1), str(c), True)
        D = (Fraction(d, 1), str(d), True)

        # 1: (((A ? B) ? C) ? D)
        for AB in _combine_two(A, B):
            for ABC in _combine_two(AB, C):
                for ABCD in _combine_two(ABC, D):
                    if _equals_24(ABCD[0]):
                        solutions.add(ABCD[1])

        # 2: ((A ? (B ? C)) ? D)
        for BC in _combine_two(B, C):
            for ABC in _combine_two(A, BC):
                for ABCD in _combine_two(ABC, D):
                    if _equals_24(ABCD[0]):
                        solutions.add(ABCD[1])

        # 3: (A ? ((B ? C) ? D))
        for BC in _combine_two(B, C):
            for BCD in _combine_two(BC, D):
                for ABCD in _combine_two(A, BCD):
                    if _equals_24(ABCD[0]):
                        solutions.add(ABCD[1])

        # 4: (A ? (B ? (C ? D)))
        for CD in _combine_two(C, D):
            for BCD in _combine_two(B, CD):
                for ABCD in _combine_two(A, BCD):
                    if _equals_24(ABCD[0]):
                        solutions.add(ABCD[1])

        # 5: ((A ? B) ? (C ? D))
        for AB in _combine_two(A, B):
            for CD in _combine_two(C, D):
                for ABCD in _combine_two(AB, CD):
                    if _equals_24(ABCD[0]):
                        solutions.add(ABCD[1])

    return sorted(solutions)

# construct the operators logic: (symbol, logic, commutative)
OPS = [
    ('+', lambda x, y: x + y, True),
    ('-', lambda x, y: x - y, False),
    ('*', lambda x, y: x * y, True),
    ('/', lambda x, y: x / y if y != 0 else None, False),
]

# apply operation on two digits 
# ops are wrapped in tuples: (symbol, logic, commutative)
# digits are wrapped in tuples: (value, expression, is_atom)
# return new tuple: (value, expression, is_atom)
def _apply(op, x, y):
    sym, fn, _ = op
    out = fn(x[0], y[0])
    if out is None:
        return None
    # add parentheses to composite parts
    sx = x[1] if x[2] else f"({x[1]})"
    sy = y[1] if y[2] else f"({y[1]})"
    return (out, f"{sx}{sym}{sy}", False)

# the real calculation process
def _combine_two(x, y):
    seen_commutative = set()
    for op in OPS:
        sym, _, comm = op
        if comm:
            # prune duplicates for + and *
            key = (sym, tuple(sorted([x[1], y[1]])))
            if key in seen_commutative:
                continue
            seen_commutative.add(key)
            res = _apply(op, x, y)
            if res is not None:
                yield res
        else:
            # for - and /, try both orders
            for a, b in ((x, y), (y, x)):
                res = _apply(op, a, b)
                if res is not None:
                    yield res

def _equals_24(frac):
    return frac == Fraction(24, 1)

############################################################

# If we relax the requirement so that instead of generating all solutions, we only need to check whether a solution exists, we can simplify the code significantly.

# depth-first search (DFS) recursion

from fractions import Fraction
def judgePoint24(digits):
    
    if len(digits) != 4 or any(c < '1' or c > '9' for c in digits):
        raise ValueError("Input must be a string of four digits 1–9.")
    cards = [int(c) for c in digits]
    
    def dfs(cards):
        n = len(cards)
        # base case
        if n == 1:
            return cards[0] == 24

        # loop all pairs of 2 cards, x=cards[i] 和 y=cards[j]
        for i, x in enumerate(cards):
            for j in range(i + 1, n):
                y = cards[j]
                # generate all possible result (max 6 possibilities)
                candidates = [x + y, x - y, y - x, x * y]
                if y:  # y cannot be 0 for x / y
                    candidates.append(x / y)
                if x:  # x cannot be 0 for y / x
                    candidates.append(y / x)
                # recurse with a reduced set of numbers
                new_cards = cards[:j] + cards[j + 1:]  # delete cards[j]
                for res in candidates:
                    new_cards[i] = res  # overwrite cards[i]
                    if dfs(new_cards):
                        return True
        return False

    return dfs([Fraction(x) for x in cards])
