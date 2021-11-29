#calcular el módulo del punto (distancia respecto al origen)

from _typeshed import Self
from math import sqrt

class Punto:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

def mostrar(self):
    print("Punto ({}, {}, {})".format(self.a, self.b, self.c))


def calculo_modulo(a, b, c):
    return (Self.a**2 + Self.b**2 + Self.c**2) ** (1 / 2)

def calculo_distancia(self, origen):
    origen = (0, 0, 0)
    return ((Self.a - origen.a)**2 +(Self.b - origen.b)**2 +(Self.c - origen.c)**2)**(1/2)
