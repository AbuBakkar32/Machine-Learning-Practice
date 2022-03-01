def main():
    game = {'rock': 'pock', 'papper': 'speark', 'popular': 'Python'}
    # for k in game.keys():
    #     print(k)

    # for k in game.values():
    #     print(k)

    game['yang'] = 'Olee'
    print_list(game)


def print_list(list):
    for i in list:
        print(f'{i}: {list[i]}')
    print()


if __name__ == "__main__":
    main()
