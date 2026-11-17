"""建立離線 API request/response"""

import json
request = {
    "model": "MODEL_ID_FROM_PROVIDER_DOCS",
    "messages": [{"role": "user", "content": "請用一句話問候。"}],
}
print(json.dumps(request, ensure_ascii=False, indent=2))
