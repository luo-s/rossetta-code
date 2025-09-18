# The 24 Game tests a person's mental arithmetic.

# The aim of the game is to arrange four numbers in a way that when evaluated, the result is 24

# Implement a function that takes a string of four digits as its argument, with each digit from 1 to 9 (inclusive) with repetitions allowed, and returns an arithmetic expression that evaluates to the number 24. If no such solution exists, return "no solution exists".

# Rules:

# Only the following operators/functions are allowed: multiplication, division, addition, subtraction.
# Division should use floating point or rational arithmetic, etc, to preserve remainders.
# Forming multiple digit numbers from the supplied digits is disallowed. (So an answer of 12+12 when given 1, 2, 2, and 1 is wrong).
# The order of the digits when given does not have to be preserved.

############################################################
# approach: we have 4 single-digit numbers and 4 kinds of operations. We can use 4 numbers (in any order) and 3 any operators (with parentheses) to get 24. 
# So we need to check 
# 1) the permutation of 4 numbers (4! = 24 possible ways)
# 2) the permutation of 3 operators (4 ^ 3 = 64 possible ways)
# 3) all possible parentheses (operators order) (5 possible ways)
# if we got 24, return the solution; if at last we cannot find a solution, return a message.
# other considerations
def solve24(digits):
    if len(digits) != 4 or any(c < '1' or c > '9' for c in digits):
        raise ValueError("Input must be a string of four digits 1–9.")

    nums = [int(c) for c in digits]
    