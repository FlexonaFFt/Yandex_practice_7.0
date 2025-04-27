def main():
    n = int(input())
    if n == 0:
        return 0
    else:
        binary = bin(n)[2:]
        max_binary = binary
        current = binary

        for _ in range(len(binary)):
            current = current[-1] + current[:-1]
            if current > max_binary:
                max_binary = current

        print(int(max_binary, 2))

main()
