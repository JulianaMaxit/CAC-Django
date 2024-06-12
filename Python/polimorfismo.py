class Circulo:
    def dibujar(self):
        print("O")

class Triangulo:
    def dibujar(self):
        print("A")

class Rectangulo:
    def dibujar(self):
        print("※")

figuras = [Circulo(), Rectangulo(), Triangulo()]

for figura in figuras:
    figura.dibujar()

