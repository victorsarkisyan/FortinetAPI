#!/usr/bin/env python3

import requests
import json
import sys
import urllib3

# Disable insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_key = sys.argv[1]
switch = sys.argv[2]

url = "https://192.168.0.1/api/v2/monitor/switch-controller/managed-switch/port-stats"

params = {
     'mkey': switch
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

try:
    response = requests.get(url, headers=headers, params=params, verify=False)
    response.raise_for_status()
    data = response.json()
    print(json.dumps(data))

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    sys.exit(1)
