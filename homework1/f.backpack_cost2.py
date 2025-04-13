n, m = map(int, input().split())
weights = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if weights[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + costs[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

res = []
i, j = n, m
while i > 0 and j > 0:
    if dp[i][j] != dp[i - 1][j]:
        res.append(i)
        j -= weights[i - 1]
    i -= 1

for item in sorted(res):
    print(item)
