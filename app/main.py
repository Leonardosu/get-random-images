import time
import random
from flask import Flask, render_template
from utils import Validator

app = Flask(__name__, template_folder='templates')


def get_random_site():
    num = random.randrange(100000, 999999)
    site = "https://prnt.sc/" + str(num)
    return site


@app.route('/', methods=['GET', 'POST'])
def index():

    found_image = False
    img_link = ''
    while not found_image:
        site = get_random_site()
        found_image, img_link = Validator.validate_link(site)
        
        print("Found image." if found_image else "Image is crashed.")
        time.sleep(0.2)

    print(img_link)
    return render_template('index.html', img_url=img_link)


if __name__ == "__main__":
    app.run()
