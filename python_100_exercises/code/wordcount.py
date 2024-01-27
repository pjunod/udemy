import string
import sys

if len(sys.argv) < 2:
    sys.argv.append("words2.txt")


def wordcount(sentin: str) -> int:
    return len(sentin.split())


def wordcountfile(sentin: str) -> int:
    with open(sentin) as filein:
        wktxt = filein.read()
        return len(wktxt.split())


def advwc(sentin: str) -> int:
    with open(sentin) as filein:
        wktxt = filein.read()
        wktxt = wktxt.replace(',', ' ')
        return len(wktxt.split())


myin = "this is the input sentence to count words"

print(wordcount(myin))

myin = sys.argv[1]
print(wordcountfile(myin))

print(advwc(myin))

with open("./alph.txt", 'w') as outfile:
    for letter in string.ascii_lowercase:
        outfile.write(f"{letter}\n")

a = [1, 2, 3]
b = [4, 5, 6]

mytup = zip(a, b)
for i in mytup:
    print(sum(i))