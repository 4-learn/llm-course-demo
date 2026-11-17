"""安全檢查合成頁面"""

from html.parser import HTMLParser

class Paragraphs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_p = False
        self.text = []
    def handle_starttag(self, tag, attrs):
        self.in_p = tag == "p"
    def handle_endtag(self, tag):
        if tag == "p":
            self.in_p = False
    def handle_data(self, data):
        if self.in_p and data.strip():
            self.text.append(data.strip())

def extract(html):
    parser = Paragraphs()
    parser.feed(html)
    if not parser.text:
        return "失敗：沒有可用正文"
    return "成功：" + " ".join(parser.text)

for page in ("<nav>Menu</nav><p>公開公告</p>", "<nav>Menu</nav>"):
    print(extract(page))
