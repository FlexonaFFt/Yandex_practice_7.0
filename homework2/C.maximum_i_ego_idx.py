class Solution:
    def mathFunctions(self, otrezok: list[int], intervals: list[list[int]]):
        size = 1
        while size < len(otrezok):
            size <<= 1
        seg_max = [-float('inf')] * (2 * size)
        seg_idx = [-1] * (2 * size)
        for i in range(len(otrezok)):
            seg_max[size + i] = otrezok[i]
            seg_idx[size + i] = i
        for i in range(size - 1, 0, -1):
            left_max = seg_max[2 * i]
            right_max = seg_max[2 * i + 1]
            if left_max > right_max:
                seg_max[i] = left_max
                seg_idx[i] = seg_idx[2 * i]
            else:
                seg_max[i] = right_max
                seg_idx[i] = seg_idx[2 * i + 1]

        def query(l, r):
            l += size
            r += size
            res_max = -float('inf')
            res_idx = -1
            while l < r:
                if l % 2 == 1:
                    current_max = seg_max[l]
                    current_idx = seg_idx[l]
                    if current_max > res_max:
                        res_max = current_max
                        res_idx = current_idx
                    l += 1
                if r % 2 == 1:
                    r -= 1
                    current_max = seg_max[r]
                    current_idx = seg_idx[r]
                    if current_max > res_max:
                        res_max = current_max
                        res_idx = current_idx
                l //= 2
                r //= 2
            return (res_max, res_idx + 1)

        output = []
        for interval in intervals:
            l, r = interval[0] - 1, interval[1] - 1
            max_val, idx = query(l, r + 1)
            output.append(f"{max_val} {idx}")
        print("\n".join(output))

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
