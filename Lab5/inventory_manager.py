import json
import re
pattern = r"^P\d{3}$"
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
    print("Current Inventory")
    print("-"*37)
    if not inventory:
        print("No items found in inventory.")
        return
    for product in inventory:
        test = []
        for info in product:
            test.append(f"{info}:{product[info]}")
            result = " | ".join(test)
        print(result)

def update_product(inventory):
    print("Update Stock")
    existingIDs = []
    existingProducts = []
    for product in inventory:
        existingIDs.append(product["ID"])
        existingProducts.append(product)

    while True:
        ProductID = input("Enter Product ID: ").strip().upper()
        if not re.match(pattern,ProductID):
            print("Invalid format, try again.")
            continue
        elif ProductID not in existingIDs:
            print(f"Product ID {ProductID} is not a valid ID, please try again.")
            continue
        else:
            for item in existingProducts:
                if ProductID in item.values():
                    print("\nProduct Found")
                    print(f"Name:{item["Name"]}")
                    print(f"Current Stock:{item["Stock"]}\n")

                    while True:
                        try:
                            NewStock = int(input("New Stock Quantity: "))
                            if NewStock == 0:
                                existingProducts.remove(item)
                                existingIDs.remove(ProductID)
                                inventory.remove(item)
                                return
                            elif NewStock < 0:
                                print("Negative numbers are not allowed.")
                                continue
                            else:
                                item["Stock"] = NewStock
                                print("Stock updated successfully !")
                                return
                        except ValueError:
                            print("Invalid input, please try again.")
                            continue

def search_product(inventory):
    existingIDs = []
    existingProducts = []
    for product in inventory:
        existingIDs.append(product["ID"])
        existingProducts.append(product)
    print("Search For Product")

    try:
        ProductID = input("Enter a Product ID: ").strip().upper()
        if not re.match(pattern,ProductID):
            print("Invalid ID.")
            return
        elif ProductID not in existingIDs:
            print(f"The Product ID {ProductID} does not exist.")
            return
        else:
            for item in existingProducts:
                if ProductID in item.values():
                    print("Product Found")
                    print("-"*37)
                    print(f"ID:{item["ID"]}")
                    print(f"Name:{item["Name"]}")
                    print(f"Price:{item["Price"]}")
                    print(f"Stock:{item["Stock"]}")
                    return
    except ValueError:
        print("Invalid input.")
        return  

def add_product(inventory):
    print("Add New Product")
    existingIDs = []
    existingProducts = []
    for product in inventory:
        existingIDs.append(product["ID"])
        existingProducts.append(product["Name"].lower().replace(' ',''))
    
    while True:
        ProductID = input("Product ID: ").strip().upper()
        if not re.match(pattern,ProductID):
            print("Invalid format, Try again")
            continue
        elif ProductID in existingIDs:
            print(f"Product ID {ProductID} already exists, please try again.")
        else:
            break

    while True:
        ProductName = input("Product Name: ")
        if ProductName.replace(' ','').isalpha() == False:
            print("Invalid format, please try again.")
            continue
        elif ProductName.lower().replace(' ','') in existingProducts:
            print(f"{ProductName} already exists, please try again.")
            continue
        else:
             break

    while True:
        try:
            ProductPrice = float(input("Price: $"))
            if ProductPrice <= 0:
                print("Invalid price, please try again.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input type, please try again.")
            continue

    while True:
        try:
            Stock = int(input("Stock: "))
            if Stock <= 0:
                print("Invalid stock quantity, please try again.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input, please try again.")

    print("Product added successfully!")

    NewProduct = {
        "ID":ProductID,
        "Name":ProductName,
        "Price":f"${ProductPrice:.2f}",
        "Stock":Stock
    }
    inventory.append(NewProduct)

def save_inventory(inventory):
    print("Saving Inventory...")
    with open("Inventory.json", "w") as file:
        json.dump(inventory, file)
    print("Inventory saved successfully to inventory.json")
    
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

inventory = load_inventory()
while True:
    print("="*37)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("="*37)

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
            add_product(inventory)
        case 3:
            update_product(inventory)
        case 4:
            search_product(inventory)
        case 5:
            save_inventory(inventory)
        case 6:
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Terminating program...")
            break
        case _:
            print("Invalid option")
    print("\n")