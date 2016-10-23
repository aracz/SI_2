inventory = {"arrow":12, "gold coin":42, "rope":1, "torch":6, "dagger":1}

dragon_loot=['gold coin','dagger','gold coin','gold coin','ruby']

def display_inventory():
    print("\nInventory: ")
    for key in inventory.items():
        print('{:>1}'.format(key[1]),"   ",'{:}'.format(key[0]))
    print("Total number of items: ",sum(inventory.values()))

def add_to_inventory(inventory,added_items):
    for key in added_items:
        if not key in inventory:
            inventory[key] = 1
        else:
            inventory[key] += 1

add_to_inventory(inventory,dragon_loot)
display_inventory()


