#tarea 2 LABERINTO
#sol: ['Abajo', 'Abajo', 'Abajo', 'Abajo', 'Derecha', 'Derecha', 'Arriba', 'Arriba', 'Derecha', 'Derecha', 'Abajo', 'Abajo', 'Abajo']
def recorrido(tablero):
    #Ahora el tablero es solo de una fila
    fila = columnas = 0
    movimientos = ['Abajo', 'Arriba', 'Derecha']

print("Solución: ", recorrido(tablero))    