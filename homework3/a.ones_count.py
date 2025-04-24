def main():
    number, counter = int(input()), 0
    while number > 0:
        counter += number & 1
        number >>= 1
    print(counter)

if __name__ == '__main__':
    main()
