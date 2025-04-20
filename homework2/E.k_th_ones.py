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
    seg_tree = [0] * (2 * size)

    # Построение дерева
    for i in range(N):
        seg_tree[size + i] = 1 if arr[i] == 0 else 0
    for i in range(size - 1, 0, -1):
        seg_tree[i] = seg_tree[2 * i] + seg_tree[2 * i + 1]

    M = int(input[ptr])
    ptr += 1

    output = []

    for _ in range(M):
        query = input[ptr]
        ptr += 1

        if query == 'u':
            # Обновление элемента
            pos = int(input[ptr]) - 1  # преобразуем в 0-based индекс
            ptr += 1
            val = int(input[ptr])
            ptr += 1

            # Обновляем значение в массиве
            old_val = arr[pos]
            arr[pos] = val

            # Обновляем дерево отрезков
            node = size + pos
            new_zero = 1 if val == 0 else 0
            if seg_tree[node] == new_zero:
                continue  # ничего не изменилось

            seg_tree[node] = new_zero
            node >>= 1
            while node >= 1:
                new_val = seg_tree[2 * node] + seg_tree[2 * node + 1]
                if seg_tree[node] == new_val:
                    break
                seg_tree[node] = new_val
                node >>= 1

        elif query == 's':
            # Поиск k-го нуля на отрезке [l, r]
            l = int(input[ptr]) - 1  # 0-based
            ptr += 1
            r = int(input[ptr]) - 1
            ptr += 1
            k = int(input[ptr])
            ptr += 1

            # Функция для поиска k-го нуля
            def find_kth_zero(l, r, k):
                l += size
                r += size
                zeros = 0
                left_edges = []
                right_edges = []

                while l <= r:
                    if l % 2 == 1:
                        left_edges.append(l)
                        l += 1
                    if r % 2 == 0:
                        right_edges.append(r)
                        r -= 1
                    l >>= 1
                    r >>= 1

                all_nodes = left_edges + right_edges[::-1]

                # Проверяем, достаточно ли нулей
                total = 0
                for node in all_nodes:
                    total += seg_tree[node]
                    if total >= k:
                        break

                if total < k:
                    return -1

                # Ищем k-й ноль
                remaining = k
                for node in all_nodes:
                    if seg_tree[node] >= remaining:
                        # Ищем в этом узле
                        while node < size:
                            left_child = 2 * node
                            right_child = 2 * node + 1
                            if seg_tree[left_child] >= remaining:
                                node = left_child
                            else:
                                remaining -= seg_tree[left_child]
                                node = right_child
                        return node - size + 1  # преобразуем в 1-based индекс
                    else:
                        remaining -= seg_tree[node]

                return -1

            res = find_kth_zero(l, r, k)
            output.append(str(res))

    print(' '.join(output))

if __name__ == "__main__":
    main()
