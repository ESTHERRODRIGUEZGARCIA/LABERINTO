#LABERINTO
print("El laberinto es el siguiente: ")
    
def tablero(laberinto, muro):
    tablero = [
    [' E', ' X', ' X', ' X', ' X'], 
    ['  ', ' X', '  ', '  ', '  '],
    ['  ', ' X', '  ', ' X', '  '], 
    ['  ', '  ', '  ', ' X', '  '], 
    [' X', ' X', ' X', ' X', ' S']
    ]

#i van a ser las filas, que son 5. Ya definidas supongo

    for i in range (laberinto):
        fila = []
    return tablero


muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

labyrinth = tablero(5, muro)

for i in labyrinth:
    print("".join(i))




            