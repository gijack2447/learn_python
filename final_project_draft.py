import json, requests

base_url = "https://api.openweathermap.org/data/2/5/weather"
apikey = "134a631032499d98cc8d99fcfdcacbf7"
city = "Omaha"

url = f"{base_url}?q={city}&units=imperial&APPID={apikey}"
print(url)