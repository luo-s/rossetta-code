# integer partition problem: https://en.wikipedia.org/wiki/Integer_partition

# Given a positive integer n, how many ways of writing n as a sum of positive integers.

############################################################

# dynamic programming
# let p(k, n) = # of ways to form n using number <= k
    # 1) not use k: p(k-1, n)
    # 2) use k: p(k, n-k)
# thus, p(k, n) = p(k-1, n) + p(k, n-k)

# let dp[i] be the number of ways to form i (we need dp[n])
# dp[i] = p(i, i) = # of ways to form i using number <= i

# 1. start with dp[0] = 1
# 2. for each interger k = 1, 2, ..., n:
    # for each sum k <= s <= n, we can either
        # 1) not use k: dp[s] stays the same
        # 2) use k: dp[s] += dp[s-k] (add k to each method to make sum s - k)
# 3. k in ascending order ensures no duplication of partition counts.
    # s in ascending order allows the same k to be used multiple times.
    # If you reversed the inner loop to go in descending order, then each k could be used at most once. That would be a different problem: partitions into distinct parts only.

def partition(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1
    # Ensures parts are added in non-decreasing order, so no duplicate partitions.
    for k in range(1, n + 1):
        for s in range(k, n + 1):
            dp[s] += dp[s - k]
    return dp[n]

