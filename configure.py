# In the future, this will be used to determine which DLCs the 
# user owns. Right now, this does nothing.

import json

def ask(prompt):
    answer = input(prompt)
    if answer == "Y" or answer == "y":
        return True
    else:
        return False

steeled_veterans = ask("Do you own the Steeled Veterans Warbond? (Y/N) ")

dlc = {
    "steeled_veterans": steeled_veterans
}

out = json.dumps(dlc)

with open('config.json', 'w') as f:
    f.write(out)

print("Config.json successfully updated.")