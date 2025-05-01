def solve_weakest_link(n, ratings):
    result = [0] * n
    active = list(range(n))
    round_num = 1

    while len(active) > 2:
        to_remove = []
        for i in range(len(active)):
            left = active[(i - 1) % len(active)]
            right = active[(i + 1) % len(active)]
            current = active[i]

            if ratings[current] < ratings[left] and ratings[current] < ratings[right]:
                to_remove.append(i)
                result[current] = round_num

        if not to_remove:
            break

        for i in sorted(to_remove, reverse=True):
            active.pop(i)

        round_num += 1

    return result

n = int(input())
ratings = list(map(int, input().split()))
result = solve_weakest_link(n, ratings)
print(*result)
