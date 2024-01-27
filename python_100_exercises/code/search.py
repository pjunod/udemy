import urllib.parse
import webbrowser

term = input("Enter search term: ")

search_term = urllib.parse.quote_plus(term)

url = f"https://www.google.com/search?q={search_term}"
webbrowser.open(url, new=0)