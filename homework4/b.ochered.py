from collections import deque

def main():
    queue = deque()
    while True:
        try:
            command = input().strip()
        except EOFError:
            break

        if command.startswith("push"):
            _, n = command.split()
            queue.append(int(n))
            print("ok")
        elif command == "pop":
            if queue:
                print(queue.popleft())
            else:
                print("error")
        elif command == "front":
            if queue:
                print(queue[0])
            else:
                print("error")
        elif command == "size":
            print(len(queue))
        elif command == "clear":
            queue.clear()
            print("ok")
        elif command == "exit":
            print("bye")
            break
        else:
            print("unknown command")

if __name__ == "__main__":
    main()
