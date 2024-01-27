
d = dict(weather="clima", earth="terra", rain="chuva")


def translate(word):
    try:
        return d[word]
    except KeyError:
        return "That word does not exist."


word = input("Enter word: ")

translated = translate(word.lower())

print(translated)
