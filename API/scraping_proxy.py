from concurrent.futures import ProcessPoolExecutor, as_completed
from requests import get
from bs4 import BeautifulSoup, Tag
from json import dump
from sys import getsizeof

urls = {
    'all': 'https://free-proxy-list.net/',
    'ssl': 'https://www.sslproxies.org/',
    'anonymous': 'https://free-proxy-list.net/anonymous-proxy.html',
    'socks': 'https://www.socks-proxy.net/',
    'usa': 'https://www.us-proxy.org/',
    'uk': 'https://free-proxy-list.net/uk-proxy.html',
    'socks_2': 'https://premproxy.com/socks-list/',
    'all_2': 'https://premproxy.com/list/'
}


def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9'
    }
    # url_name = url.split('//')[1].replace('/', '.')

    response = get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    return soup


def url_last(soup_head):
    new_soup_head = []
    for head_column in soup_head:
        if isinstance(head_column, Tag):
            if head_column.find("a"):
                new_soup_head.append(head_column.find("a").contents[0])
            if head_column.find("dfn"):
                new_soup_head.append(head_column.find("dfn").contents[0])

    return new_soup_head


def extract(key, url):
    soup = get_url(url)
    soup_head = soup.find("table").find('thead').find("tr").contents
    soup_row = soup.find("table").find('tbody').contents

    if key == 'all_2' or key == 'socks_2':  # Last url scraping is different
        soup_head = url_last(soup_head)

    # json.dump for file, json.dumps for parsing, print
    """
        json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, 
            allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
    """
    with open(f"proxies_({key}).json", 'w') as js:

        json_list = []
        for row_index, row_value in enumerate(soup_row):
            if isinstance(row_value, Tag):
                row_value = row_value.find_all('td')

                detail_row_value = {}
                detail_row_value['id'] = row_index

                for head_index, head in enumerate(soup_head):
                    if len(row_value) < len(soup_head):
                        continue
                    elif len(row_value[head_index].get_text()) > 0:
                        detail_row_value[head.get_text()] = row_value[head_index].get_text()

                        if row_value[head_index].get_text() == "\u00a0":
                            detail_row_value[head.get_text()] = 'empty'
                    else:
                        detail_row_value[head.get_text()] = 'empty'

                json_list.append(detail_row_value)  # Append to dicts to list, [{}]

        dump(json_list, js, indent=2)

    print(f'[ proxies_({key}).json : {getsizeof(key)} KB ]')


def main(urls=None):
    with ProcessPoolExecutor() as exe:
        for key, value in urls.items():
            exe.submit(extract, key, value)


if __name__ == "__main__":
    main(urls)
