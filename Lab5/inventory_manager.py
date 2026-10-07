import json

def load_inventory():
        try:
            with open('inventory.json', 'r') as inventory:
                data =json.load(inventory)
                print("inventory.json found\nInventory loaded successfully.\n")
                return data
        except FileNotFoundError:
            print("inventory.json not found")
            with open('inventory.json', 'w') as inventory:
                json.dump([], inventory)
            print("No such file as inventory.json, creating a new file")
            data = []
            return data
        
def display_all(inventory):
    test = []
    for product in inventory:
        for info in product:
            test.append(f"{info}:{product[info]}")
            result = " | ".join(test)
        print(result)
        test.clear()

    
    
           
                
            
        
    

def get_valid_input():
    while True:
         try:
            user_input = int(input("Your Option: "))
            if (user_input < 1 or user_input > 6):
                print("That is not one of the options. Please try again.")
                continue
            else:
                return user_input
         except ValueError:
             print("That is not an integer!")
             continue

while True:
    print("="*37)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("="*37)

    inventory = load_inventory()

    print("-"*37)
    print("MENU")
    print("-"*37)
    print("1. Display all products\n2. Add product\n3. Update stock\n4. Search product\n5.Save inventory\n6.Exit")
    print("-"*37)

    option = get_valid_input()

    match option:
        case 1:
            display_all(inventory)
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
    
    break