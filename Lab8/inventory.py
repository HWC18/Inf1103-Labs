import json
from product import Product, PhysicalProduct, DigitalProduct
from supplier import Supplier
from dataclasses import dataclass

class Inventory:
    def __init__(self):
        self.products : list[Product] = []

    def get_IDs(self):
        existing_IDs = []
        for items in self.products:
            existing_IDs.append(items.ProductID)
        return existing_IDs

    def get_Names(self):
        existing_Names = []
        for items in self.products:
            existing_Names.append(items.Name.lower().replace(' ',''))
        return existing_Names
    
    def load_products(self, file): #this function loads the JSON file, then converts each item into a object in the Product class and then places them back in the list
        with open(file, 'r') as inventoryFile:
            for items in json.load(inventoryFile):
                if items["ProductType"] == "PhysicalProduct":
                    items = PhysicalProduct(ProductID=items["ID"],Name=items["Name"],Price=float(items["Price"].replace('$','')),Quantity=items["Stock"],Weight=float(items["Weight"].replace("Kg",'')),
                                            Supplier=Supplier(SupplierID=items["Supplier"]["SupplierID"], Name=items["Supplier"]["Name"], ContactEmail=items["Supplier"]["ContactEmail"]))

                elif items["ProductType"] == "DigitalProduct":
                    items = DigitalProduct(ProductID=items["ID"],Name=items["Name"],Price=float(items["Price"].replace('$','')),Quantity=items["Stock"],Download_Size=float(items["Size"].replace("Mb",'')),
                                           Supplier=Supplier(SupplierID=items["Supplier"]["SupplierID"], Name=items["Supplier"]["Name"], ContactEmail=items["Supplier"]["ContactEmail"]))
                self.products.append(items)
        print("inventory successfully loaded\n")
        return

    def display_products(self):
        print("\nCurrent Inventory")
        print("-"*37)
        if not self.products:
            print("No products found in the inventory")
            return
        else:
            for items in self.products:
                items.display_info()
                items.get_fulfilment_info()
        return

    def search_product(self,productID):
        for items in self.products:
            if items.ProductID == productID:
                print("\nProduct Found")
                print("-"*37)
                print(f"Product ID: {items.ProductID}")
                print(f"Name: {items.Name}")
                print(f"Stock: {items.Quantity}")
                items.get_fulfilment_info()
                if type(items).__name__ == "PhysicalProduct":
                    items.get_shipping_info()

    def add_product(self, product):
        self.products.append(product)
        print("Product successfully added.")

    def remove_product(self, productID: str):
        for items in self.products:
            if productID == items.ProductID:
                popped = self.products.pop(self.products.index(items))
        return popped
    
    def save_inventory(self,file):
        test = []
        with open(file,'w') as inventoryFile:
            for items in self.products:
                test.append(items.to_dictionary())
            json.dump(test, inventoryFile, indent=4)
        print("Inventory saved successfully!")


