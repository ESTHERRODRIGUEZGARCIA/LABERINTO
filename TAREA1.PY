def tablero(LABERINTO):
    muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
    for i in range (12):
        LABERINTO[muro[i][0]][muro[i][1]] = "X"

    for i in range (5):
        print(LABERINTO[i])
            
