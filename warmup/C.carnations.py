def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 2:
        print(a[1] + a[0])
        return

    s = [a[1] - a[0], a[2] - a[0]]
    for i in range(2, len(a) - 1):
        s.append(min(s[i - 1], s[i - 2]) + abs(a[i] - a[i + 1]))

    print(s[-1])

if __name__ == "__main__":
    main()
