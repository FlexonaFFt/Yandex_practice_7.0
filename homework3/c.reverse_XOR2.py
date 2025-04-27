def solve():
    n = int(input())
    a = list(map(int, input().split()))

    # Найдем максимальную длину в битах
    max_len = max(a).bit_length()

    # Представим все числа как списки битов (с выравниванием)
    bits = []
    for num in a:
        b = bin(num)[2:].zfill(max_len)
        bits.append(list(b))

    # Считаем количество единиц на каждой позиции
    ones = [0] * max_len
    for b in bits:
        for i in range(max_len):
            if b[i] == '1':
                ones[i] += 1

    # Проверяем: если сумма единиц на позиции нечётная — невозможно
    for count in ones:
        if count % 2 != 0:
            print('impossible')
            return

    # Теперь нужно распределить биты по позициям
    result = [0] * n
    for i in range(max_len):
        one_indices = [idx for idx, b in enumerate(bits) if b[i] == '1']
        zero_indices = [idx for idx, b in enumerate(bits) if b[i] == '0']

        # Поровну разделим единицы
        half = len(one_indices) // 2
        for idx in one_indices[:half]:
            result[idx] = (result[idx] << 1) | 1
        for idx in one_indices[half:] + zero_indices:
            result[idx] = (result[idx] << 1) | 0

    print(*result)

# Пример использования
solve()
