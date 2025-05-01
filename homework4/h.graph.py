class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1


def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n, m, k = map(int, data[0].split())
    edges = set()
    for i in range(1, m + 1):
        u, v = map(int, data[i].split())
        edges.add((min(u, v), max(u, v)))

    operations = []
    to_cut = set()
    for line in data[m + 1:]:
        parts = line.split()
        if parts[0] == 'cut':
            u, v = int(parts[1]), int(parts[2])
            to_cut.add((min(u, v), max(u, v)))
            operations.append(('cut', u, v))
        else:
            u, v = int(parts[1]), int(parts[2])
            operations.append(('ask', u, v))

    dsu = DSU(n)
    for u, v in edges:
        if (u, v) not in to_cut:
            dsu.union(u, v)

    result = []
    for op in reversed(operations):
        if op[0] == 'ask':
            _, u, v = op
            result.append("YES" if dsu.find(u) == dsu.find(v) else "NO")
        else:
            _, u, v = op
            dsu.union(u, v)

    for ans in reversed(result):
        print(ans)


if __name__ == "__main__":
    solve()
