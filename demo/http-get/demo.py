"""請求公共測試端點（需要網路）"""

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

request = Request("https://example.com/", method="GET")
try:
    with urlopen(request, timeout=5) as response:
        print("status:", response.status)
except (URLError, HTTPError, TimeoutError) as exc:
    print("request failed:", type(exc).__name__)
