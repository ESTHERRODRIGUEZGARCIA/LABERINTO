#calcular el módulo del punto (distancia respecto al origen)

from math import sqrt

class Punto:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

def mostrar(self):
    print("Punto ({}, {}, {})".format(self.a, self.b, self.c))


def calculo_modulo(p1,p2):
    return sqrt((p1.a - p2.a)**2 + (p1.b - p2.b)**2)

punto1 = Punto(3, 2)
punto2 = Punto(0, 0)

print("La distancia del punto respecto al origen es de: ")
print(calculo_modulo(punto1, punto2))
