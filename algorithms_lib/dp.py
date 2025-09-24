from typing import List
def lis_length(nums: List[int]) -> int:
    import bisect
    tails = []
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails): tails.append(x)
        else: tails[i] = x
    return len(tails)
def coin_change(coins: List[int], amount: int) -> int:
    dp = [amount+1]*(amount+1); dp[0]=0
    for c in coins:
        for x in range(c, amount+1):
            dp[x] = min(dp[x], dp[x-c]+1)
    return dp[amount] if dp[amount]!=amount+1 else -1
def edit_distance(a: str, b: str) -> int:
    m,n = len(a), len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0]=i
    for j in range(n+1): dp[0][j]=j
    for i in range(1,m+1):
        for j in range(1,n+1):
            cost = 0 if a[i-1]==b[j-1] else 1
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+cost)
    return dp[m][n]
