def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    index += 2

    groups = list(map(int, data[index:index + n]))
    index += n
    audiences = list(map(int, data[index:index + m]))
    index += m

    group_indices = [(groups[i], i) for i in range(n)]
    audience_indices = [(audiences[j], j) for j in range(m)]
    group_indices.sort()
    audience_indices.sort()
    result = [0] * n
    audience_used = [False] * m
    count = 0

    i = 0
    j = 0

    while i < n and j < m:
        group_val, group_idx = group_indices[i]
        audience_val, audience_idx = audience_indices[j]

        if group_val + 1 <= audience_val:
            result[group_idx] = audience_idx + 1
            audience_used[j] = True
            count += 1
            i += 1
            j += 1
        else:
            j += 1

    print(count)
    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()
