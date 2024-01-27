import string
import os

# idx = 0
# idx2 = 1
# with open("twoout.txt", 'w') as twofile:
#     while idx < len(string.ascii_lowercase) - 2:
#         twoout = string.ascii_lowercase[idx] + string.ascii_lowercase[idx2]
#         twofile.write(twoout + '\n')
#         idx += 2
#         idx2 += 2

with open("twoout2.txt", "w") as file:
    for ltr, ltr2 in zip(string.ascii_lowercase[0::2],
                         string.ascii_lowercase[1::2]):
        file.write(ltr + ltr2 + '\n')

letters = string.ascii_lowercase + " "

slice1 = letters[0::3]
slice2 = letters[1::3]
slice3 = letters[2::3]

with open("threeout.txt", "w") as file:
    for ltr, ltr2, ltr3 in zip(slice1, slice2, slice3):
        file.write(ltr + ltr2 + ltr3 + '\n')

for letter in string.ascii_lowercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(letter + '\n')

letterlist = []
for file in os.listdir("letters"):
    with open(file) as letterfile:
        letterlist.append(letterfile.read().strip())
print(letterlist)