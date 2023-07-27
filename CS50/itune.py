import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()
response = requests.get(
    "https://itunes.apple.com/search?term=" + sys.argv[1] + "&limit=50"
)
# print(json.dumps(response.json(),indent=2))

o = response.json()

for request in o["results"]:
    print(request["trackName"])
