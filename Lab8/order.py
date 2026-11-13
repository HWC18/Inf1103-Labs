from orderline import OrderLine
from product import Product, PhysicalProduct, DigitalProduct
from supplier import Supplier
class Order:
    def __init__(self, OrderID: str):
        self.OrderID: str = OrderID
        self.Orders: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.Orders.append(order_line)

    def calculate_total(self):
        total: float = 0
        for order_line in self.Orders:
            total += order_line.calculate_subtotal()
        return total
