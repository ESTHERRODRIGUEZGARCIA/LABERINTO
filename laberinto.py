#LABERINTO
print("El laberinto es el siguiente: ")
    
def tablero(LABERINTO, muro):
    LABERINTO = [
    [' E', ' X', ' X', ' X', ' X'], 
    ['  ', ' X', '  ', '  ', '  '],
    ['  ', ' X', '  ', ' X', '  '], 
    ['  ', '  ', '  ', ' X', '  '], 
    [' X', ' X', ' X', ' X', ' S']
    ]

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

            