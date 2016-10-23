import operator
inventory = {"arrow":12, "gold coin":42, "rope":1, "torch":6, "dagger":1}
dragon_loot=['gold coin','dagger','gold coin','gold coin','ruby']

def display_inventory():
    print("\nInventory: ")
    for key in inventory.items():
        print('{:}'.format(key[1]),"   ",'{:}'.format(key[0]))
    print("Total number of items: ",sum(inventory.values()))

def add_to_inventory(inventory,added_items):
    for key in added_items:
        if not key in inventory:
            inventory[key] = 1
        else:
            inventory[key] += 1

def print_table(order):
    if order == 1:
        sorted_inv = sorted(inventory.items(), key=operator.itemgetter(1), reverse=True)
    elif order == 2:
        sorted_inv = sorted(inventory.items(), key=operator.itemgetter(1))
    elif order == 0:
        sorted_inv = inventory.items()
    print('\nInventory: ')
    print("{:>5} {:>12}".format("count", "item name"))
    print("-"*18)
    for key in sorted_inv:
        print("{:>5} {:>12}".format(key[1],key[0]))
    print("-"*18)
    print("\nTotal number of items: ",sum(inventory.values()))

add_to_inventory(inventory,dragon_loot)
print_table(0)



