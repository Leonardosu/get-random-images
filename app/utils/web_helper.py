import random
import urllib.request


class WebHelper:
    @staticmethod
    def get_random_site():
        number = random.randrange(100000, 999999)
        return 'https://prnt.sc/' + str(number)

    @staticmethod
    def download_image(url, file_path, file_name):
        urllib.request.urlretrieve(url, file_path + file_name)
