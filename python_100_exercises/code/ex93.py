import os

pcount = 0

walk = os.walk("ex93")
for dirlist in walk:
    for file in dirlist[2]:
        if file.endswith("py"):
            pcount += 1

print(f"Number of .py files: [{pcount}]")
