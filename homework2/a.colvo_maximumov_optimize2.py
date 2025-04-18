import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    arr = list(map(int, input[ptr:ptr+N]))
    ptr += N

    # Инициализация дерева отрезков
    size = 1
    while size < N:
        size <<= 1
    seg_max = [0] * (2 * size)
    seg_cnt = [0] * (2 * size)

    # Заполнение листьев
    for i in range(N):
        seg_max[size + i] = arr[i]
        seg_cnt[size + i] = 1
    # Построение дерева
    for i in range(size - 1, 0, -1):
        left_max = seg_max[2 * i]
        right_max = seg_max[2 * i + 1]
        if left_max > right_max:
            seg_max[i] = left_max
            seg_cnt[i] = seg_cnt[2 * i]
        elif left_max < right_max:
            seg_max[i] = right_max
            seg_cnt[i] = seg_cnt[2 * i + 1]
        else:
            seg_max[i] = left_max
            seg_cnt[i] = seg_cnt[2 * i] + seg_cnt[2 * i + 1]

    # Функция запроса
    def query(l, r):
        l += size
        r += size
        res_max = 0
        res_cnt = 0
        while l < r:
            if l % 2 == 1:
                current_max = seg_max[l]
                current_cnt = seg_cnt[l]
                if current_max > res_max:
                    res_max = current_max
                    res_cnt = current_cnt
                elif current_max == res_max:
                    res_cnt += current_cnt
                l += 1
            if r % 2 == 1:
                r -= 1
                current_max = seg_max[r]
                current_cnt = seg_cnt[r]
                if current_max > res_max:
                    res_max = current_max
                    res_cnt = current_cnt
                elif current_max == res_max:
                    res_cnt += current_cnt
            l //= 2
            r //= 2
        return (res_max, res_cnt)

    K = int(input[ptr])
    ptr += 1
    output = []
    for _ in range(K):
        l = int(input[ptr]) - 1
        r = int(input[ptr + 1]) - 1
        ptr += 2
        max_val, cnt = query(l, r + 1)
        output.append(f"{max_val} {cnt}")

    print('\n'.join(output))

if __name__ == "__main__":
    main()
