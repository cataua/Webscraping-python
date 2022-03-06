# This is a sample Python script.
import urllib.request
import ssl

from bs4 import BeautifulSoup


def catchWeb(url):
    # Use a breakpoint in the code line below to debug your script.
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "https://uol.com.br"
    catchWeb(url)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
