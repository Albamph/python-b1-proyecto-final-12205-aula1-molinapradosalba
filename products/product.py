from abc import ABC, abstractmethod
from .food_package import FoodPackage, Wrapping, Bottle, Glass, Box


class Product(ABC):
    """Una classe abstracta, el motlle dels productes"""
    def __init__(self, id: str, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price
    
    def describe(self):
        return (f"Product - Type: {self.type()}, Name: {self.name}, "
                f"Id: {self.id} , Price: {self.price} , "
                f"{self.foodPackage().describe()}.")
    
    @abstractmethod
    def type(self) -> str:
        """Retornarà el tipus de producte"""
        pass
        
    @abstractmethod
    def foodPackage(self) -> FoodPackage:
        """Aquí retorna l'embolcall que es fa servir amb el producte"""
        pass


class Hamburger(Product):
    """L'hamburguersa va embolicada amb el paper"""
    
    def __init__(self, id: str, name: str, price: float):
        super().__init__(id, name, price)
        
    def type(self) -> str:
        return "Hamburguesa"
        
    def foodPackage(self) -> FoodPackage:
        return Wrapping()


class Soda(Product):
    """Refresc, per tant es serveix en un got."""

    def __init__(self, id: str, name: str, price: float):
        super().__init__(id, name, price)

    def type(self) -> str:
        return "Refresco"

    def foodPackage(self) -> FoodPackage:
        return Glass()


class Drink(Product):
    """Beguda, per això es serveix en una ampolla."""

    def __init__(self, id: str, name: str, price: float):
        super().__init__(id, name, price)

    def type(self) -> str:
        return "Bebida"

    def foodPackage(self) -> FoodPackage:
        return Bottle()


class HappyMeal(Product):
    """Menú infantil, es serveix en una capseta."""

    def __init__(self, id: str, name: str, price: float):
        super().__init__(id, name, price)

    def type(self) -> str:
        return "Happy Meal"

    def foodPackage(self) -> FoodPackage:
        return Box()
