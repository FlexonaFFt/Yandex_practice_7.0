def main():
    n = int(input())
    binary = bin(n)[2:]
    max_val = n

    for _ in range(len(binary) - 1):
        binary = binary[-1] + binary[:-1]
        val = int(binary, 2)
        if val > max_val:
            max_val = val

    print(max_val)

main()
