import time
from flask import Flask, render_template
from utils import Validator, WebHelper

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    found_image = False
    image_link = ''

    while not found_image:
        site = WebHelper.get_random_site()
        found_image, image_link = Validator.validate_link(site)

        if found_image:
            try:
                WebHelper.download_image(image_link, 'static/', 'temporary_image.jpg')
            except Exception as e:
                found_image = False
                print(f'Failed to download image: {image_link}\n{e}')

        time.sleep(0.01)

    print(image_link)
    return render_template('index.html', random_img=image_link)


if __name__ == '__main__':
    app.run()
