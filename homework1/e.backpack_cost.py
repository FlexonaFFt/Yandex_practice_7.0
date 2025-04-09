def algorithm(n: int, m: int, masses: list[int], costs: list[int]) -> int:
    dp = [0] * (m + 1)
    for i in range(n):
        weight, cost = masses[i], costs[i]
        for j in range(m, weight - 1, -1):
            if dp[j - weight] + cost > dp[j]:
                dp[j] = dp[j - weight] + cost
    return max(dp)


def main():
    n, m = map(int, input().split())
    masses = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    print(algorithm(n, m, masses, costs))

main()
