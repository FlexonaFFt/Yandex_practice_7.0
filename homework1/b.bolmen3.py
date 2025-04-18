def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        res = []
        i = 0
        while i < n:
            max_len = 1
            for l in range(1, n - i + 1):
                valid = True
                for j in range(i, i + l):
                    if a[j] < l:
                        valid = False
                        break
                if valid:
                    max_len = l
                else:
                    break
            res.append(max_len)
            i += max_len

        print(len(res))
        print(' '.join(map(str, res)))


solve()
