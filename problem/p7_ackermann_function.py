# The Ackermann function is a classic example of a recursive function, notable especially because it is not a primitive recursive function. It grows very quickly in value, as does the size of its call tree.

# The Ackermann function is usually defined as follows:

# A(m,n) =
#   n + 1                   if m == 0
#   A(m - 1, 1)             if m > 0 and n == 0
#   A(m - 1, A(m, n - 1))   if m > 0 and n > 0
 

# Its arguments are never negative and it always terminates.

# Write a function which returns the value of A(m,n). Arbitrary precision is preferred (since the function grows so quickly), but not required.

############################################################
def ack(m, n):
    # base case
    if m == 0: return n + 1
    # resursive case
    if m > 0 and n == 0: return ack(m - 1, 1)
    if m > 0 and n > 0: return ack(m - 1, ack(m, n - 1))

############################################################
# memoization
def ack(m, n):
    memo = {}

    def helper(m, n):
        if (m, n) in memo:
            return memo[(m, n)]
        if m == 0:
            val = n + 1
        elif n == 0:
            val = helper(m - 1, 1)
        else:
            val = helper(m - 1, helper(m, n - 1))
        memo[(m, n)] = val
        return val

    return helper(m, n)

# another version of memoization
def ack(m, n):
    
    def helper(m, n, memo):
        if (m, n) in memo:
            return memo[(m, n)]
        if m == 0:
            memo[(m, n)] = n + 1
        elif n == 0:
            memo[(m, n)] = helper(m - 1, 1, memo)
        else:
            memo[(m, n)] = helper(m - 1, helper(m, n - 1, memo), memo)
        return memo[(m, n)]
    
    return helper(m, n, {})

############################################################
# we can not guarantee m, n in range, so we cannot using tabulation dp here.