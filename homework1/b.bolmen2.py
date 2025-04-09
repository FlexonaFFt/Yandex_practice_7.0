# Считываем количество тестов
t = int(input())

# Обрабатываем каждый тест
for _ in range(t):
    # Считываем длину массива
    n = int(input())
    # Считываем массив
    a = list(map(int, input().split()))

    # Список для хранения длин отрезков
    lengths = []
    i = 0  # Текущая позиция в массиве

    # Пока не обработали весь массив
    while i < n:
        # Пробуем минимальную длину отрезка
        len_segment = 1
        max_val = a[i]

        # Пробуем расширять отрезок
        while i + len_segment <= n:
            max_val = max(a[i:i + len_segment])
            # Если длина отрезка >= максимального значения, или это последний отрезок
            if len_segment >= max_val or i + len_segment == n:
                break
            # Пробуем длину, которая ближе к ожидаемому разбиению
            if len_segment < max_val:
                # Если максимальное значение больше текущей длины, пробуем взять отрезок длиной max_val
                len_segment = max_val
            else:
                len_segment += 1

        # Если вышли за пределы, корректируем длину
        if i + len_segment > n:
            len_segment = n - i

        # Добавляем длину отрезка
        lengths.append(len_segment)
        # Переходим к следующему отрезку
        i += len_segment

    # Выводим количество отрезков
    print(len(lengths))
    # Выводим длины отрезков
    print(*lengths)
