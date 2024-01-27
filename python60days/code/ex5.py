newmem = input("Enter new member: ")

with open("members.txt", "a") as file:
    file.write(newmem)
