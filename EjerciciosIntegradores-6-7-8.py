# Ejercicios Integradores
# Ej. 6
class Persona():
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def get_dni(self):
        return self.dni   
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False 
 
    def set_nombre(self, nombre):
        if nombre != "":
            self.nombre = nombre
        else: print("Debe ingresar un nombre, intente de nuevo")

    def set_edad(self, edad):
        self.edad = edad
        if self.es_mayor_de_edad() == False:
            print("Debe ingresar una edad válida, intente de nuevo")
         
    def set_dni(self, dni):
        if dni != "":
            self.dni = dni
        else:  print("Debe ingresar un DNI, intente de nuevo")
    def mostrar(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.dni}"    
    

        
# Ej. 7
class Cuenta:
    def __init__(self, titular="", cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    def get_titular(self):
        return self.__titular    
    def get_cantidad(self):
        return self.__cantidad
    
    def set_titular(self, titular):
        if titular != "":
            self.__titular = titular
        else: print("Debe ingresar un nombre de Titular, intente de nuevo")

    def mostrar(self):
        return f"Titular: {self.__titular}\nCantidad: ${self.__cantidad}"
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    def retirar(self, cantidad):
        self.__cantidad -= cantidad

# Ej 8
class CuentaJoven(Cuenta):
    def __init__(self, titular:str, bonificacion:int, edad:int, cantidad=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion 
        self.edad = edad
        self.__titular = titular
        self.__cantidad = cantidad

    def get_bonificacion(self):
        return self.bonificacion    
    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def get_titular(self):
        return self.__titular
    def get_edad(self):
        return self.edad
    def get_cantidad(self):
        return self.__cantidad

    def es_titular_valido(self):
        return self.edad >= 18 and self.edad < 25

    def set_titular(self, titular):
        self.__titular = titular

    def set_edad(self, edad):
        self.edad = edad
        if self.es_titular_valido() == False:
            print("Edad inválida. Para una Cuenta joven, la edad debe ser mayor de 18 y menor de 25 años.\n")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
            print(f"Se ingresaron ${cantidad}\n")

    def retirar(self, cantidad):
        if self.es_titular_valido():
            self.__cantidad -= cantidad
            print(f"Se retiraron ${cantidad}\n")
        else:
            print("Edad inválida. Para Retirar La edad debe ser mayor de 18 y menor de 25 años.\n")

    def mostrar(self):

        return f"Cuenta Joven.\nTitular: {self.__titular}\nCantidad: ${self.__cantidad}\nEdad: {self.edad}\nBonificación: {self.bonificacion}"


def main():
    print("--- EJ. 6 -----------------------------------------------------")

    persona = Persona()

    print(persona.mostrar())

    persona.set_nombre("Osvaldo")
    persona.set_edad(50)
    persona.set_dni("19123123")

    print(persona.get_nombre())
    print(persona.get_edad())
    print(persona.get_dni())

    print(persona.mostrar())
    print(persona.es_mayor_de_edad())

    print("--- EJ. 7 -----------------------------------------------------")

    cuenta = Cuenta("Osvaldo")
    print(cuenta.get_titular())
    print(cuenta.get_cantidad())
    cuenta.set_titular("Osvaldo Meijide")

    print(cuenta.mostrar())

    cuenta.ingresar(10_000)
    print(cuenta.mostrar())
    cuenta.retirar(15_000)
    print(cuenta.mostrar())

    print(cuenta.get_cantidad())

    print("--- EJ. 8 -----------------------------------------------------")
# titular:str, bonificacion:int, edad:int, cantidad=0.0
    cuenta_j = CuentaJoven("Osvaldo", 10, 19, 10_000)
    print(cuenta_j.get_titular())
    print(cuenta_j.get_bonificacion())
    print(cuenta_j.get_edad())
    print(cuenta_j.get_cantidad())

    cuenta_j.set_titular("Osvaldo Meijide")
    cuenta_j.set_bonificacion(20)
    cuenta_j.set_edad(22)
    cuenta_j.ingresar(500_000)

    print(cuenta_j.mostrar())

    cuenta_j.retirar(20_000)

    print("Probando cambiar la edad fuera del rango de la cuenta joven")
    cuenta_j.set_edad(40)
    print("Probando retirar con edad fuera del rango de la cuenta joven")
    cuenta_j.retirar(30_000)

    print("Probando retirar con edad dentro del rango de la cuenta joven")
    cuenta_j.set_edad(20)
    print(cuenta_j.get_edad())
    cuenta_j.retirar(30_000)

    print(cuenta_j.mostrar())

    print(cuenta_j.get_cantidad())


if __name__ == "__main__":  
    main()
