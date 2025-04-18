class Solution:
    def mathFunctions(self, otrezok: list[int], intervals: list[list[int]]):
        answer = []

        for interval in intervals:
            counter, variable = 0, 0
            i, j = interval[0], interval[1]
            for element in otrezok[i - 1: j]:
                if element > variable:
                    variable = element
                    counter = 1

                elif element == variable:
                    counter += 1

            answer.append([variable, counter])

        for block in answer:
            print(*block)

# Решение не проходит 6 тест, TL
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
