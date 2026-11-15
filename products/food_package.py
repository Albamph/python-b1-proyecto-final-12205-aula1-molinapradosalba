# Mòdul food_package: els embolcalls on es posarà el menjar
from abc import ABC, abstractmethod


class FoodPackage(ABC):
    """Classe abstracta: el motlle de tots els embolcalls dels productes."""

    @abstractmethod
    def pack(self) -> str:
        """Ens retorna el tipus d'embolcall."""
        pass

    @abstractmethod
    def material(self) -> str:
        """Ens retorna el material del qual està fet l'embolcall."""
        pass

    def describe(self):
        return f"Empaque: {self.pack()} , Material: {self.material()}"


class Wrapping(FoodPackage):
    """Embolcall de paper per a les hamburgueses."""

    def pack(self) -> str:
        return "Food Wrap Paper"

    def material(self) -> str:
        return "Aluminium"


class Bottle(FoodPackage):
    """Ampolla per a les begudes."""

    def pack(self) -> str:
        return "Bottle"

    def material(self) -> str:
        return "Plastic"


class Glass(FoodPackage):
    """Got per als refrescos."""

    def pack(self) -> str:
        return "Glass"

    def material(self) -> str:
        return "Cardboard"


class Box(FoodPackage):
    """Capseta per als Happy Meals."""

    def pack(self) -> str:
        return "Box"

    def material(self) -> str:
        return "Cardboard"
