import math

class Circulo:
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self):
        return math.pi * math.pow(self.radio, 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def imprimir(self):
        print("CÍRCULO")
        print(f"Radio = {self.radio} cm")
        print(f"Área = {self.calcular_area():.2f} cm²")
        print(f"Perímetro = {self.calcular_perimetro():.2f} cm")


class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def imprimir(self):
        print("RECTÁNGULO")
        print(f"Base = {self.base} cm")
        print(f"Altura = {self.altura} cm")
        print(f"Área = {self.calcular_area():.2f} cm²")
        print(f"Perímetro = {self.calcular_perimetro():.2f} cm")


class Cuadrado:
    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self):
        return math.pow(self.lado, 2)

    def calcular_perimetro(self):
        return 4 * self.lado

    def imprimir(self):
        print("CUADRADO")
        print(f"Lado = {self.lado} cm")
        print(f"Área = {self.calcular_area():.2f} cm²")
        print(f"Perímetro = {self.calcular_perimetro():.2f} cm")


class TrianguloRectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_hipotenusa(self):
        return math.sqrt(math.pow(self.base, 2) +
                         math.pow(self.altura, 2))

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return (self.base + self.altura +
                self.calcular_hipotenusa())

    def determinar_tipo(self):
        hipotenusa = self.calcular_hipotenusa()

        if math.isclose(self.base, self.altura) and math.isclose(
                self.base, hipotenusa):
            return "Equilátero"
        elif math.isclose(self.base, self.altura) or math.isclose(
                self.base, hipotenusa) or math.isclose(
                self.altura, hipotenusa):
            return "Isósceles"
        else:
            return "Escaleno"

    def imprimir(self):
        print("TRIÁNGULO RECTÁNGULO")
        print(f"Base = {self.base} cm")
        print(f"Altura = {self.altura} cm")
        print(f"Hipotenusa = {self.calcular_hipotenusa():.2f} cm")
        print(f"Área = {self.calcular_area():.2f} cm²")
        print(f"Perímetro = {self.calcular_perimetro():.2f} cm")
        print(f"Tipo de triángulo = {self.determinar_tipo()}")

class Rombo:
    def __init__(self, diagonal_mayor: float, diagonal_menor: float):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def calcular_perimetro(self):
        lado = math.sqrt(
            math.pow(self.diagonal_mayor / 2, 2) +
            math.pow(self.diagonal_menor / 2, 2)
        )
        return 4 * lado

    def imprimir(self):
        print("ROMBO")
        print(f"Diagonal mayor = {self.diagonal_mayor} cm")
        print(f"Diagonal menor = {self.diagonal_menor} cm")
        print(f"El área del rombo es = {self.calcular_area()}")
        print(f"El perímetro del rombo es = {self.calcular_perimetro()}")

class Trapecio:
    def __init__(self, base_mayor: float, base_menor: float,
                 altura: float, lado1: float, lado2: float):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def calcular_perimetro(self):
        return (self.base_mayor + self.base_menor +
                self.lado1 + self.lado2)

    def imprimir(self):
        print("TRAPECIO")
        print(f"Base mayor = {self.base_mayor} cm")
        print(f"Base menor = {self.base_menor} cm")
        print(f"Altura = {self.altura} cm")
        print(f"Lado 1 = {self.lado1} cm")
        print(f"Lado 2 = {self.lado2} cm")
        print(f"El área del trapecio es = {self.calcular_area()}")
        print(f"El perímetro del trapecio es = {self.calcular_perimetro()}")

class PruebaFiguras:
    @staticmethod
    def main():

        circulo = Circulo(2)
        rectangulo = Rectangulo(1, 2)
        cuadrado = Cuadrado(3)
        triangulo = TrianguloRectangulo(3, 4)
        rombo = Rombo(9, 4)
        trapecio = Trapecio(10, 7, 4, 3, 3)

        print(f"El área del círculo es = {circulo.calcular_area()}")
        print(f"El perímetro del círculo es = {circulo.calcular_perimetro()}")
        print()

        print(f"El área del rectángulo es = {rectangulo.calcular_area()}")
        print(f"El perímetro del rectángulo es = {rectangulo.calcular_perimetro()}")
        print()

        print(f"El área del cuadrado es = {cuadrado.calcular_area()}")
        print(f"El perímetro del cuadrado es = {cuadrado.calcular_perimetro()}")
        print()

        print(f"El área del triángulo es = {triangulo.calcular_area()}")
        print(f"El perímetro del triángulo es = {triangulo.calcular_perimetro()}")
        print(f"Es un triángulo {triangulo.determinar_tipo()}")
        print()

        print(f"El área del rombo es = {rombo.calcular_area()}")
        print(f"El perímetro del rombo es = {rombo.calcular_perimetro()}")
        print()

        print(f"El área del trapecio es = {trapecio.calcular_area()}")
        print(f"El perímetro del trapecio es = {trapecio.calcular_perimetro()}")

if __name__ == "__main__":
    PruebaFiguras.main()
