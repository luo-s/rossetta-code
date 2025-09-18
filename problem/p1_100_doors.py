# There are 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, visit every door and 'toggle' the door (if the door is closed, open it; if it is open, close it). The second time, only visit every 2nd door (i.e., door #2, #4, #6, ...) and toggle it. The third time, visit every 3rd door (i.e., door #3, #6, #9, ...), etc., until you only visit the 100th door.

# Implement a function to determine the state of the doors after the last pass. Return the final result in an array, with only the door number included in the array if it is open.

############################################################
# the state of doors depends on the total number of divisors its number has
# if n = p1 ^ n1 * p2 ^ n2 * ... * pn ^ nn
# the total number of divisors d(n) = (n1 + 1)(n2 + 1)...(nn + 1)
import math
def getFinalOpenedDoors():
    doors = []
    for i in range(1, 101):
        if factors_count(i) % 2:
            doors.append(i)
    return doors

from collections import Counter
def factors_count(n):
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    total = 1
    for p, i in Counter(factors).items():
        total *= (i + 1)
    print(total)
    return total

############################################################
# A door is toggled once for every divisor its number has. Most numbers have divisors in # pairs, which the door will be toggled even numbers of times -> closed
# Only perfect squares have an odd number of divisors. Thus the answer is a list of perfect square numbers do not exceed 100.
def getFinalOpenedDoors():
    i = 1
    doors = []
    while i * i <= 100:
        doors.append(i * i)
        i += 1
    return doors