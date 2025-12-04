#!/usr/bin/env python3

import requests
import json
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_key = sys.argv[1]
controller_ip = sys.argv[2]
ap_id = sys.argv[3]

url = f"https://{controller_ip}/api/v2/monitor/wifi/managed_ap"
params = {"wtp_id": ap_id}
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

response = requests.get(url, headers=headers, params=params, verify=False)
results = response.json().get("results", [])

# Return the full radio array as JSON
radio_stats = results[0].get('radio', [])
print(json.dumps(radio_stats))