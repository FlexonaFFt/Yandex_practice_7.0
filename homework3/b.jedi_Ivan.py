def main():
    n, a = int(input()), []
    matrix = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        current = 0
        for j in range(n):
            if i != j:
                current |= matrix[i][j]
        a.append(current)

    print(' '.join(map(str, a)))


if __name__ == '__main__':
    main()
