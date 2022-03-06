import urllib.request
import ssl

from bs4 import BeautifulSoup


def catchWeb(url):
    name = []
    ssl._create_default_https_context = ssl._create_unverified_context
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html5lib')
    list_item = soup.find_all('img')
    for item in list_item:
        if 'src' in item.attrs:
            src = item['src']
            name.append(src)
    print(name)

if __name__ == '__main__':
    url = "https://uol.com.br"
    catchWeb(url)
