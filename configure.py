import json

def ask(prompt):
    answer = input(prompt)
    if answer == "Y" or answer == "y":
        return True
    else:
        return False

steeled_veterans = ask("Do you own the Steeled Veterans Warbond? (Y/N) ")
cutting_edge = ask("Do you own the Cutting Edge Warbond? (Y/N) ")
democratic_detonation = ask("Do you own the Democratic Detonation Warbond? (Y/N) ")
polar_patriots = ask("Do you own the Polar Patriots Warbond? (Y/N) ")
viper_commandos = ask("Do you own the Viper Commandos Warbond? (Y/N) ")
freedoms_flame = ask("Do you own the Freedom's Flame Warbond? (Y/N) ")
chemical_agents = ask("Do you own the Chemical Agents Warbond? (Y/N) ")
truth_enforcers = ask("Do you own the Truth Enforcers Warbond? (Y/N) ")
urban_legends = ask("Do you own the Urban Legends Warbond? (Y/N) ")
servants_of_freedom = ask("Do you own the Servants of Freedom Warbond? (Y/N) ")


dlc = {
    "steeled_veterans": steeled_veterans,
    "cutting_edge": cutting_edge,
    "democratic_detonation": democratic_detonation,
    "polar_patriots": polar_patriots,
    "viper_commandos": viper_commandos,
    "freedoms_flame": freedoms_flame,
    "chemical_agents": chemical_agents,
    "truth_enforcers": truth_enforcers,
    "urban_legends": urban_legends,
    "servants_of_freedom": servants_of_freedom
}

out = json.dumps(dlc)

with open('config.json', 'w') as f:
    f.write(out)

print("config.json successfully updated.")