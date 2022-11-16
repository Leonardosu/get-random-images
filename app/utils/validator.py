from urllib.request import Request, urlopen


class Validator:
    @staticmethod
    def validate_imgur_link(imgur_link: str) -> bool:
        if 'prntscr' in imgur_link:
            return False

        imgur_req = Request(imgur_link, headers={'User-Agent': 'Mozilla/5.0'})
        imgur_html = str(urlopen(imgur_req).read())

        if 'content="https://www.facebook.com/imgur">  <script src=' in imgur_html:
            return False
        return True

    @staticmethod
    def validate_link(site) -> tuple[bool, str]:
        req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
        html = str(urlopen(req).read())

        img_class = 'twitter:image:src'
        img_class_index = html.index(img_class)
        img_link_ini = img_class_index + len(img_class) + 11
        img_link_end = img_link_ini + html[img_link_ini:].index('"')
        img_link = html[img_link_ini:img_link_end]

        imgur_link = img_link[:len(img_link) - 4]
        return Validator.validate_imgur_link(imgur_link), str(imgur_link + '.jpeg')
