# 1-mashq
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        return "Men %s" % self.name

class Cat(Animal):
    pass

c = Cat("Mimi")
print(c.info())
# 2-mashq
class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def __init__(self, name, stack):
        super().__init__(name)
        self.stack = stack

dev = Developer("Alim", ["Python", "FastAPI"])
print(dev.name, dev.stack)
# 3-mashq
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

c = Car("BMW", 4)
print(c.brand, c.doors)
# 4-mashq
class PayPal:
    def pay(self, amount):
        return "PayPal orqali %s to‘landi" % amount

class Click:
    def pay(self, amount):
        return "Click orqali %s to‘landi" % amount

def checkout(payment, amount):
    print(payment.pay(amount))

checkout(PayPal(), 1000)
checkout(Click(), 1000)
# 5-mashq
class HtmlRenderer:
    def render(self, text):
        return "<p>%s</p>" % text

class MarkdownRenderer:
    def render(self, text):
        return "**%s**" % text

def show(renderer, text):
    print(renderer.render(text))

show(HtmlRenderer(), "salom")
show(MarkdownRenderer(), "salom")
