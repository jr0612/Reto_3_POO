class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def calculate_total_price(self, quantity):
        return self.price * quantity

class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

class Appetizer(MenuItem):
    def __init__(self, name, price, servings):
        super().__init__(name, price)
        self.servings = servings

class MainCourse(MenuItem):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price)
        self.ingredients = ingredients

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity=1):
        self.items.append((item, quantity))

    def calculate_total_bill(self):
        total_bill = 0
        for item, quantity in self.items:
            total_bill += item.calculate_total_price(quantity)
        

        if total_bill >= 50:
            discount = total_bill * 0.1  
            total_bill -= discount
        
        return total_bill


if __name__ == "__main__":
    
    cola = Beverage("Cola", 2.5, "Medium")
    wings = Appetizer("Chicken Wings", 8.99, 10)
    steak = MainCourse("Steak", 15.99, ["Beef", "Potatoes", "Vegetables"])

   
    order = Order()
    order.add_item(cola, 16)
    order.add_item(wings)
    order.add_item(steak)


    total_bill = order.calculate_total_bill()
    print("Total Bill: $", total_bill)
