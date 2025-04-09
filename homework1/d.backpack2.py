def algorithm(n: int, m: int, masses: list[int]) -> int:
    dp = [False] * (m + 1)
    dp[0], max_weight = True, 0

    for weight in masses:
        for j in range(m, weight - 1, -1):
            if dp[j - weight]:
                dp[j] = True

    for j in range(m, -1, -1):
        if dp[j]:
            max_weight = j
            break

    return max_weight

def main():
    n, m = map(int, input().split())
    spisok = list(map(int, input().split()))
    print(algorithm(n, m, spisok))

main()
