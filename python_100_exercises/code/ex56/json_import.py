import json
import pprint

with open("./company1.json") as file:
    filestring = json.loads(file.read())
    pprint.pprint(filestring)
    