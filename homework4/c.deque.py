from collections import deque

def main():
    d = deque()
    while True:
        try:
            command = input().strip()
        except EOFError:
            break

        if command.startswith("push_front"):
            _, n = command.split()
            d.appendleft(int(n))
            print("ok")
        elif command.startswith("push_back"):
            _, n = command.split()
            d.append(int(n))
            print("ok")
        elif command == "pop_front":
            if d:
                print(d.popleft())
            else:
                print("error")
        elif command == "pop_back":
            if d:
                print(d.pop())
            else:
                print("error")
        elif command == "front":
            if d:
                print(d[0])
            else:
                print("error")
        elif command == "back":
            if d:
                print(d[-1])
            else:
                print("error")
        elif command == "size":
            print(len(d))
        elif command == "clear":
            d.clear()
            print("ok")
        elif command == "exit":
            print("bye")
            break
        else:
            print("unknown command")

if __name__ == "__main__":
    main()
