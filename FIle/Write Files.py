import time


def main():
    infile = open('reads.txt', 'rb')
    CopyFile = open('reads-copy.txt', 'wb')

    for line in infile:
        print(line.strip(), file=CopyFile)
        print('.', end='', flush=True)

    CopyFile.close()
    print('\nDone........')


if __name__ == '__main__':
    main()

