#tarea 2 LABERINTO
#sol: ['Abajo', 'Abajo', 'Abajo', 'Abajo', 'Derecha', 'Derecha', 'Arriba', 'Arriba', 'Derecha', 'Derecha']
def recorrido(tablero):
    #Ahora el tablero es solo de una fila
    fila = 1
    columnas = 10
    movimientos = ['Abajo', 'Arriba', 'Derecha']
    
print("Solución: ", recorrido(tablero))    