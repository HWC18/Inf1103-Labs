import re
import json
from inventory import Inventory
from product import Product
pattern = r"^P\d{3}$"
def get_valid_input(): #function to get menu option
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

def load_InventoryFile(): #This function checks if the inventory file exists and creates it if it doesn't
        try:
            with open('inventory.json', 'r') as inventory:
                print("inventory.json found\n")
                return inventory
        except FileNotFoundError:
            print("inventory.json not found")
            with open('inventory.json', 'w') as inventory:
                json.dump([], inventory)
            print("No such file as inventory.json, creating a new file")
            return inventory

def get_ProductInfo(inventory):
    ExistingIDs = inventory.get_IDs()
    ExistingNames = inventory.get_Names()

    #ask user for Product ID
    while True:
        ProductID = input("Product ID: ").strip().upper()
        if not re.match(pattern,ProductID):
            print("Invalid format. Please try again.")
            continue
        elif ProductID in ExistingIDs:
            print(f"Product ID, {ProductID} already exists. Please Try again.")
            continue
        else:
            break

    while True:
        ProductName = input("Product Name: ")
        if ProductName.replace(' ','').isalpha() == False:
            print("Invalid format. Please try again.")
            continue
        elif ProductName.lower().replace(' ','') in ExistingNames:
            print(f"{ProductName} already exists. Please try again.")
            continue
        else:
            break 

    while True:
        ProductPrice = float(input("Price: $"))
        try:
            if ProductPrice <= 0:
                print("Invalid price, please try agian.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input type. Please try agian.")
            continue

    while True:
        ProductStock = int(input("Stock: "))
        try:
            if ProductStock <= 0:
                print("Invalid stock amount. Please try again.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input type. Please try again.")
            continue
    return ProductID,ProductName,ProductPrice,ProductStock

def get_ProductID(inventory):
    ExistingIDs = inventory.get_IDs()
    while True:
        ProductID = input("Product ID: ").strip().upper()
        if not re.match(pattern,ProductID):
            print("Invalid format. Please try again.")
            continue
        elif ProductID not in ExistingIDs:
            print(f"Product ID, {ProductID} does not exists. Please Try again.")
            continue
        else:
           return ProductID

def get_Stock(ProductId, inventory):
    while True:
        try:
            Stock = int(input("Enter the updated stock quantity: "))
            if Stock == 0:
                for items in inventory.products:
                    if ProductId == items.ProductID:
                        inventory.products.remove(items)
                        return
            elif Stock < 0: #stock cannot be negative
                print("Stock cannot be negative. Please try again.")
                continue
            else:
                for items in inventory.products:
                    if ProductId == items.ProductID:
                        items.update_stock(Stock)
                        print("Stock updated successfully!")
                        items.display_info()
                return
        except ValueError:
                print("Invalid format, please try again.")
                continue
        

load_InventoryFile()
inventory = Inventory()
inventory.load_products(file='inventory.json')





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
                inventory.display_products()
                pass         
            case 2:
                print("\nAdd New Product")
                print("-"*37)
                productInfo = get_ProductInfo(inventory)#call function that gets user to provide product info
                newProduct = Product(productInfo[0],productInfo[1],productInfo[2],productInfo[3]) #create new product object and store in inventory
                inventory.add_product(newProduct)
                pass
            case 3:
                print("\nUpdate Stock")
                print("-"*37)
                ProductID = get_ProductID(inventory)
                inventory.search_product(ProductID)
                #call function to get update stock quantity
                get_Stock(ProductID,inventory)
                pass
            case 4:
                ProductID = get_ProductID(inventory)
                inventory.search_product(ProductID)
                pass
            case 5:
                inventory.save_inventory(file='inventory.json')
                pass
            case 6:
                print("Saving inventory before exit...")
                inventory.save_inventory(file='inventory.json')
                print("Terminating program...")
                break
            case _:
                print("Invalid option")

    print("\n")
