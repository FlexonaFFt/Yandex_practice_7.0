from collections import deque

n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print('0 0')
    exit()

result = [0] * n
prev = [(i - 1 + n) % n for i in range(n)]
next_ = [(i + 1) % n for i in range(n)]
alive = bytearray([1] * n)
queue = deque()

for i in range(n):
    l, r = prev[i], next_[i]
    if a[i] < a[l] and a[i] < a[r]:
        queue.append(i)

round_num = 1
while queue:
    next_queue = deque()

    while queue:
        i = queue.popleft()
        if not alive[i]:
            continue
        l, r = prev[i], next_[i]
        if a[i] < a[l] and a[i] < a[r]:
            result[i] = round_num
            alive[i] = 0
            next_[l] = r
            prev[r] = l

            if alive[l] and a[l] < a[prev[l]] and a[l] < a[next_[l]]:
                next_queue.append(l)
            if alive[r] and a[r] < a[prev[r]] and a[r] < a[next_[r]]:
                next_queue.append(r)

    if sum(alive) <= 2:
        break

    queue = next_queue
    round_num += 1

print(*result)
