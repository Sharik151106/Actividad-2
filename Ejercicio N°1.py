class Persona:
    def __init__(self, nombre, apellido, numero_documento,año_nacimiento,pais_nacimiento,genero):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_documento = numero_documento
        self.año_nacimiento = año_nacimiento
        self.pais_nacimiento = pais_nacimiento
        self.genero = genero

    def mostrar_datos_personales(self):
        print(f"Nombre = {self.nombre}")
        print(f"Apellido = {self.apellido}")
        print(f"Número de documento de identidad = {self.numero_documento}")
        print(f"Año de nacimiento = {self.año_nacimiento}")
        print(f"País de Nacimiento = {self.pais_nacimiento}")
        print(f"Género = {self.genero}")
        print()


nombre = input("Ingrese el nombre:\n")
apellido = input("Ingrese el apellido:\n")
numero_documento = input("Ingrese el número de documento de identidad:\n")
año_nacimiento = int(input("Ingrese el año de nacimiento:\n"))
pais_nacimiento = input("Ingrese su país de nacimiento:\n")
genero = input("Ingrese su género(H/M):\n") 

persona1 = Persona(nombre, apellido, numero_documento, año_nacimiento,pais_nacimiento,genero)
persona1.mostrar_datos_personales()

nombre = input("Ingrese el nombre:\n")
apellido = input("Ingrese el apellido:\n")
numero_documento = input("Ingrese el numero de documento de identidad:\n")
año_nacimiento = int(input("Ingrese el año de nacimiento:\n"))
pais_nacimiento = input("Ingrese su país de nacimiento:\n")
genero = input("Ingrese su género(H/M):\n") 

persona2 = Persona(nombre, apellido, numero_documento, año_nacimiento,pais_nacimiento,genero)
persona2.mostrar_datos_personales()

