from abc import ABC, abstractmethod


class User(ABC):
  """Motlle de persones"""
  
  def __init__(self, dni: str, name: str, age: int):
    self.dni = dni
    self.name = name
    self.age = age
   
  @abstractmethod
  def describe(self):
    """Ens retornarà el text amb la info de la persona"""


class Cashier(User):
  """És el caixer/a, qui prepara la comanda"""
  
  def __init__(self, dni: str, name: str, age: int, timeTable: str,
               salary: float):
    super().__init__(dni, name, age)
    self.timeTable = timeTable
    self.salary = salary
 
  def describe(self):
        return (f"Cashier - Name: {self.name}, DNI: {self.dni} , "
                f"Timetable: {self.timeTable}, Salary: {self.salary}.")

class Customer(User):
  """persona que realitza la comanda"""
  
  def __init__(self, dni: str, name: str, age: int, email: str,
               postalCode: str):
    super().__init__(dni, name, age)
    self.email = email
    self.postalCode = postalCode


  def describe(self):
        return (f"Customer - Name: {self.name}, DNI: {self.dni} , "
                f"Age: {self.age}, Email: {self.email}, "
                f"Postal Code: {self.postalCode}")
