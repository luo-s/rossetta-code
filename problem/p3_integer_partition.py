# integer partition problem: https://en.wikipedia.org/wiki/Integer_partition

# Given a positive integer n, how many ways of writing n as a sum of positive integers.

############################################################

# dynamic programming
# let dp[i] be the number of ways of writing i
# dp[s] += dp[s-k]
# thus dp[s] = dp[]
def partition(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1
    for k in range(1, n + 1):
        for s in range(k, n + 1):
            dp[s] += dp[s - k]
    return dp[n]

