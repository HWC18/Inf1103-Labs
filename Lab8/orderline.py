from product import Product
class OrderLine:
    def __init__(self, Product: Product, Quantity: int):
        self.Product = Product
        self.Quantity = Quantity

    def calculate_subtotal(self) -> float:
        return self.Product.Price * self.Quantity

        