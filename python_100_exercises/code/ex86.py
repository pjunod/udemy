checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open("countries_clean.txt") as file:
    countries = file.readlines()

countries = [a.strip() for a in countries]

checklist = [x for x in checklist if x in countries]

print(checklist)