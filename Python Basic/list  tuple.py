def main():
    game = ['rock', 'pock','papper', 'speark', 'popular', 'Python']
    print_list(', '.join(game))


def print_list(list):
    for i in list:
        print(i, end=' ', flush=True)
    print()


if __name__ =="__main__":
    main()