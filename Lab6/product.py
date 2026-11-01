class Product:
    def __init__(self, ProductID, Name, Price, Quantity):
        self.ProductID = ProductID
        self.Name = Name
        self.Price = float(Price)
        self.Quantity = int(Quantity)

    #class method for each object to display its own info
    def display_info(self):
        print(f"Product ID:{self.ProductID} | Name:{self.Name} | Price:${self.Price:.2f} | Quantity:{self.Quantity}")

    #class method for each object to update its own quantity
    def update_stock(self, Quantity):
        self.Quantity = Quantity

    def to_dictionary(self):
        return {
            "ID":self.ProductID,
            "Name":self.Name,
            "Price":f"${self.Price:.2f}",
            "Stock":self.Quantity
        }