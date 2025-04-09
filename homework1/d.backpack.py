# PE
class Solution:
    def algorithm(self, n: int, m: int, masses: list[int]) -> int:
        '''rez, masses = 0, sorted(masses)
        first_iteration = m // masses[0]
        first_ostatok = m % masses[0]
        rez += first_iteration
        ostatok_ot_m = m - first_iteration

        for i in range(1, len(masses)):
            second_iteration = ostatok_ot_m // masses[i]'''

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
        print(max_weight)

def main():
    solution = Solution()
    n, m = list(map(int, input().split()))
    spisok = list(map(int, input().split()))
    print(solution.algorithm(n, m, spisok))

def test():
    solution = Solution()
    print(solution.algorithm(1, 5968, [18]))

if __name__ == '__main__':
    main()
