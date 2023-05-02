import json
import requests

fetch=requests.get('https://api.data.gov.sg/v1/environment/2-hour-weather-forecast')
data=fetch.text
parse_data=json.loads(data)

# print(parse_data)

print(parse_data['items'])