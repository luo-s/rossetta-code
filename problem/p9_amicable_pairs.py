# Two integers N and M are said to be amicable pairs if N ≠ M and the sum of the proper divisors of N equals to M as well as the sum of the proper divisors of M equals to N.

# Example:

# 1184 and 1210 are an amicable pair, with proper divisors:

# 1, 2, 4, 8, 16, 32, 37, 74, 148, 296, 592 and
# 1, 2, 5, 10, 11, 22, 55, 110, 121, 242, 605 respectively.
# The sum of the divisors for the first value, 1184, is 1210 and the sum of the divisors for the second value, 1210, is 1184.

# Calculate and show here the Amicable pairs below 20,000 (there are eight).

############################################################
# use a data structure to store the n and its sum of proper divisors (dict)

def amicablePairsUpTo(n):
    divisorMap, pairs = {}, []
    for i in range(1, n + 1):
        divisorMap[i] = sum = divisorSum(i)
        if sum in divisorMap and divisorMap[sum] == i and i != sum:
            pairs.append([sum, i])
    return pairs

def divisorSum(n):
    if n == 1: return 0
    sum, i = 1, 2
    while i * i <= n:
        if n % i == 0:
            sum += i
            if i * i != n:
                sum += n // i
        i += 1
    return sum
