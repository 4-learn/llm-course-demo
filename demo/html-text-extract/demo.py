"""離線抽取 HTML 標題與正文。"""

from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.keep = False
    def handle_starttag(self, tag, attrs):
        if tag in ("title", "p", "h1"):
            self.keep = True
    def handle_endtag(self, tag):
        if tag in ("title", "p", "h1"):
            self.keep = False
    def handle_data(self, data):
        if self.keep and data.strip():
            self.parts.append(data.strip())

sample = "<html><title>公告</title><nav>導覽</nav><h1>活動通知</h1><p>週五舉辦講座。</p></html>"
parser = TextExtractor()
parser.feed(sample)
print("\n".join(parser.parts))
