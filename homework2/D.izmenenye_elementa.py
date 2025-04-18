import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    arr = list(map(int, input[ptr:ptr+N]))
    ptr += N

    size = 1
    while size < N:
        size <<= 1
    seg_max = [-float('inf')] * (2 * size)

    for i in range(N):
        seg_max[size + i] = arr[i]
    for i in range(size - 1, 0, -1):
        seg_max[i] = max(seg_max[2 * i], seg_max[2 * i + 1])

    def update(pos, value):
        pos += size
        seg_max[pos] = value
        pos >>= 1
        while pos >= 1:
            new_max = max(seg_max[2 * pos], seg_max[2 * pos + 1])
            if seg_max[pos] == new_max:
                break
            seg_max[pos] = new_max
            pos >>= 1

    def query(l, r):
        l += size
        r += size
        res = -float('inf')
        while l < r:
            if l % 2 == 1:
                res = max(res, seg_max[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res = max(res, seg_max[r])
            l >>= 1
            r >>= 1
        return res

    M = int(input[ptr])
    ptr += 1
    output = []
    for _ in range(M):
        cmd = input[ptr]
        ptr += 1
        if cmd == 's':
            l = int(input[ptr]) - 1
            r = int(input[ptr + 1]) - 1
            ptr += 2
            max_val = query(l, r + 1)
            output.append(str(max_val))
        elif cmd == 'u':
            pos = int(input[ptr]) - 1
            value = int(input[ptr + 1])
            ptr += 2
            update(pos, value)

    print(' '.join(output))

if __name__ == "__main__":
    main()
