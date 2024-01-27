import sys

entry = input("Enter values: ")
if len(entry) < 1:
    print("Error, you must enter something")
    sys.exit(1)


with open("ex95.out", "a") as file:
    for item in entry.split(','):
        file.write(f"{item}\n")
