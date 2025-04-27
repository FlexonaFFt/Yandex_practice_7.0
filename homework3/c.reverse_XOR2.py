def solve():
    # Читаем входные данные
    n = int(input())
    numbers = list(map(int, input().split()))

    # Преобразуем числа в двоичное представление
    binary_numbers = [bin(num)[2:] for num in numbers]

    # Находим максимальную длину двоичного представления
    max_length = max(len(num) for num in binary_numbers)

    # Дополняем числа ведущими нулями
    padded_numbers = [num.zfill(max_length) for num in binary_numbers]

    # Создаем матрицу битов
    bit_matrix = []
    for num in padded_numbers:
        bit_matrix.append(list(map(int, num)))

    # Проверяем возможность решения
    for col in range(max_length):
        ones_count = sum(row[col] for row in bit_matrix)
        if ones_count % 2 != 0:
            print("impossible")
            return

    # Если решение возможно, строим новые числа
    new_numbers = []
    for i in range(n):
        new_number_bits = [0] * max_length
        for j in range(max_length):
            if bit_matrix[i][j] == 1:
                # Переносим единицы в новое число
                new_number_bits[j] = 1
        new_numbers.append(int(''.join(map(str, new_number_bits)), 2))

    # Выводим результат
    print(*new_numbers)

# Вызываем функцию
solve()
