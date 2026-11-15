"""
Ejercicio 1: Sistema de comida rápida
 
Implementar un paquete llamado ‘products' que tiene dos módulos: ‘food_package.py' y ‘product.py', con la siguiente estructura:

products/
        __init__.py
        food_package.py
        product.py

El módulo food_package.py contendrá una clase abstracta denominada 'FoodPackage' con dos funciones abstractas: 'def pack(self)  -> str ' y 'def material(self) -> str '. Esta clase nos permite crear un tipo específico de paquete o envoltura dependiendo del tipo de alimento a empacar, por ejemplo:

Un vaso de soda puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Una hamburguesa puede ser empacada en un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las siguientes clases ‘Wrapping’, ‘Bottle’, ‘Glass’ y ‘Box’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Wrapping’ se puede definir como:

class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return "Aluminium" 

El módulo 'product.py’ contendrá una clase abstracta denominada 'Product' con dos funciones abstractas: 'def type(self) -> str' y 'def foodPackage(self)-> FoodPackage. Esta clase nos permita crear un producto específico y relacionarlo con su tipo de empaque por ejemplo:

Un producto con código de barras G1, es una soda Sprite cuyo precio es de 5 euros, pertenece al tipo Soda y puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Un producto con código de barras H1, es una hamburguesa Bacon  cuyo precio es de 15 euros, pertenece al tipo Hamburger y puede ser empacado en un paquete un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Hamburger’, ‘Soda’, ‘Drink’ y ‘HappyMeal’, es decir, de forma parecida al módulo anterior, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Hamburger’, se puede definir como:

class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
Implementar un paquete llamado ‘users' que tiene un módulo ‘user.py', con la siguiente estructura:

users/
        __init__.py
        user.py

El módulo 'user.py' contendrá una clase abstracta denominada ‘User’ que tiene un constructor por defecto para los siguientes datos 'def __init__(self, dni:str, name:str, age:int) ', con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Cashier’ y ‘Customer’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Adicionalmente, estas clases se diferencian por los parámetros que reciben sus constructores, por tanto, debemos hacer uso de herencia para inicializar el constructor de la clase padre y agregar características propias a cada clase.  

Implementar un paquete llamado 'util' que tiene dos módulos, denominados 'file_manager.py' y 'converter.py’, con la siguiente estructura:

util/
        __init__.py
        file_manager.py
        converter.py

El módulo ‘file_manager.py' contendrá una clase ‘CSVFileManager’ la cual es una implementaciòn libre y debe incluir las funciones:

La función 'def read(self)' lee un archivo en formato CSV y permite exportar su resultado como un Data Frame.
La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. Esta es una función opcional, se deja al estudiante la implementación.

Los archivos en formato CSV se encuentran en la ruta “data/”, a continuación, se describe el contenido de cada archivo:

cashiers.csv: Información de los cajeros que harán uso del sistema.
customers.csv: Información de los clientes que harán uso del sistema.
drinks.csv: Información de los diferentes tipos de bebidas.
sodas.csv: Información de los diferentes tipos de gaseosas.
hamburgers.csv: Información de los diferentes tipos de hamburguesas.
happyMeal.csv: Información de los diferentes tipos de happy meals.

El módulo 'converter.py' contendrá una clase denominada ‘Converter’ con una función abstracta para convertir las filas de un Data Frame en instancias de objetos. La función sería ‘def convert(self, dataFrame, *args) -> list’. Adicionalmente esta clase debe incluir un método que permite imprimir la información de los objetos ‘def print(self, list)’. En el mismo módulo se deberán incluir las implementaciones específicas que permitan leer los archivos en formato CSV y convertir sus filas en objetos de cada clase utilizando los paquetes product y users.

Implementar un paquete llamado 'orders' que tiene un módulo 'order.py', con la siguiente estructura:

orders/
        __init__.py
        order.py

El módulo 'order.py' contendrá una clase denominada ‘Order’ con un constructor ‘def __init__(self, cashier:Cashier, customer:Customer):’, el cual permite inicializar la clase con los datos del cajero, del cliente y la lista de productos vacía por defecto. Además, debe incluir tres funciones para agregar productos, calcular el total de la orden solicitada y mostrar la información de la orden que está siendo procesada. Las funciones son ‘def add(self, product: Product)', ' def calculateTotal(self) -> float' y ‘def show(self)’, respectivamente.

Finalmente tendremos una clase principal que se llamará ‘PrepareOrder’ en la cual se deberá realizar una implementación que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para finalmente crear una orden. 

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos. 


A grandes rasgos, la aplicación seguiría los siguientes pasos:

1)	Leer archivos en formato csv: 
a.	Leer cada archivo en formato csv: Utilizar una instancia de la clase 'CSVFileManager' y llamar al método 'read()'.
2)	Convertir a listas de objetos:
a.	Convertir cajeros: Función creada por el alumno  
b.	Convertir clientes: Función creada por el alumno 
c.	Convertir productos: Función creada por el alumno 
3)	Preparar Orden:
a.	Buscar cajero por dni: Función creada por el alumno y debe devolver una instancia de tipo cajero.
b.	Buscar cliente por dni. Función creada por el alumno y debe devolver una instancia de tipo cliente.
c.	Inicializar Orden: Utilizar una instancia la clase 'Order', e inicializar con su constructor por defecto.
d.	Mostrar productos a vender: Función creada por el alumno.
e.	Escoger productos: Función creada por el alumno.
f.	Agregar productos: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'add()'.
4)	Mostrar Orden: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'show()'


"""
#Write your code here
from users import Cashier, Customer
from products import Product, Hamburger, Soda, Drink, HappyMeal
from util import (CSVFileManager, CashierConverter, CustomerConverter,
                  ProductConverter)
