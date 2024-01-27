import glob

match = "python"
matchlist = []

for letterfile in glob.glob("letters/*"):
    with open(letterfile) as file:
        contents = file.read()
        contents = contents.strip()
        if contents in match:
            matchlist.append(contents)

print(matchlist)