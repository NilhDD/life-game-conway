def vacio(estado, pantalla, celula):
    """pantalla limpia"""
    pantalla.pause = True

    celula.generacion = 1; celula.poblacion = 0

    for i in range(len(estado)):
        for j in range(len(estado[0])):
            estado[i][j] = False



def random(estado, pantalla, celula):
    vacio(estado, pantalla, celula)

    import random
    vida = (True, False)
    for i in range(len(estado)):
        for j in range(len(estado[0])):
            estado[i][j] = random.choice(vida)



def canon(estado, pantalla, celula):
    """patron cañon"""
    vacio(estado, pantalla, celula)

    estado[5][2] = True; estado[6][2] = True

    estado[5][3] = True; estado[6][3] = True

    estado[5][12] = True; estado[6][12] = True; estado[7][12] = True

    estado[4][13] = True; estado[8][13] = True

    estado[9][14] = True; estado[3][14] = True

    estado[9][15] = True; estado[3][15] = True

    estado[6][16] = True

    estado[8][17] = True; estado[4][17] = True

    estado[5][18] = True; estado[6][18] = True; estado[7][18] = True

    estado[6][19] = True

    estado[5][22] = True; estado[4][22] = True; estado[3][22] = True

    estado[5][23] = True; estado[4][23] = True; estado[3][23] = True

    estado[2][24] = True; estado[6][24] = True

    estado[2][26] = True; estado[6][26] = True; estado[1][26] = True; estado[7][26] = True

    estado[3][36] = True; estado[4][36] = True

    estado[3][37] = True; estado[4][37] = True



def palo(estado, pantalla, celula):
    vacio(estado, pantalla, celula)
    cen_x = len(estado[0])//2; cen_y = len(estado)//2

    estado[cen_y][cen_x] = True
    estado[cen_y - 1][cen_x - 1] = True
    estado[cen_y - 1][cen_x] = True
    estado[cen_y][cen_x + 1] = True
    estado[cen_y + 1][cen_x] = True



def estables(estado, pantalla, celula):
    vacio(estado, pantalla, celula)
    cen_x = len(estado[0])//2; cen_y = len(estado)//2

    estado[cen_y][cen_x - 6] = True; estado[cen_y][cen_x - 3] = True; estado[cen_y - 1][cen_x - 5] = True; estado[cen_y - 1][cen_x - 4] = True
    estado[cen_y + 1][cen_x - 5] = True; estado[cen_y + 1][cen_x - 4] = True

    estado[cen_y - 3][cen_x] = True; estado[cen_y - 4][cen_x + 1] = True; estado[cen_y - 5][cen_x + 1] = True;estado[cen_y - 6][cen_x] = True
    estado[cen_y - 5][cen_x - 1] = True; estado[cen_y - 4][cen_x - 1] = True

    estado[cen_y][cen_x + 3] = True; estado[cen_y - 1][cen_x + 4] = True; estado[cen_y - 1][cen_x + 5] = True; estado[cen_y][cen_x + 6] = True
    estado[cen_y][cen_x + 7] = True; estado[cen_y + 1][cen_x + 4] = True; estado[cen_y + 1][cen_x + 5] = True

    estado[cen_y + 3][cen_x] = True; estado[cen_y + 4][cen_x + 1] = True; estado[cen_y + 5][cen_x + 1] = True; estado[cen_y + 6][cen_x] = True
    estado[cen_y + 4][cen_x - 1] = True; estado[cen_y + 5][cen_x - 1] = True


def penta (estado, pantalla, celula):
    vacio(estado, pantalla, celula)

    cen_x = len(estado[0])//2; cen_y = len(estado)//2
    #Figura central
    estado[cen_y][cen_x] = True; estado[cen_y][cen_x -1] = True; estado[cen_y][cen_x -3] = True
    estado[cen_y -1][cen_x] = True; estado[cen_y -1][cen_x +1] = True
    estado[cen_y][cen_x -4] = True; estado[cen_y][cen_x +1] = True; estado[cen_y][cen_x +2] = True
    estado[cen_y][cen_x +4] = True; estado[cen_y][cen_x +5] = True; estado[cen_y -1][cen_x -2] = True
    estado[cen_y +1][cen_x-2] = True; estado[cen_y -1][cen_x +3] = True; estado[cen_y +1][cen_x +3] = True

    #Figura esquina izq up
    estado[cen_y -14][cen_x -11] = True; estado[cen_y -14][cen_x -12] = True; estado[cen_y -14][cen_x -14] = True
    estado[cen_y -14][cen_x - 15] = True; estado[cen_y -14][cen_x -10] = True; estado[cen_y -14][cen_x -9] = True
    estado[cen_y -14][cen_x -7] = True; estado[cen_y -14][cen_x -6] = True; estado[cen_y -15][cen_x -13] = True;
    estado[cen_y -13][cen_x -13] = True; estado[cen_y -15][cen_x -8] = True; estado[cen_y -13][cen_x -8] = True

    #Figura esquina der up
    estado[cen_y -14][cen_x +11] = True; estado[cen_y -14][cen_x +10] = True; estado[cen_y -14][cen_x +8] = True; estado[cen_y -14][cen_x +7] = True
    estado[cen_y -14][cen_x +12] = True; estado[cen_y -14][cen_x +13] = True; estado[cen_y -14][cen_x +15] = True; estado[cen_y -14][cen_x +16] = True
    estado[cen_y -15][cen_x +9] = True; estado[cen_y -13][cen_x +9] = True
    estado[cen_y -15][cen_x +14] = True; estado[cen_y -13][cen_x +14] = True

    #Figura esquina izq down
    estado[cen_y +14][cen_x -11] = True; estado[cen_y +14][cen_x -12] = True; estado[cen_y +14][cen_x -14] = True; estado[cen_y +14][cen_x - 15] = True
    estado[cen_y +14][cen_x -10] = True; estado[cen_y +14][cen_x -9] = True; estado[cen_y +14][cen_x -7] = True; estado[cen_y +14][cen_x -6] = True
    estado[cen_y +15][cen_x -13] = True; estado[cen_y +13][cen_x -13] = True
    estado[cen_y +15][cen_x -8] = True; estado[cen_y +13][cen_x -8] = True

    #Figura esquina der down
    estado[cen_y +14][cen_x +11] = True; estado[cen_y +14][cen_x +10] = True; estado[cen_y +14][cen_x +8] = True; estado[cen_y +14][cen_x +7] = True
    estado[cen_y +14][cen_x +12] = True; estado[cen_y +14][cen_x +13] = True; estado[cen_y +14][cen_x +15] = True; estado[cen_y +14][cen_x +16] = True
    estado[cen_y +15][cen_x +9] = True; estado[cen_y +13][cen_x +9] = True
    estado[cen_y +15][cen_x +14] = True; estado[cen_y +13][cen_x +14] = True


