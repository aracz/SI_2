import operator
inventory = {"arrow":12, "gold coin":42, "rope":1, "torch":6, "dagger":1}

def display_inventory():
    print("\nInventory: ")
    sorted_inv = sorted(inventory.items(), key=operator.itemgetter(1))
    for key in sorted_inv:
        print('{:}'.format(key[1]),"   ",'{:}'.format(key[0]))
    print("Total number of items: ",sum(inventory.values()))

display_inventory()

