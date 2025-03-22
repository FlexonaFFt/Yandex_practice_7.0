class Solution:
    # Для решения задачи буду использовать динамическое программирование
    def ticket_choose(self, n: int, tickets: list[list[int]]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        if n >= 1:
            dp[1] = tickets[0][0]
        if n >= 2:
            dp[2] = min(dp[1] + tickets[1][0], dp[0] + tickets[0][1])
        if n >= 3:
            dp[3] = min(dp[2] + tickets[2][0], dp[1] + tickets[1][1], dp[0] + tickets[0][2])

        for i in range(4, n + 1):
            dp[i] = min(
                dp[i-1] + tickets[i-1][0],
                dp[i-2] + tickets[i-2][1],
                dp[i-3] + tickets[i-3][2]
            )

        return dp[n] # type: ignore


def main():
    solution = Solution()
    n = int(input())
    tickets = []
    for _ in range(n):
        tick = list(map(int, input().split()))
        tickets.append(tick)
    print(solution.ticket_choose(n=n, tickets=tickets))

main()
