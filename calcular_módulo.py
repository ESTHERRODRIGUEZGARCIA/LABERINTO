#calcular el módulo del punto (distancia respecto al origen)

from math import sqrt

class Punto:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

def mostrar(self):
    print("Punto ({}, {}, {})".format(self.a, self.b, self.c))


def calculo_modulo(a, b, c):
    return (self.a**2 + self.b**2 + self.c**2) ** (1 / 2)

def calculo_distancia(self, origen):
    origen = Punto(0, 0, 0)
    return ((self.a - origen.a)**2 +(self.b - origen.b)**2 +(self.c - origen.c)**2)**(1/2)

p = Punto(1, 2, 3)
p.mostrar()
