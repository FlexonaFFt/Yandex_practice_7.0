def get_label(x, y):
    return x ^ y

def find_y(x, c):
    return x ^ c

# Чтение данных
x1, y1 = map(int, input().split())
x2, c2 = map(int, input().split())

# Первая часть
print(get_label(x1, y1))
# Вторая часть
print(find_y(x2, c2))
