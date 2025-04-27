n = int(input())

# Инициализируем BIT
size = n + 2  # запас по индексам
tree = [[[0] * size for _ in range(size)] for _ in range(size)]

def update(x, y, z, delta):
    xi = x + 1
    while xi < size:
        yi = y + 1
        while yi < size:
            zi = z + 1
            while zi < size:
                tree[xi][yi][zi] += delta
                zi += zi & -zi
            yi += yi & -yi
        xi += xi & -xi

def query(x, y, z):
    res = 0
    xi = x + 1
    while xi > 0:
        yi = y + 1
        while yi > 0:
            zi = z + 1
            while zi > 0:
                res += tree[xi][yi][zi]
                zi -= zi & -zi
            yi -= yi & -yi
        xi -= xi & -xi
    return res

def query_cube(x1, y1, z1, x2, y2, z2):
    # Inclusion-Exclusion формула
    def safe_query(x, y, z):
        if x < 0 or y < 0 or z < 0:
            return 0
        return query(x, y, z)

    total = (
        safe_query(x2, y2, z2)
        - safe_query(x1 - 1, y2, z2)
        - safe_query(x2, y1 - 1, z2)
        - safe_query(x2, y2, z1 - 1)
        + safe_query(x1 - 1, y1 - 1, z2)
        + safe_query(x1 - 1, y2, z1 - 1)
        + safe_query(x2, y1 - 1, z1 - 1)
        - safe_query(x1 - 1, y1 - 1, z1 - 1)
    )
    return total

# Обрабатываем запросы
while True:
    parts = list(map(int, input().split()))
    m = parts[0]

    if m == 1:
        x, y, z, k = parts[1:]
        update(x, y, z, k)
    elif m == 2:
        x1, y1, z1, x2, y2, z2 = parts[1:]
        print(query_cube(x1, y1, z1, x2, y2, z2))
    elif m == 3:
        break
