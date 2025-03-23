def func(grid, N, M):
    dp = [[0] * M for _ in range(N)]
    dp[0][0] = grid[0][0]

    for j in range(1, M):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    path = []
    i, j = N - 1, M - 1
    while i > 0 or j > 0:
        if i > 0 and (j == 0 or dp[i - 1][j] > dp[i][j - 1]):
            path.append("D")
            i -= 1
        else:
            path.append("R")
            j -= 1

    path.reverse()
    print(dp[N - 1][M - 1])
    ans_path = ' '.join(path)
    print(ans_path)


def main():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):  # Исправлено здесь
        layer = list(map(int, input().split()))
        grid.append(layer)
    func(grid, n, m)

main()
