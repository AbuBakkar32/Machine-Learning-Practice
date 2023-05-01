class Mobile:
    old_phone = 'Keypad'
    new_phone = 'Touch Screen'

    def old_nokia(self):
        print(self.old_phone)

    def new_iphone(self):
        print(self.new_phone)


def main():
    myMobile = Mobile()
    myMobile.new_iphone()
    myMobile.old_nokia()


if __name__ == '__main__':
    main()
