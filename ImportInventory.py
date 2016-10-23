import csv

with open("dragon_loot.csv") as infile:
    reader = csv.reader(infile)
    with open("dragon_loot.csv", mode="w") as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[1]:rows[2] for rows in reader}

mydict

inventory = {"arrow":12, "gold coin":42, "rope":1, "torch":6, "dagger":1}

#def import_inventory(filename):
