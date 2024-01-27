import string

remove = list(string.ascii_uppercase + '\n')
remove.append("Top of Page")
remove.append("")

with open("countries_raw.txt") as file:
    dirty = file.readlines()

dirty = [x.strip() for x in dirty]
dirty = [x for x in dirty if x not in remove]

for country in dirty:
    print(country)