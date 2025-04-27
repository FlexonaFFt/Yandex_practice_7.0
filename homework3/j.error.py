import sys

def insert_parity_bits(data):
    n = len(data)
    m = 0
    # посчитаем сколько нужно контрольных бит
    while (1 << m) < n + m + 1:
        m += 1

    res = ['0'] * (n + m)
    j = 0
    for i in range(1, len(res) + 1):
        if i & (i - 1) == 0:
            # это место для контрольного бита
            continue
        res[i - 1] = data[j]
        j += 1

    # Теперь устанавливаем контрольные биты
    for i in range(m):
        pos = (1 << i)
        parity = 0
        for j in range(1, len(res) + 1):
            if j & pos and j != pos:
                parity ^= int(res[j - 1])
        res[pos - 1] = str(parity)

    return ''.join(res)

def fix_error_and_extract(data):
    n = len(data)
    m = 0
    while (1 << m) < n + 1:
        m += 1

    res = list(data)
    error_pos = 0

    for i in range(m):
        pos = (1 << i)
        parity = 0
        for j in range(1, n + 1):
            if j & pos:
                parity ^= int(res[j - 1])
        if parity:
            error_pos += pos

    if error_pos:
        # исправляем бит
        res[error_pos - 1] = '1' if res[error_pos - 1] == '0' else '0'

    # теперь извлекаем данные
    result = []
    for i in range(1, n + 1):
        if i & (i - 1) == 0:
            continue
        result.append(res[i - 1])

    return ''.join(result)

def main():
    mode = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    if mode == 1:
        y = insert_parity_bits(s)
        print(y)
    else:
        x = fix_error_and_extract(s)
        print(x)

if __name__ == "__main__":
    main()
