class Solution:
    def three_ones(self, n: int) -> int:
        if n == 0:
            return 0

        dp = [[0] * 3 for _ in range(n+1)]
        dp[1][0] = 1
        dp[1][1] = 1
        dp[1][2] = 0

        for i in range(2, n + 1):
            dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
            dp[i][1] = dp[i-1][0]
            dp[i][2] = dp[i-1][1]
        return dp[n][0] + dp[n][1] + dp[n][2]


def main():
    solution = Solution()
    n = int(input())
    print(solution.three_ones(n=n))

main()
