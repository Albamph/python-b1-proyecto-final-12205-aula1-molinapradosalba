from abc import ABC, abstractmethod
from users import Cashier, Customer


class Converter(ABC):
  """Classe abstracta que és el motlle de tots els conversors"""
  
  @abstractmethod
  def convert(self, dataFrame, *args) -> list:
    """Convertirà cada fila del DataFrame en un objecte"""
    pass
    
  def print(self, objects):
    """Mostra a la pantalla la info de cada objecte"""
    for item in objects:
      print(item.describe())


class CashierConverter(Converter):
  """Converteix les files de cashiers.csv en objectes Cashier"""
  
  def convert(self, dataFrame, *args) -> list:
    cashiers = []
    # Fa el recorregut del DataFrame fila per fila
    for _, row in dataFrame.iterrows():
      # Passem el DNI a text perquè després el puguem
      # comparar amb el que posi el/la caixer/a a input
      cashier = Cashier(str(row["dni"]), row["name"], int(row["age"]),
                        row["timetable"], float(row["salary"]))
      cashiers.append(cashier)
    return cashiers


class CustomerConverter(Converter):
    """Converteix les files de customers.csv en objectes Customer."""

    def convert(self, dataFrame, *args) -> list:
        customers = []
        for _, row in dataFrame.iterrows():
            # Compte: al CSV la columna es diu "postalcode" (tot minúscules)
            customer = Customer(str(row["dni"]), row["name"], int(row["age"]),
                                row["email"], str(row["postalcode"]))
            customers.append(customer)
        return customers


class ProductConverter(Converter):
    """Converteix les files d'un CSV de productes en objectes.

    Com que hi ha diversos tipus de producte, a args[0] rebem la classe
    que s'ha de crear (Hamburger, Soda, Drink o HappyMeal).
    """

    def convert(self, dataFrame, *args) -> list:
        product_class = args[0]
        products = []
        for _, row in dataFrame.iterrows():
            product = product_class(str(row["id"]), row["name"],
                                    float(row["price"]))
            products.append(product)
        return products
