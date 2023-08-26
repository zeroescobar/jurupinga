import requests
import json


url = "https://api.jikan.moe/v4/random/anime"

result = requests.get(url).json()