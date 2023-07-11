
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

# This is a Hard Challenge (dynamic programming algorithm)

def kSumSubset(numArray: list[int], k: int) -> bool:
    n = len(numArray)
    dp = [[False for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(k+1):
            if j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            else:
                if numArray[i-1] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-numArray[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]

    return dp[n][k]