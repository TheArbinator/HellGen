import json
import random
import sys

print("HellGen: A Helldivers 2 Loadout Generator by TheArbinator")
print("This project is incomplete. Not all items are implemented.\n")

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data

def append_dlc(dlc_list, dlc_name, primaries_list, secondaries_list, throwables_list, stratagems_list):
    if dlc_list.get(dlc_name):
        filename = "data/" + dlc_name + ".json"
        dlc_data = read_json(filename)
        primaries_list.extend(dlc_data.get("primaries"))
        secondaries_list.extend(dlc_data.get("secondaries"))
        throwables_list.extend(dlc_data.get("throwables"))
        stratagems_list.extend(dlc_data.get("stratagems"))

default = read_json("data/default.json")
dlc = read_json("config.json")

primaries = default.get("primaries")
secondaries = default.get("secondaries")
throwables = default.get("throwables")
stratagems = default.get("stratagems")

append_dlc(dlc, "steeled_veterans", primaries, secondaries, throwables, stratagems)
append_dlc(dlc, "cutting_edge", primaries, secondaries, throwables, stratagems)
append_dlc(dlc, "democratic_detonation", primaries, secondaries, throwables, stratagems)
append_dlc(dlc, "polar_patriots", primaries, secondaries, throwables, stratagems)
append_dlc(dlc, "viper_commandos", primaries, secondaries, throwables, stratagems)
append_dlc(dlc, "freedoms_flame", primaries, secondaries, throwables, stratagems)
append_dlc(dlc, "chemical_agents", primaries, secondaries, throwables, stratagems)
append_dlc(dlc, "truth_enforcers", primaries, secondaries, throwables, stratagems)
append_dlc(dlc, "urban_legends", primaries, secondaries, throwables, stratagems)
append_dlc(dlc, "servants_of_freedom", primaries, secondaries, throwables, stratagems)


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