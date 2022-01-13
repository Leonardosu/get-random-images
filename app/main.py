from flask import Flask, render_template
from urllib.request import Request, urlopen

app = Flask(__name__)
from utils import getRandomLink, validateImage

@app.route('/')
def index():

    found_image = False
    while not found_image:

        site = getRandomLink()
        req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
        html = str(urlopen(req).read())

        img_class = "twitter:image:src"
        img_class_index = html.index(img_class)
        img_link_ini = img_class_index + len(img_class) + 11
        img_link_end = img_link_ini + html[img_link_ini:].index('"')
        img_link = html[img_link_ini:img_link_end]

        imgur_link = img_link[:len(img_link) - 4]

        found_image = validateImage(imgur_link)
        print("Found image." if found_image else "Image is crashed.")

    return render_template('index.html', random_img=img_link)


if __name__ == "__main__":
    app.run()
