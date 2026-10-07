import json

def load_inventory():
        try:
            with open('inventory.json', 'r') as inventory:
                data =json.load(inventory)
                print("inventory.json found\nInventory loaded successfully.")
                return data
        except FileNotFoundError:
            print("inventory.json not found")
            with open('inventory.json', 'w') as inventory:
                json.dump({}, inventory)
            print("No such file as inventory.json, creating a new file")
            data = {}
            return data



while True:
    print("=====================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("======================================")

    inventory = load_inventory()
    print(inventory)
    break