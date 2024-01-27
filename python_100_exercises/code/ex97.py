prompt = ""
buffer = []


def savetofile(buffer, file):
    for entry in buffer:
        file.write(f"{entry}\n")
    file.flush()


with open("user_data.txt", "a") as file:
    while True:
        prompt = input("Write a value: ")
        if prompt == "CLOSE":
            savetofile(buffer, file)
            break
        elif prompt == "SAVE":
            savetofile(buffer, file)
            buffer = []
        else:
            buffer.append(prompt)
