import json
from urllib import response
import requests

response = requests.get("https://forbes400.herokuapp.com/api/forbes400")
json_result = json.loads(response.text)
ordered_res = []

for data in json_result:
    print(f"{data['rank']}. {data['person']['name']} - {data['finalWorth']} min $ ")