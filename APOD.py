import requests
import json
import webbrowser
from urllib.request import urlretrieve
from pprint import PrettyPrinter
pp = PrettyPrinter()
pp = PrettyPrinter()

apiKey = 'KfO5HEevBmYG2rrA6Jd4S4XjaQx4GRODy9BMQi2p'

def fetchAPOD():
  URL_APOD = "https://api.nasa.gov/planetary/apod"
  date = '2023-07-22'
  params = {
      'api_key':apiKey,
      'date':date,
      'hd':'True'
  }
  response = requests.get(URL_APOD,params=params)
  json_data = json.loads(response.text)
  image_url = json_data['hdurl']
  webbrowser.open(image_url)
fetchAPOD()
