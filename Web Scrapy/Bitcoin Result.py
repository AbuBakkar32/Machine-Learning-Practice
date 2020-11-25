from bs4 import BeautifulSoup
import requests
from termcolor import colored


def get_crypto_coin(coin):
    url = f"https://www.google.com/search?q={coin}+price"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    result = soup.find(class_="BNeawe iBp4i AP7Wnd").find(class_="BNeawe iBp4i AP7Wnd")
    results = f"1 {coin} = {result.text}"
    print(colored(results, 'red'))
    # print(soup.prettify())


# get_crypto_coin('bitcoin')

while True:
    try:
        currency_name = str(input("Write Your Crypto type currency: "))
        currency_name = currency_name.lower()
        if currency_name:
            get_crypto_coin(currency_name)
        else:
            print("Sorry Something Wrong!! Try Again.....\n")
    except:
        print("You Entered a Wrong keywords\n")
        pass
