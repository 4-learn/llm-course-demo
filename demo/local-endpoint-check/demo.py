"""檢查本機端點"""

from urllib.parse import urlparse

endpoint = "http://127.0.0.1:11434"
parsed = urlparse(endpoint)
print("主機：", parsed.hostname)
print("本機端點：", parsed.hostname in {"127.0.0.1", "localhost", "::1"})
