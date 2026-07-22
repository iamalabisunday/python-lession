# 1.
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
        
#     def __repr__(self):
#         return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"
    
#     def total_value(self):
#         return self.price * self.quantity

# 2.
class Product:
    def __init__(self, name, price, quantity):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be positive")
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"
    
class ProductNotFoundError(Exception):
    pass

class Inventory:
    def __init__(self):
        self.products = {}  # key: name, value: Product object

    def add_product(self, product):
        self.products[product.name] = product

    def remove_product(self, name):
        if name not in self.products:
            raise ProductNotFoundError(f"{name} not found in inventory")
        del self.products[name]

    def restock(self, name, amount):
        if name not in self.products:
            raise ProductNotFoundError(f"{name} not found in inventory")
        
        if amount < 0:
            raise ValueError("Cannot restock negative amount")

        self.products[name].quantity += amount

    def sell(self, name, amount):
        if name not in self.products:
            raise ProductNotFoundError(f"{name} not found in inventory")
        
        product = self.products[name]

        if amount > product.quantity:
            raise ValueError("Not enough stock")

        product.quantity -= amount

    def total_inventory_value(self):
        return sum(p.total_value() for p in self.products.values())

    def low_stock_report(self, threshold=5):
        return [name for name, p in self.products.items() if p.quantity < threshold]

    def __repr__(self):
        return f"Inventory({list(self.products.keys())})"
    
    
try:
    inv = Inventory()

    p1 = Product("Laptop", 1000, 10)
    p2 = Product("Phone", 500, 3)
    p3 = Product("Tablet", 300, 2)

    inv.add_product(p1)
    inv.add_product(p2)
    inv.add_product(p3)

    print(inv)

    inv.sell("Laptop", 2)
    inv.restock("Phone", 5)

    print("Total value:", inv.total_inventory_value())
    print("Low stock:", inv.low_stock_report())

    inv.remove_product("Tablet")

except ProductNotFoundError as e:
    print("Error:", e)

except ValueError as e:
    print("Error:", e)