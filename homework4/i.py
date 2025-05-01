n = int(input())
mass = [0] * (n + 1)
prev = [0] * (n + 1)
top_mass = [0] * (n + 1)
total_mass = 0

for i in range(1, n + 1):
    t, m = map(int, input().split())
    if m == 0:

        mass[i] = mass[prev[t]]
        prev[i] = prev[prev[t]]
        top_mass[i] = top_mass[prev[t]]
    else:

        mass[i] = mass[t] + m
        prev[i] = t
        top_mass[i] = m
    total_mass += mass[i]

print(total_mass)
