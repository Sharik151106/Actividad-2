from enum import Enum

class TipoA(Enum):
    CIUDAD = "CIUDAD"
    SUBCOMPACTO = "SUBCOMPACTO"
    COMPACTO = "COMPACTO"
    FAMILIAR = "FAMILIAR"
    EJECUTIVO = "EJECUTIVO"
    SUV = "SUV"

class TipoColor(Enum):
    BLANCO = "BLANCO"
    NEGRO = "NEGRO"
    ROJO = "ROJO"
    NARANJA = "NARANJA"
    AMARILLO = "AMARILLO"
    VERDE = "VERDE"
    AZUL = "AZUL"
    VIOLETA = "VIOLETA"

class TipoCom(Enum):
    GASOLINA = "GASOLINA"
    BIOETANOL = "BIOETANOL"
    DIESEL = "DIESEL"
    BIODIESEL = "BIODIESEL"
    GAS_NATURAL = "GAS_NATURAL"

class Automovil:
    def __init__(self, marca: str, modelo: int, motor: int,
                 tipo_combustible: TipoCom, tipo_automovil: TipoA,
                 numero_puertas: int, cantidad_asientos: int,
                 velocidad_maxima: int, color: TipoColor,
                 automatico: bool):

        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = 0

        self.automatico = automatico

        self.cantidad_multas = 0
        self.valor_multa = 100000
        self.total_multas = 0

    def get_automatico(self) -> bool:
        return self.automatico

    def set_automatico(self, automatico: bool):
        self.automatico = automatico

    def acelerar(self, incremento_velocidad: int):
        if incremento_velocidad < 0:
            print("El incremento de velocidad no puede ser negativo")
        elif self.velocidad_actual + incremento_velocidad <= self.velocidad_maxima:
            self.velocidad_actual += incremento_velocidad
        else:
            print("No se puede superar la velocidad máxima del automóvil")

            self.cantidad_multas += 1
            self.total_multas += self.valor_multa

            print(f"Multa generada: ${self.valor_multa}")

    def desacelerar(self, decremento_velocidad: int):
        if (self.velocidad_actual - decremento_velocidad) >= 0:
            self.velocidad_actual -= decremento_velocidad
        else:
            print("No se puede decrementar a una velocidad negativa")

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia: int) -> float:
        if self.velocidad_actual == 0:
            return float('inf')
        return distancia / self.velocidad_actual

    def tiene_multas(self) -> bool:
        return self.cantidad_multas > 0

    def calcular_total_multas(self) -> int:
        return self.total_multas

    def imprimir(self):
        print(f"Marca = {self.marca}")
        print(f"Modelo = {self.modelo}")
        print(f"Motor = {self.motor}")
        print(f"Tipo de combustible = {self.tipo_combustible.value}")
        print(f"Tipo de automóvil = {self.tipo_automovil.value}")
        print(f"Número de puertas = {self.numero_puertas}")
        print(f"Cantidad de asientos = {self.cantidad_asientos}")
        print(f"Velocidad máxima = {self.velocidad_maxima}")
        print(f"Color = {self.color.value}")
        print(f"¿Es automático? = {self.get_automatico()}")
    
if __name__ == "__main__":

    auto1 = Automovil(
        "Ford", 2018, 3,
        TipoCom.DIESEL,
        TipoA.EJECUTIVO,
        5, 6, 250,
        TipoColor.NEGRO,
        True
    )
    auto1.imprimir()
    auto1.velocidad_actual = 240
    auto1.acelerar(40)

    print(f"\nVelocidad actual = {auto1.velocidad_actual}")
    print(f"Cantidad de multas = {auto1.cantidad_multas}")
    print(f"Valor Total de multas = ${auto1.calcular_total_multas()}")

    auto1.acelerar(20)
    print(f"Cantidad de multas = {auto1.cantidad_multas}")
    print(f"Valor Total de multas = ${auto1.calcular_total_multas()}")
    

    auto1.desacelerar(50)
    print(f"Velocidad actual = {auto1.velocidad_actual}")

    auto1.frenar()
    print(f"Velocidad actual = {auto1.velocidad_actual}")

    auto1.desacelerar(20)