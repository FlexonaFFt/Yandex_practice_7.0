class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    k = int(data[1])

    fenwick = FenwickTree(n)
    arr = [0] * (n + 1)

    idx = 2
    result = []
    for _ in range(k):
        command = data[idx]
        if command == 'A':
            i = int(data[idx + 1])
            x = int(data[idx + 2])
            diff = x - arr[i]
            arr[i] = x
            fenwick.update(i, diff)
            idx += 3
        elif command == 'Q':
            l = int(data[idx + 1])
            r = int(data[idx + 2])
            res = fenwick.range_query(l, r)
            result.append(str(res))
            idx += 3

    print('\n'.join(result))

if __name__ == "__main__":
    main()
