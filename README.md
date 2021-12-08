# LABERINTO

Mi dirección de github para este repositorio es la siguiente: https://github.com/ESTHERRODRIGUEZGARCIA/LABERINTO.git

El diagrama de flujo que tenemos en el código es el siguiente: 

![image](https://user-images.githubusercontent.com/91721860/145286562-f470afd1-947e-4279-ad6f-1fad9998e471.png)

El código de la tarea 1:
````
#LABERINTO
print("El laberinto es el siguiente: \nSe empieza en E (Entrada); hay que llegar hasta S(Salida) \n")
    
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

````
El código de la tarea 2:

````
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
    fila = columnas = 1 # son las iniciales
    mov = ['Abajo', 'Abajo', 'Abajo', 'Abajo', 'Derecha', 'Derecha', 'Arriba', 'Arriba', 'Derecha', 'Derecha', 'Abajo', 'Abajo', 'Abajo']

    while (fila < 1 and columnas < 1):
        if mov != 'Arriba' and fila + 1 < 1 and recorrido[fila + 1 ][columnas] != 'X':
            fila += 1
            #la fila sería una más, la columna queda quieta en el recorrido
            print("Abajo")
        elif mov != 'Abajo' and fila -1 > 0 and recorrido[fila - 1 ][columnas] != 'X':
            fila -= 1
            #la fila sería una menos, la columna queda quieta en el recorrido
            print("Arriba")
        elif mov != 'Izquierda' and fila -1 > 1 and recorrido[fila][columnas + 1] != 'X':
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
````
