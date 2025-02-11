import json
import random
import sys

print("HellGen: A Helldivers 2 Loadout Generator by TheArbinator")
print("This project is incomplete. Not all items are implemented.\n")

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data


default = read_json("data/default.json")
dlc = read_json("config.json")

primaries = default.get("primaries")
secondaries = default.get("secondaries")
throwables = default.get("throwables")
stratagems = default.get("stratagems")

if dlc.get("steeled_veterans"):
    sv = read_json("data/steeled_veterans.json")
    primaries.extend(sv.get("primaries"))
    secondaries.extend(sv.get("secondaries"))
    throwables.extend(sv.get("throwables"))
    stratagems.extend(sv.get("stratagems"))



primary = random.choice(primaries)
secondary = random.choice(secondaries)
throwable = random.choice(throwables)
stratagem_loadout = random.sample(stratagems, 4)


# Name generation
# TODO: Generate a relevant name if there are many items with similar tags (eg. fire, bombs, etc.)

names = read_json("data/names.json")

adjectives = names.get("adjectives")
nouns = names.get("nouns")
suffixes = names.get("suffixes")
suffix_probability = names.get("suffix_probability")

name = "The " + random.choice(adjectives) + " " + random.choice(nouns)

if random.random() < suffix_probability:
    name += " of " + random.choice(suffixes)

# Output

print("-- " + name + " --")
print("Primary: " + primary.get("name"))
print("Secondary: " + secondary.get("name"))
print("Throwable: " + throwable.get("name"))
print("Stratagems: ")
for strat in stratagem_loadout:
    print("- " + strat.get("name"))