def crecimiento (estado, pantalla, celula):
    vacio(estado, pantalla, celula)

    cen_x = len(estado[0])//2; cen_y = len(estado)//2

    estado[cen_y][cen_x] = True; estado[cen_y][cen_x -1] = True; estado[cen_y][cen_x -2] = True
    estado[cen_y][cen_x -6] = True; estado[cen_y][cen_x -7] = True; estado[cen_y][cen_x -8] = True; estado[cen_y][cen_x -9] = True; estado[cen_y][cen_x -10] = True;
    estado[cen_y][cen_x -12] = True; estado[cen_y][cen_x -13] = True; estado[cen_y][cen_x -14] = True; estado[cen_y][cen_x -15] = True; estado[cen_y][cen_x -16] = True
    estado[cen_y][cen_x -17] = True; estado[cen_y][cen_x -18] = True; estado[cen_y][cen_x -19] = True
    estado[cen_y][cen_x +7] = True; estado[cen_y][cen_x +8] = True; estado[cen_y][cen_x +9] = True; estado[cen_y][cen_x +10] = True; estado[cen_y][cen_x +11] = True
    estado[cen_y][cen_x +12] = True; estado[cen_y][cen_x +13] = True; estado[cen_y][cen_x +15] = True; estado[cen_y][cen_x +16] = True; estado[cen_y][cen_x +17] = True
    estado[cen_y][cen_x +18] = True; estado[cen_y][cen_x +19] = True



def tech (estado, pantalla, celula):
    vacio(estado, pantalla, celula)

    cen_x = len(estado[0])//2; cen_y = len(estado)//2

    estado[cen_y][cen_x] = True; estado[cen_y][cen_x -1] = True; estado[cen_y][cen_x +1] = True
    estado[cen_y +1][cen_x -2] = True; estado[cen_y +1][cen_x +2] = True
    estado[cen_y +2][cen_x -3] = True; estado[cen_y +2][cen_x +3] = True
    estado[cen_y +3][cen_x -3] = True; estado[cen_y +3][cen_x +3] = True


def diez_inf (estado, pantalla, celula):
    vacio(estado, pantalla, celula)

    cen_x = len(estado[0])//2; cen_y = len(estado)//2

    estado[cen_y][cen_x] = True; estado[cen_y][cen_x +2] = True;estado[cen_y -1][cen_x +2] = True
    estado[cen_y -2][cen_x + 4] = True; estado[cen_y -3][cen_x + 4] = True; estado[cen_y -4][cen_x + 4] = True
    estado[cen_y -3][cen_x + 6] = True; estado[cen_y -4][cen_x + 6] = True; estado[cen_y -5][cen_x + 6] = True
    estado[cen_y -4][cen_x + 7] = True


def cinco_inf (estado, pantalla, celula):
    vacio(estado, pantalla, celula)

    cen_x = len(estado[0])//2; cen_y = len(estado)//2

    estado[cen_y][cen_x] = True; estado[cen_y -3][cen_x] = True; estado[cen_y -4][cen_x] = True; estado[cen_y -1][cen_x +1] = True
    estado[cen_y -4][cen_x +1] = True; estado[cen_y][cen_x +2] = True; estado[cen_y -1][cen_x +2] = True; estado[cen_y -4][cen_x +2] = True
    estado[cen_y -2][cen_x +3] = True; estado[cen_y][cen_x +4] = True; estado[cen_y -1][cen_x +4] = True; estado[cen_y -2][cen_x +4] = True
    estado[cen_y -4][cen_x +4] = True


def inf_lin(estado, pantalla, celula):
    vacio(estado, pantalla, celula)

    cen_x = len(estado[0])//2; cen_y = len(estado)//2

    estado[cen_y][cen_x] = True;  estado[cen_y][cen_x -1] = True; estado[cen_y-1][cen_x-1] = True; estado[cen_y][cen_x-2] = True; estado[cen_y-1][cen_x-2] = True
    estado[cen_y][cen_x-3] = True; estado[cen_y][cen_x-4] = True; estado[cen_y][cen_x-5] = True; estado[cen_y-1][cen_x-5] = True; estado[cen_y-1][cen_x+1] = True
    estado[cen_y][cen_x+2] = True; estado[cen_y -1][cen_x+2] = True; estado[cen_y][cen_x+3] = True; estado[cen_y -1][cen_x+3] = True; estado[cen_y][cen_x+2] = True
    estado[cen_y -1][cen_x+4] = True; estado[cen_y][cen_x+6] = True; estado[cen_y -1][cen_x+6] = True
