# Чтение входных данных
N = int(input())  # Читаем N
A = list(map(int, input().split()))  # Читаем массив рейтингов
M = int(input())  # Читаем M

# Функция для нахождения максимальной длины подмассива с положительной суммой на отрезке [l, r]
def max_positive_subarray_length(arr, l, r):
    # Приводим индексы к 0-based (в задаче индексы 1-based)
    l -= 1
    r -= 1

    # Если отрезок состоит из одного элемента
    if l == r:
        return 1 if arr[l] > 0 else 0

    max_length = 0  # Максимальная длина подмассива с положительной суммой
    current_sum = 0  # Текущая сумма подмассива
    current_length = 0  # Текущая длина подмассива

    # Проходим по отрезку от l до r
    for i in range(l, r + 1):
        if current_sum + arr[i] > 0:
            # Если добавление текущего элемента даёт положительную сумму,
            # увеличиваем текущую длину подмассива
            current_sum += arr[i]
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            # Если сумма становится <= 0, сбрасываем подмассив
            current_sum = 0
            current_length = 0

    return max_length

# Обработка запросов
for _ in range(M):
    query = input().split()
    query_type = query[0]

    if query_type == "UPDATE":
        i, x = map(int, query[1:])
        # Обновляем рейтинг i-го ученика (индексы 1-based)
        A[i - 1] = x
    else:  # QUERY
        l, r = map(int, query[1:])
        # Находим максимальную длину подмассива с положительной суммой на отрезке [l, r]
        result = max_positive_subarray_length(A, l, r)
        print(result)
