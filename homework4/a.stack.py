class Solution:
    def main(self):
        stack = []
        while True:
            try:
                command = input().strip()
            except EOFError: break

            if command.startswith("push"):
                _, n = command.split()
                stack.append(int(n))
                print("ok")
            elif command == "pop":
                if stack:
                    print(stack.pop())
                else:
                    print("error")
            elif command == "back":
                if stack:
                    print(stack[-1])
                else:
                    print("error")
            elif command == "size":
                print(len(stack))
            elif command == "clear":
                stack.clear()
                print("ok")
            elif command == "exit":
                print("bye")
                break
            else:
                print("unknown command")

if __name__ == "__main__":
    solution = Solution()
    solution.main()
