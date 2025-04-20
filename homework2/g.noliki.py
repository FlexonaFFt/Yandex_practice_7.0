import sys
# WA 5
def main():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    A = list(map(int, input[ptr:ptr+N]))
    ptr += N
    M = int(input[ptr])
    ptr += 1

    # Инициализация дерева отрезков
    size = 1
    while size < N:
        size <<= 1
    tree_max = [0] * (2 * size)
    tree_left = [0] * (2 * size)
    tree_right = [0] * (2 * size)
    tree_all_zero = [False] * (2 * size)

    # Заполнение листьев
    for i in range(N):
        tree_max[size + i] = 1 if A[i] == 0 else 0
        tree_left[size + i] = 1 if A[i] == 0 else 0
        tree_right[size + i] = 1 if A[i] == 0 else 0
        tree_all_zero[size + i] = (A[i] == 0)
    # Заполнение внутренних узлов
    for i in range(size - 1, 0, -1):
        left_child = 2 * i
        right_child = 2 * i + 1
        # Обновляем tree_all_zero
        tree_all_zero[i] = tree_all_zero[left_child] and tree_all_zero[right_child]
        # Обновляем tree_left
        if tree_all_zero[left_child]:
            tree_left[i] = tree_left[left_child] + tree_left[right_child]
        else:
            tree_left[i] = tree_left[left_child]
        # Обновляем tree_right
        if tree_all_zero[right_child]:
            tree_right[i] = tree_right[left_child] + tree_right[right_child]
        else:
            tree_right[i] = tree_right[right_child]
        # Обновляем tree_max
        tree_max[i] = max(tree_max[left_child], tree_max[right_child], tree_right[left_child] + tree_left[right_child])

    def update(pos, value):
        pos += size
        tree_max[pos] = 1 if value == 0 else 0
        tree_left[pos] = 1 if value == 0 else 0
        tree_right[pos] = 1 if value == 0 else 0
        tree_all_zero[pos] = (value == 0)
        pos >>= 1
        while pos >= 1:
            left_child = 2 * pos
            right_child = 2 * pos + 1
            # Обновляем tree_all_zero
            tree_all_zero[pos] = tree_all_zero[left_child] and tree_all_zero[right_child]
            # Обновляем tree_left
            if tree_all_zero[left_child]:
                tree_left[pos] = tree_left[left_child] + tree_left[right_child]
            else:
                tree_left[pos] = tree_left[left_child]
            # Обновляем tree_right
            if tree_all_zero[right_child]:
                tree_right[pos] = tree_right[left_child] + tree_right[right_child]
            else:
                tree_right[pos] = tree_right[right_child]
            # Обновляем tree_max
            tree_max[pos] = max(tree_max[left_child], tree_max[right_child], tree_right[left_child] + tree_left[right_child])
            pos >>= 1

    def query(l, r):
        l += size
        r += size
        res = 0
        left_segments = []
        right_segments = []
        while l <= r:
            if l % 2 == 1:
                left_segments.append(l)
                l += 1
            if r % 2 == 0:
                right_segments.append(r)
                r -= 1
            l >>= 1
            r >>= 1
        segments = left_segments + right_segments[::-1]
        # Обрабатываем сегменты
        current_max = 0
        current_left = 0
        prev_right = 0
        for node in segments:
            current_max = max(current_max, tree_max[node])
            if tree_all_zero[node]:
                current_left += tree_left[node]
            else:
                current_left = tree_left[node]
            if prev_right > 0 and tree_left[node] > 0:
                current_max = max(current_max, prev_right + tree_left[node])
            if not tree_all_zero[node]:
                prev_right = tree_right[node]
            else:
                prev_right += tree_right[node]
        return max(current_max, current_left, prev_right)

    output = []
    for _ in range(M):
        parts = input[ptr:ptr+3]
        if parts[0] == 'QUERY':
            l = int(parts[1]) - 1
            r = int(parts[2]) - 1
            res = query(l, r)
            output.append(str(res))
            ptr += 3
        elif parts[0] == 'UPDATE':
            i = int(parts[1]) - 1
            x = int(parts[2])
            update(i, x)
            ptr += 3
    print('\n'.join(output))

if __name__ == '__main__':
    main()
