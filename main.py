import requests

para = {'api_key': "" } # paste your api key from https://api.nasa.gov inside double quotes}
json = (requests.get('https://api.nasa.gov/planetary/apod', params=para)).json()
file_to_open = (json["date"] + " - " + json["title"] + "." + (json["url"].split("."))[-1])
with open(file_to_open, "wb") as file:
    file.write((requests.get(json["hdurl"])).content)