from orders import Order

    
class PrepareOrder:
    """Classe que fa de "taulell" del caixer: llegeix les dades i
    permet preparar una comanda pas a pas."""

    def __init__(self, data_path: str = "data/"):
        # Els CSV són tots a la carpeta data/
        self.data_path = data_path
        # De moment les llistes estan buides; les omplirem a load_data()
        self.cashiers = []
        self.customers = []
        self.products = []

    # --- Pas 1 i 2: llegir els CSV i passar-los a objectes ---

    def load_data(self):
        """Llegeix els CSV i guarda els caixers, clients i productes."""
        # Primer els caixers: llegim el CSV i el convertim en objectes Cashier
        df_cashiers = CSVFileManager(self.data_path + "cashiers.csv").read()
        cashier_converter = CashierConverter()
        self.cashiers = cashier_converter.convert(df_cashiers)
        print("\nLlista de caixers:")
        cashier_converter.print(self.cashiers)

        # Després els clients, igual que amb els caixers
        df_customers = CSVFileManager(self.data_path + "customers.csv").read()
        customer_converter = CustomerConverter()
        self.customers = customer_converter.convert(df_customers)
        print("\nLlista de clients:")
        customer_converter.print(self.customers)

        # Els productes estan repartits en 4 fitxers. En comptes de repetir
        # el mateix codi 4 vegades, faig una llista amb cada fitxer i la
        # classe que li toca, i ho recorro amb un for.
        product_files = [
            ("hamburgers.csv", Hamburger),
            ("sodas.csv", Soda),
            ("drinks.csv", Drink),
            ("happyMeal.csv", HappyMeal),
        ]
        product_converter = ProductConverter()
        self.products = []
        for file_name, product_class in product_files:
            df_products = CSVFileManager(self.data_path + file_name).read()
            self.products += product_converter.convert(df_products,
                                                       product_class)

    # --- Funcions per buscar ---
    # Totes fan el mateix: recorren la llista i, si troben el que busquem,
    # el retornen. Si no el troben, retornen None.

    def find_cashier(self, dni: str) -> Cashier:
        """Busca un caixer pel DNI."""
        for cashier in self.cashiers:
            if cashier.dni == dni:
                return cashier
        return None

    def find_customer(self, dni: str) -> Customer:
        """Busca un client pel DNI."""
        for customer in self.customers:
            if customer.dni == dni:
                return customer
        return None

    def find_product(self, product_id: str) -> Product:
        """Busca un producte pel seu identificador (H1, G1...)."""
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    # --- Pas 3: preparar la comanda ---

    def ask_cashier(self) -> Cashier:
        """Pas 3a: demana el DNI del caixer.

        Si el DNI no existeix, el torna a demanar (per això el while True).
        """
        while True:
            dni = input("Introdueix DNI del caixer: ").strip()
            cashier = self.find_cashier(dni)
            if cashier is not None:
                print(cashier.describe())
                return cashier
            print("No existeix cap caixer amb aquest DNI. Torna-ho a provar.")

    def ask_customer(self) -> Customer:
        """Pas 3b: el mateix que amb el caixer, però amb el client."""
        while True:
            dni = input("Introdueix DNI del client: ").strip()
            customer = self.find_customer(dni)
            if customer is not None:
                print(customer.describe())
                return customer
            print("No existeix cap client amb aquest DNI. Torna-ho a provar.")

    def show_products(self):
        """Pas 3d: ensenya la carta, és a dir, tots els productes."""
        print("\nLlista de productes:")
        for product in self.products:
            print(product.describe())

    def choose_products(self, order: Order):
        """Passos 3e i 3f: anem demanant productes i els afegim a la comanda
        fins que l'usuari digui que ja no en vol més."""
        while True:
            # Passo l'id a majúscules perquè "g1" també funcioni
            product_id = input(
                "Introdueix l'identificador del producte: ").strip().upper()
            product = self.find_product(product_id)
            if product is not None:
                print(product.describe())
                order.add(product)
            else:
                print("No existeix cap producte amb aquest identificador.")
            # Si la resposta no és "s" o "sí", sortim del bucle
            answer = input("Vols afegir un altre producte? (s/n): ")
            if answer.strip().lower() not in ("s", "si", "sí"):
                break

    def create_order(self):
        """Fa tota la comanda de cap a peus: caixer, client, productes
        i, al final, la mostra amb el total."""
        cashier = self.ask_cashier()
        customer = self.ask_customer()
        # Pas 3c: creem la comanda, que de moment no té cap producte
        order = Order(cashier, customer)
        self.show_products()
        self.choose_products(order)
        # Pas 4: ja la tenim, la mostrem
        print()
        order.show()

    # --- Menú d'opcions ---

    def run(self):
        """Carrega les dades i mostra el menú. Es repeteix fins que
        l'usuari tria 0 per sortir."""
        self.load_data()
        while True:
            print("\n===== MENJAR RÀPID =====")
            print("1. Buscar caixer")
            print("2. Buscar client")
            print("3. Veure productes")
            print("4. Crear una comanda")
            print("0. Sortir")
            option = input("Tria una opció: ").strip()
            if option == "1":
                self.ask_cashier()
            elif option == "2":
                self.ask_customer()
            elif option == "3":
                self.show_products()
            elif option == "4":
                self.create_order()
            elif option == "0":
                print("Fins aviat!")
                break
            else:
                print("Opció no vàlida.")


# Això fa que el programa només s'engegui si executem aquest fitxer
# directament (python prepare_order.py) i no quan s'importa.
if __name__ == "__main__":
    PrepareOrder().run()
