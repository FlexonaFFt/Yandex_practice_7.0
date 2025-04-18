class Solution:
    def mathFunctions(self, otrezok: list[int], intervals: list[list[int]]):
        n, answer = len(otrezok), []
        prefix_max = [0] * n
        count_max = [0] * n

        prefix_max[0] = otrezok[0]
        count_max[0] = 1

        for i in range(1, n):
            if otrezok[i] > prefix_max[i - 1]:
                prefix_max[i] = otrezok[i]
                count_max[i] = 1
            elif otrezok[i] == prefix_max[i - 1]:
                prefix_max[i] = prefix_max[i - 1]
                count_max[i] = count_max[i - 1] + 1
            else:
                prefix_max[i] = prefix_max[i - 1]
                count_max[i] = count_max[i - 1]

        for L, R in intervals:
            L -= 1
            R -= 1

            current_max = prefix_max[R]
            if L == 0:
                cnt = prefix_max[R]
            else:
                if prefix_max[L - 1] == current_max:
                    cnt = count_max[R] - count_max[L - 1]
                elif prefix_max[L - 1] < current_max:
                    cnt = count_max[R]
                else: cnt = 0

            answer.append([current_max, cnt])
        for block in answer:
                    print(*block)

# WA 2 закрытый тест
def main():
    solution = Solution()
    n = int(input())
    otrezok = list(map(int, input().split()))
    k = int(input())
    intervals = []
    for _ in range(k):
        interval = list(map(int, input().split()))
        intervals.append(interval)

    solution.mathFunctions(otrezok=otrezok, intervals=intervals)

if __name__ == '__main__':
    main()
