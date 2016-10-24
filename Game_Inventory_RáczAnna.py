import operator
import csv

inventory = {"arrow":12, "gold coin":42, "rope":1, "torch":6, "dagger":1}
dragon_loot=['gold coin','dagger','gold coin','gold coin','ruby']

#***STEP 1***
def display_inventory():
    print("\nInventory: ")
    for key in inventory.items():
        print('{:}'.format(key[1]),"   ",'{:}'.format(key[0]))
    print("Total number of items: ",sum(inventory.values()))

#***STEP 2***
def add_to_inventory(inventory,added_items):
    for key in added_items:
        if not key in inventory:
            inventory[key] = 1
        else:
            inventory[key] += 1

#***STEP 3***
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

#***STEP 4***
def import_inventory(filename = "import_inventory.csv"):
    file_list = []
    with open(filename, "r") as file:       
        for line in file:                   
            row = line.split(",")                                       
            first = row[0]                                              
            second = row[1]                                             
            minus_line = len(second)-1                                  
            second = second[0:minus_line]                               
            file_list.extend([[first,second]])                          
    
    for l in range(1,len(file_list)):                               
        if file_list[l][0] in inventory:                                  
            inventory[file_list[l][0]] += int(file_list[l][1])        
        else:
            inventory[file_list[l][0]] = int(file_list[l][1])

#***STEP 5***
def export_inventory(filename = "export_inventory.csv"):
    if os.path.exists(filename) == False:
        with open(filename, 'w') as file:
            for key, value in inv.items():
                file.write('{0},{1}\n'.format(key, value))
    else:
        with open(filename, 'w') as file:
            for key, value in inv.items():
                file.write('{0},{1}\n'.format(key, value))

#***MAIN***
def main():
    display_inventory()
    add_to_inventory(inventory,dragon_loot)
    print_table(0)
    import_inventory("import_inventory.csv")
    display_inventory()
    export_inventory()