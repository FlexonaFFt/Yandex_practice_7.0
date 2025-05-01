def min_piggybanks_to_break(n, keys):
    visited = [False] * n
    in_stack = [False] * n
    result = 0

    def dfs(u):
        nonlocal result
        while not visited[u]:
            visited[u] = True
            in_stack[u] = True
            u = keys[u]
        if in_stack[u]:
            result += 1

        u = keys[u]
        while in_stack[u]:
            in_stack[u] = False
            u = keys[u]

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return result


n = int(input())
keys = [int(input()) - 1 for _ in range(n)]
print(min_piggybanks_to_break(n, keys))
