from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta:
    def __init__(self, nombre, cantidad_satelites, masa, volumen, diametro, distancia_sol, tipo, es_observable, perido_orbital, periodo_rotacion):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable
        self.periodo_orbital = perido_orbital
        self.periodo_rotacion = periodo_rotacion

    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diámetro del planeta = {self.diametro}")
        print(f"Distancia al sol = {self.distancia_sol}")
        print(f"Tipo de planeta = {self.tipo.name}")
        print(f"Es observable = {self.es_observable}")
        print(f"Periodo Orbital en años = {self.periodo_orbital}")
        print(f"Periodo de Rotación en días = {self.periodo_rotacion}")


    def calcular_densidad(self):
        return self.masa / self.volumen if self.volumen != 0 else 0

    def es_planeta_exterior(self):
        limite = 508632758.0
        return self.distancia_sol > limite
    

p1 = Planeta(
    "Tierra", 1, 5.9736E24, 1.08321E12,
    12742, 150000000,TipoPlaneta.TERRESTRE,True, 1, 1);
print("*********************************")
p1.imprimir()
print(f"Densidad del planeta = {p1.calcular_densidad()}")
print(f"Es planeta exterior = {p1.es_planeta_exterior()}")
print("*********************************")

p2 = Planeta(
    "Júpiter", 79, 1.899E27, 1.4313E15,
    139820, 750000000,TipoPlaneta.GASEOSO,True, 11.86,0.41);
print("*********************************")
p2.imprimir()
print(f"Densidad del planeta = {p2.calcular_densidad()}")
print(f"Es planeta exterior = {p2.es_planeta_exterior()}")
print("*********************************")
