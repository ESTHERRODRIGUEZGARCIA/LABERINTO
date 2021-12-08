#tarea 2 LABERINTO
#sol: ['Abajo', 'Abajo', 'Abajo', 'Abajo', 'Derecha', 'Derecha', 'Arriba', 'Arriba', 'Derecha', 'Derecha', 'Abajo', 'Abajo', 'Abajo']
def tablero(laberinto, muro):
    tablero = [
    [' E', ' X', ' X', ' X', ' X'], 
    ['  ', ' X', '  ', '  ', '  '],
    ['  ', ' X', '  ', ' X', '  '], 
    ['  ', '  ', '  ', ' X', '  '], 
    [' X', ' X', ' X', ' X', ' S']
    ]

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))



def recorrido(tablero):
        #Consiste en realizar el laberinto, no hay tablero
    fila = columnas = 0
    mov = [' ']
    while (fila < n-1 and columnas < n-1):
        if mov != 'Arriba ' and fila + 1 < n and columnas != 'X':
            fila += 1
            print("Abajo")
        elif mov != 'Abajo' and fila -1 > 0 and columnas != 'X':
            fila -= 1
            print("Arriba")
        elif mov != 'Izquierda' and fila -1 > 0 and columnas != 'X':
            fila -= 1
            print("Derecha")
        elif mov != 'Derecha' and fila -1 > 0 and columnas != 'X':
            fila -= 1
            print("izquierda")
        else:
            print("no hay salida")
            


print("Solución: ", recorrido(tablero))   
