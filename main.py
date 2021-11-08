import requests

para = {'api_key':  # paste your api key from https://api.nasa.gov inside double quotes}
json = (requests.get('https://api.nasa.gov/planetary/apod', params=para)).json()
file = open(json["date"] + " - " + json["title"] + "." + (json["url"].split("."))[-1], "wb")
file.write((requests.get(json["hdurl"])).content)
file.close()
