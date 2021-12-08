#tarea 2 LABERINTO
#sol: ['Abajo', 'Abajo', 'Abajo', 'Abajo', 'Derecha', 'Derecha', 'Arriba', 'Arriba', 'Derecha', 'Derecha', 'Abajo', 'Abajo', 'Abajo']
def tablero(laberinto, muro):
    tablero = [
    ['  ', ' X', ' X', ' X', ' X'], 
    ['  ', ' X', '  ', '  ', '  '],
    ['  ', ' X', '  ', ' X', '  '], 
    ['  ', '  ', '  ', ' X', '  '], 
    [' X', ' X', ' X', ' X', '  ']
    ]

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))



def recorrido(tablero):
    #Consiste en realizar el laberinto, no hay tablero
    fila = columnas = 0
    mov = ['Abajo', 'Abajo', 'Abajo', 'Abajo', 'Derecha', 'Derecha', 'Arriba', 'Arriba', 'Derecha', 'Derecha', 'Abajo', 'Abajo', 'Abajo']
    
    while (fila < 0 and columnas < 0):
        if mov != 'Arriba' and fila + 1 < 0 and recorrido[fila + 1 ][columnas] != 'X':
            fila += 1
            #la fila sería una más, la columna queda quieta en el recorrido
            print("Abajo")
        elif mov != 'Abajo' and fila -1 > 0 and recorrido[fila - 1 ][columnas] != 'X':
            fila -= 1
            #la fila sería una menos, la columna queda quieta en el recorrido
            print("Arriba")
        elif mov != 'Izquierda' and fila -1 > 0 and recorrido[fila][columnas + 1] != 'X':
            columnas += 1
            #al contrario, la fila queda quieta en el recorrido, la columna sería una más
            print("Derecha")
        elif mov != 'Derecha' and fila -1 > 0 and recorrido[fila][columnas - 1] != 'X':
            columnas -= 1
            #en este caso la columna es la anterior
            print("izquierda")
        else:
            print("no hay salida")
    return mov
            

print("Solución: ", recorrido(tablero))   
