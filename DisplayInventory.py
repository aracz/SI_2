inventory = {"arrow":12, "gold coin":42, "rope":1, "torch":6, "dagger":1}

def display_inventory():
    print("\nInventory: \n")
    for key in inventory.items():
        print('{:>1}'.format(key[1]),"   ",'{:}'.format(key[0]))
    print("\nTotal number of items: ",sum(inventory.values()))