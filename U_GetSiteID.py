#!/usr/bin/env python3

import subprocess
import json
import sys

api_key = sys.argv[1]
controller_ip = sys.argv[2]
url = f"https://{controller_ip}/proxy/network/integration/v1/sites"

curl_command = [
    "curl",
    "-k",                     # <-- allow self-signed SSL certs
    "-X", "GET",
    "-H", f"x-api-key: {api_key}",
    "-H", "Content-Type: application/json",
    url
]

result = subprocess.run(curl_command, capture_output=True, text=True)

data = json.loads(result.stdout)

item_id = data["data"][0]["id"]
print(item_id)
