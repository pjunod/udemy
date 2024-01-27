prompt = ""

with open("user_data.txt", "a") as file:
    while True:
        prompt = input("Write a value: ")
        if prompt == "CLOSE":
            break
        else:
            file.write(f"{prompt}\n")
