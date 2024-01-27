with open("urls.txt") as file:
    urls = file.readlines()

urls = [x.strip() for x in urls]

urls_fixed = []

for url in urls:
    url = url.replace("https", "http")
    url = url.replace('/', '//')
    urls_fixed.append(url)

for url in urls_fixed:
    print(url)