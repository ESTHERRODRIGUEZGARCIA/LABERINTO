#tarea 2 LABERINTO
#sol: ['Abajo', 'Abajo', 'Abajo', 'Abajo', 'Derecha', 'Derecha', 'Arriba', 'Arriba', 'Derecha', 'Derecha', 'Abajo', 'Abajo', 'Abajo']
def recorrido(tablero):
    #Consiste en realizar el laberinto, no hay tablero
    fila = columnas = 0
    mov = [' ']
    while (fila < n-1 and columnas < n-1):
        if mov != 'Arriba ' and fila + 1 < n and columnas != 'X':
            fila += 1
            print("Abajo")


print("Solución: ", recorrido(tablero))    