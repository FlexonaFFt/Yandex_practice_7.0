def solve():
    n = int(input())
    apps = []
    result = []

    for _ in range(n):
        command = input()

        if command.startswith("Run"):
            app_name = command[4:]
            apps.insert(0, app_name)
            result.append(app_name)

        else:

            k = command.count("+Tab")

            index = (k % len(apps))
            app_name = apps[index]
            apps.pop(index)
            apps.insert(0, app_name)
            result.append(app_name)

    for app in result:
        print(app)

solve()
