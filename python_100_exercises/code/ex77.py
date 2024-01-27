from datetime import datetime

age = input("Enter current age: ")

born = datetime.now().year-int(age)

print(f"You were born in {born}.")