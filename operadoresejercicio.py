
class Punto:
    """Representa un punto en el espacio"""

    def __init__(self, x, y, z):
        """Método de inicialización de un punto en el espacio"""
        self.x, self.y, self.z = x, y, z

    def distancia(self, other=None):
        """Devuelve la distancia respecto a otro punto o por defecto al origen"""
        if other is None:
            other = Punto(0, 0, 0)
        return ((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2) ** (1 / 2)

##Agregue el operador de suma a la clase Punto, sabiendo que se utiliza el método especial __add__ (y que un punto puede sumarse con otro punto).
    def __add__(self, other):
        """Operador de suma"""
        return Punto(self.x + other.x, self.y + other.y, self.z + other.z)

#Agregue el operador de sustracción (método __sub__) así como el operador de multiplicación (método especial __mul__), sabiendo que un punto se multiplica por un escalar (número).
    def __sub__(self, other):
        """Operador de resta"""
        return Punto(self.x - other.x, self.y - other.y, self.z - other.z)


    def __mul__(self, scalaire):
        """Operador de multiplicación"""
        return self.new_method(scalaire)

    def new_method(self, scalaire):
        return Punto(self.x * scalaire, self.y * scalaire, self.z * scalaire)

    def __iadd__(self, other):
        """Operador de suma en el sitio"""
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        """Operador de resta en el sitio"""
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

#sirve para mejorar el rendimiento y evitar tener que crear un nuevo objeto.
    def __imul__(self, scalaire):
        """Operador de multiplicación en el sitio"""
        self.x *= scalaire
        self.y *= scalaire
        self.z *= scalaire
        return self

#El método especial __str__ es el que se utiliza por print para mostrar un objeto, sea cual sea. Sobrecárguelo para utilizarlo en lugar del método mostrar.
    def __str__(self):
        """Representación de un punto como cadena de caracteres"""
        return "Punto ({self.x}, {self.y}, {self.z})".format(self=self)

print("Evidencia de la optimización")

p = Punto(1, 2, 3)
print(p * 3)

print("Evidencia de un problema de optimización")
print(id(p))
p *= 42
print(id(p))
print(p)
