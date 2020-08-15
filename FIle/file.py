def main():
    f = open('reads.txt', 'r')
    for line in f:
        print(line.strip())


if __name__ == '__main__':
    main()
