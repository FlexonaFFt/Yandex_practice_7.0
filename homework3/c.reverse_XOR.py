def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_len = max(a).bit_length() if a else 0

    total_xor = 0
    for num in a:
        total_xor ^= num

    if total_xor == 0:
        print(' '.join(map(str, a)))

    else:
        bit_counts = [0] * max_len
        for num in a:
            for k in range(max_len):
                if num & (1 << k):
                    bit_counts[k] += 1

        possible = True
        for count in bit_counts:
            if count % 2 != 0:
                possible = False
                break

        if possible:
            print(' '.join(map(str, a)))
        else:
            print("impossible")


if __name__ == '__main__':
    main()
