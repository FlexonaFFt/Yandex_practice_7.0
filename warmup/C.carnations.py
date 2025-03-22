def minimal(n: int, coordinates: list[int]) -> int:
    coordinates.sort()
    dp = [0] * (n + 1)
    dp[1] = 0
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + (coordinates[i - 1] - coordinates[i - 2]),
            dp[i - 2] + (coordinates[i - 1] - coordinates[i - 2]))
    return dp[n]


def main():
    n = int(input())
    coords = list(map(int, input().split()))
    print(minimal(n=n, coordinates=coords))

if __name__ == '__main__':
    main()
