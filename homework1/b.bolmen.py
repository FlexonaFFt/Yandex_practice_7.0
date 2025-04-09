class Solution:
    def main(self):
        t = int(input())
        for i in range(t):
            n = int(input())
            a = list(map(int, input().split()))

            res, segment_len, max_in_segment = 0, 0, 0
            for num in a:
                segment_len += 1
                if num > max_in_segment:
                    max_in_segment = num
                if max_in_segment == segment_len:
                    res += 1
                    segment_len, max_in_segment = 0, 0
            print(res)


def main():
    solve = Solution()
    print(solve.main())

if __name__ == '__main__':
    main()
