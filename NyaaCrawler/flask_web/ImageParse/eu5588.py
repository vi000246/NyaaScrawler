import requests
import re
from lxml import etree
"""
適用的domain:
eu55888.eu
imgazel.info
imageteam
"""
class eu5588(object):
    def __init__(self, url):
        self.url = url

    def get(self):
        BigImgUrl = ''
        """
        如果結尾是html 就request 如果是圖片 就把samll換成big
        傳進來之前先判斷 如果有縮圖 就不要request 55888.eu/xxxx.html了
        通常都是重覆的 直接把縮圖換大圖就好
        """
        try:
            if re.match(r"http.*(?=html)",self.url):
                r = requests.get(self.url,stream=True)
                img = re.search(r"(?P<url>http://[^\/]*\/upload\/big\/[^\']*)", r.text)
                if img:
                    BigImgUrl = img["url"]
            elif re.match(r"http.*(?=(jpe?g|png))",self.url):
                BigImgUrl = self.url.replace("small","big")
        except Exception as e:
            print("eu5588錯誤: url=",self.url," message=",str(e))

        return BigImgUrl

if __name__ == '__main__':
    # imh = eu5588("http://55888.eu/upload/small/2017/08/28/59a48ccb9fc49.jpeg")
    imh = eu5588("http://55888.eu/img-590acd09036a2.html ")
    print(imh.get())