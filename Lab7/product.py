from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, ProductID, Name, Price, Quantity):
        self.ProductID = ProductID
        self.Name = Name
        self.Price = float(Price)
        self.Quantity = int(Quantity)

    #class method for each object to display its own info
    def display_info(self):
        print(f"Product ID:{self.ProductID} | Name:{self.Name} | Price:${self.Price:.2f} | Quantity:{self.Quantity}", end="")

    #class method for each object to update its own quantity
    def update_stock(self, Quantity):
        self.Quantity = Quantity
    @abstractmethod
    def to_dictionary(self): #consider making this an abstact method as well
        pass

    #abstract class method to diplay the fulfilment info of the product
    @abstractmethod
    def get_fulfilment_info(self):
        pass

class CanBeShipped(ABC):
    @abstractmethod
    def get_shipping_info(self):
        pass

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, ProductID, Name, Price, Quantity, Weight):
        super().__init__(ProductID, Name, Price, Quantity)
        self.Weight = float(Weight)

    def display_info(self):
        super().display_info()
        print(f" | Weight: {self.Weight:.2f}Kg")

    def get_fulfilment_info(self):
        print("This product needs to be physically delivered.")

    def get_shipping_info(self):
        shippingCost = self.Weight * 0.25 + (self.Price * 0.25)
        print(f"Shipping cost: ${shippingCost:.2f}")

    def to_dictionary(self):
        return {
            "ProductType": type(self).__name__,
            "ID": self.ProductID,
            "Name": self.Name,
            "Price": f"${self.Price:.2f}",
            "Stock": self.Quantity,
            "Weight": f"{self.Weight:.2f}Kg"
        }

class DigitalProduct(Product):
    def __init__(self, ProductID, Name, Price, Quantity, Download_Size):
            super().__init__(ProductID, Name, Price, Quantity)
            self.Download_Size = float(Download_Size)

    def display_info(self):
        super().display_info()
        print(f" | Download Size: {self.Download_Size}Mb")

    def get_fulfilment_info(self):
        print("This product is delivered digitally.")

    def to_dictionary(self):
            return {
                "ProductType": type(self).__name__,
                "ID": self.ProductID,
                "Name": self.Name,
                "Price": f"${self.Price:.2f}",
                "Stock": self.Quantity,
                "Size": f"{self.Download_Size:.2f}Mb"
            }



#test = PhysicalProduct("P004", "Keyboard", 123.00, 50, 10)
#print(type(test.to_dictionary()["ProductType"]))




