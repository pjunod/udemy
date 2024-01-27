import json

with open("company1.json", "r+") as file:
    filecontents = json.loads(file.read())
    filecontents["employees"].append({"firstName": "Albert", "lastName":
                                      "Bert"})
    file.seek(0)
    json.dump(filecontents, file, indent=4, sort_keys=True)
    file.truncate()
    file.close()
