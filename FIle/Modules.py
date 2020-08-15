import sys
import os
import datetime

def main():
    v = sys.version_info
    print('python version {}.{}.{}'.format(*v))

    dir = os.name
    w = os.getcwd()
    print(dir)
    print(w)

    now = datetime.datetime.now()
    print(now)
    print(now.year)
    print(now.month)
    print(now.day)

if __name__ == '__main__':
    main()