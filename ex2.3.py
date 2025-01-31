# WORK IN PROGRESS
import json
with open("large-file.json", "r", encoding = "UTF=8") as file:
    content = json.load(file)

print(content[0]["type"])

for i in content:
    if content[i]["size"] != 42:
        content[i]["size"] = 42