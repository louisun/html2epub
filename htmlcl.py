from html.parser import HTMLParser
import hashlib
import requests


class get_img(HTMLParser):
    def __init__(self, html, path):
        self.html = html
        self.path = path
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):

        if tag == 'img':
            for key, value in attrs:

                if key == "src":

                    hash = hashlib.md5(value.encode('utf-8')).hexdigest().upper()[0:8]
                    new_url = "oebps/image/" + hash + '.png'

                    try:
                        i_headers = {
                            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",
                            "Accept": "text/plain"}

                        res = requests.get(value, headers=i_headers)

                        f = open(self.path + new_url, "wb")
                        f.write(res.content)


                    except Exception as e:
                        print(e)
                    self.html[0] = self.html[0].replace(value, '../' + new_url)
