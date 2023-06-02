from abc import ABCMeta, abstractmethod

class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass

class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return "Indian Veg Pizza"

    def createNonVegPizza(self):
        return "Indian Non Veg Pizza"

class USPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return "US Veg Pizza"

    def createNonVegPizza(self):
        return "US Non Veg Pizza"

indian_pizza_factory = IndianPizzaFactory()
print(indian_pizza_factory.createVegPizza())  # "Indian Veg Pizza"

us_pizza_factory = USPizzaFactory()
print(us_pizza_factory.createNonVegPizza())  # "US Non Veg Pizza"
