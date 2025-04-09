n, m = map(int, input().split())
groups = list(map(int, input().split()))
audiences = list(map(int, input().split()))

result, count, i = [0] * n, 0, 0
audience_used, j = [False] * n, 0

# Создаём список пар (значение, исходный индекс) для групп и аудиторий
group_indeces = [(groups[i], i) for i in range(n)]
audience_indeces = [(audiences[j], j) for j in range(m)]
group_indeces.sort()
audience_indeces.sort()

while i < n and j < m:
    group_val, group_idx = group_indeces[i]
    audience_val, audience_idx = audience_indeces[j]

    if group_val + 1 <= audience_val:
        result[group_idx] = audience_idx + 1
        audience_used[j] = True
        count += 1
        i += 1
        j += 1
    else: j += 1

# На 6ом тесте возникает ошибка по времени
print(count)
print(' '.join(map(str, result)))
