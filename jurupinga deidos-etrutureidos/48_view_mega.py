import requests
import json

url = f"https://api.coincap.io/v2/assets"

response = requests.get(url)

if response.status_code == 200:
    result = response.json()
    print(json.dumps(result, indent=4))
    #print(result.get("dezenas"))