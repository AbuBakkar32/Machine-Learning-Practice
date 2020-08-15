import time


def main():
    infile = open('reads.txt', 'rb')
    CopyFile = open('reads-copy.txt', 'wb')

    while True:
        buffer = infile.read(10240)
        if buffer:
            CopyFile.write(buffer)
            print('.', end='', flush=True)
        else:
            break
    CopyFile.close()
    print('\nDone........')


if __name__ == '__main__':
    main()

