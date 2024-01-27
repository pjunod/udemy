import requests

url = "https://pythonhow.com/media/data/universe.txt"

page = requests.get(url)
text = page.text

count = text.count("a")

print(count)
