# Abundant, deficient and perfect number classifications
# These define three classifications of positive integers based on their proper divisors.

# Let P(n) be the sum of the proper divisors of n where proper divisors are all positive integers n other than n itself.

# If P(n) < n then n is classed as deficient

# If P(n) = n then n is classed as perfect

# If P(n) > n then n is classed as abundant

# Example: 6 has proper divisors of 1, 2, and 3. 1 + 2 + 3 = 6, so 6 is classed as a perfect number.

# Implement a function that calculates how many of the integers from 1 to num (inclusive) are in each of the three classes. Output the result as an array in the following format [deficient, perfect, abundant].

def getDPA(num):
    ans = [0] * 3
    for i in range(num):
        pn = sumDivisor(i)
        if pn < i:
            ans[0] += 1
        elif pn == i:
            ans[1] += 1
        else:
            ans[2] += 1
    return ans

def sumDivisor(num):
    if num == 1: return 0
    divisorSum, i = 1, 2
    while i * i <= num:
        if num % i == 0:
            divisorSum += i
            if i * i != num:
                divisorSum += num // i
        i += 1
    return divisorSum
                
    
        
