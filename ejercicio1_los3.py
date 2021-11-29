#Hago los 3 ejercicios aquí

#1. Ejercicio: Cree un método que permita calcular el módulo del punto (distancia respecto al origen).
from math import sqrt
class Punto:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

def mostrar(self):
    print("Punto ({}, {}, {})".format(self.a, self.b, self.c))


def calculo_modulo(self): #el módulo es sólo de un nº
    return (self.a**2 + self.b**2 + self.c**2) ** (1 / 2)

#2. Ejercicio: Cree un método que permita calcular la distancia de un punto en curso respecto a otro.
def calculo_distancia(self, otropunto):
    return((self.a-otropunto.a)**2 + (self.b-otropunto.b)**2 + (self.c-otropunto.c)**2 )**(1/2)

#3. Ejercicio: Cree un método que permita calcular la distancia del punto en curso respecto al origen (es decir, el módulo).
def distacia_punto_origen(self, origen):
    origen == (0, 0, 0)
    return((self.a-origen.a)**2 + (self.b-origen.b)**2 + (self.c-origen.c)**2 )**(1/2)

#Para todos:
p = Punto(13, 23, 8)
p.mostrar()
print("|p| =", p.calculo_modulo())
print("distancia entre p y (1, 2, 5) es ", p.calculo_distancia(Punto(1, 2, 5)))
print("|p| =", p.distancia_punto_origen())
print("distancia entre p y (1, 2, 5) es ", p.distancia_punto_origen(Punto(1, 2, 5)))