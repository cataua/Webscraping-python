from flask import Flask, request, render_template
import urllib.request
import ssl

from bs4 import BeautifulSoup

app = Flask(__name__)


def catchweb(url):
    name = []
    ssl._create_default_https_context = ssl._create_unverified_context
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html5lib')
    list_item = soup.find_all('img')
    for item in list_item:
        if 'src' in item.attrs:
            src = item['src']
        elif 'srcset' in item.attrs:
            imgs = item['srcset']
            size = 0
            imgs_split = imgs.split(',')
            for img in imgs_split:
                img_item = img.split()
                img_size = int(img_item[1].replace('w', ''))
                if img_size > size:
                    size = img_size
        name.append(src)

    return name


@app.route('/')
def home():
    url = request.args.get("site")
    error = ""
    images = catchweb(url)
    if len(images) == 0:
        error = "Não foi possivel capturar as imagens."
    return render_template("layout.html", erro=error, images=images, total=str(len(images)))


if __name__ == '__main__':
    app.run()
