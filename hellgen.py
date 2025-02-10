import json
import random

print("This project is incomplete. Not all items are implemented.")

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        file.close()
        return data


hell_dict = read_json("data/default.json")

primaries = hell_dict.get("primaries")
secondaries = hell_dict.get("secondaries")

primary = random.choice(primaries)
secondary = random.choice(secondaries)

print("Primary: " + primary.get("name"))
print("Secondary: " + secondary.get("name"))
