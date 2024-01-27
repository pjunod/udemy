with open("countries_missing.txt") as file:
    cm = file.readlines()

checklist = ["Portugal", "Germany", "Spain"]

cm = [x.strip() for x in cm]

cm.extend(checklist)
cm = sorted(cm)

with open("countries_full.txt", "w") as file:
    file.write('\n'.join(str(i) for i in cm))