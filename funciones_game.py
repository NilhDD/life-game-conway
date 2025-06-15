def copia_matriz(matriz_copia, matriz_original):
    """crear una copia de matriz_copia en matriz_original"""
    matriz_copia = []
    for i in range(len(matriz_original)):
        matriz_copia.append(matriz_original[i].copy())
    return matriz_copia



def reglas(estado_inicial, nuevo_estado, coordX, coordY, vecinos):
    """regla 1: una celula nace si tiene 3 vivas cerca.
       regla 2: una celula sobrevive si tiene 2 o 3 celulas cerca."""
    if estado_inicial[coordX][coordY] == 0 and (vecinos == 3):
        nuevo_estado[coordX][coordY] = 1


    elif estado_inicial[coordX][coordY] == 1 and (vecinos < 2 or vecinos > 3):
        nuevo_estado[coordX][coordY] = 0



def numero_vecinos(estado_inicial, celulasX, celulasY, coordX, coordY):
    """Suma los 8 estados de las celulas que estan cerca de x,y.
    como los estados son 0 y 1 la suma da el numero de celulas vecinas vivas."""
    vecinos = estado_inicial[(coordX - 1) % celulasX][(coordY - 1) % celulasY] + estado_inicial[coordX % celulasX][(coordY - 1) % celulasY] + \
              estado_inicial[(coordX + 1) % celulasX][(coordY - 1) % celulasY] + \
              estado_inicial[(coordX - 1) % celulasX][(coordY) % celulasY] + estado_inicial[(coordX + 1) % celulasX][(coordY) % celulasY] + \
              estado_inicial[(coordX - 1) % celulasX][(coordY + 1) % celulasY] + estado_inicial[(coordX) % celulasX][(coordY + 1) % celulasY] + \
              estado_inicial[(coordX + 1) % celulasX][(coordY + 1) % celulasY]

    return vecinos



def cuadros(tamaño_X, tamaño_Y, coordX, coordY):
    """Crea las coordenadas de los puntos para crear un cuadrado."""
    cuadrado = [((coordY + 1) * tamaño_X, (coordX + 1) * tamaño_Y),
     ((coordY) * tamaño_X, (coordX + 1) * tamaño_Y),
     ((coordY) * tamaño_X, (coordX) * tamaño_Y),
     ((coordY + 1) * tamaño_X, (coordX) * tamaño_Y)]

    return cuadrado


def canon(celulas):
    celulas[5][2] = 1
    celulas[6][2] = 1

    celulas[5][3] = 1
    celulas[6][3] = 1

    celulas[5][12] = 1
    celulas[6][12] = 1
    celulas[7][12] = 1

    celulas[4][13] = 1
    celulas[8][13] = 1

    celulas[9][14] = 1
    celulas[3][14] = 1

    celulas[9][15] = 1
    celulas[3][15] = 1

    celulas[6][16] = 1

    celulas[8][17] = 1
    celulas[4][17] = 1

    celulas[5][18] = 1
    celulas[6][18] = 1
    celulas[7][18] = 1

    celulas[6][19] = 1

    celulas[5][22] = 1
    celulas[4][22] = 1
    celulas[3][22] = 1

    celulas[5][23] = 1
    celulas[4][23] = 1
    celulas[3][23] = 1

    celulas[2][24] = 1
    celulas[6][24] = 1

    celulas[2][26] = 1
    celulas[6][26] = 1
    celulas[1][26] = 1
    celulas[7][26] = 1

    celulas[3][36] = 1
    celulas[4][36] = 1

    celulas[3][37] = 1
    celulas[4][37] = 1