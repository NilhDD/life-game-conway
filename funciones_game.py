class Pantalla:

    def __init__(self, size = (650, 650), n_cel = (100, 100), color_pa = (25, 25, 25), color_cel = (255, 255, 255)):
        """propiedades de la ventana. tamaño de la ventana, numero de celulas,
        tamaño de las celulas, color de la ventana"""
        self.size = size
        self.color_fondo = color_pa
        self.color_cel = color_cel
        self.nu_cel = n_cel
        self.size_cel_x = self.size[0]/self.nu_cel[0]
        self.size_cel_y = self.size[1]/self.nu_cel[1]
        self.pause = False
        self.toroide = True
        self.speed = 0.1



def copia_matriz(matriz_original):
    """crear y retorna una copia de matriz_original"""
    matriz_copia = []
    for i in range(len(matriz_original)):
        matriz_copia.append(matriz_original[i].copy())
    return matriz_copia



def reglas(estado_inicial, nuevo_estado, coordX, coordY, vecinos):
    """regla 1: una celula nace si tiene 3 vivas cerca.
       regla 2: una celula sobrevive si tiene 2 o 3 celulas cerca."""
    if estado_inicial[coordX][coordY] == False and (vecinos == 3):
        nuevo_estado[coordX][coordY] = 1


    elif estado_inicial[coordX][coordY] == True and (vecinos < 2 or vecinos > 3):
        nuevo_estado[coordX][coordY] = 0



def numero_vecinos(pantalla, estado_inicial, celulasX, celulasY, coordX, coordY):
    vecinos = 0
    if not pantalla.toroide: #si toroide es ta en False se restan las celulas de las fronteras.
        if coordX == 0:
            vecinos -= (estado_inicial[(coordX - 1) % celulasX][(coordY - 1) % celulasY]+\
                    estado_inicial[(coordX - 1) % celulasX][(coordY) % celulasY]+\
                    estado_inicial[(coordX - 1) % celulasX][(coordY + 1) % celulasY])

        if coordX == len(estado_inicial)-1:
            vecinos -= (estado_inicial[(coordX + 1) % celulasX][(coordY - 1) % celulasY]+\
                    estado_inicial[(coordX + 1) % celulasX][(coordY) % celulasY]+\
                    estado_inicial[(coordX + 1) % celulasX][(coordY + 1) % celulasY])

        if coordY == 0:
            vecinos -= (estado_inicial[(coordX - 1) % celulasX][(coordY - 1) % celulasY]+\
                    estado_inicial[(coordX) % celulasX][(coordY - 1) % celulasY]+\
                    estado_inicial[(coordX + 1) % celulasX][(coordY - 1) % celulasY])

        if coordY == len(estado_inicial)-1:
            vecinos -= (estado_inicial[(coordX - 1) % celulasX][(coordY + 1) % celulasY]+\
                    estado_inicial[(coordX) % celulasX][(coordY + 1) % celulasY]+\
                    estado_inicial[(coordX + 1) % celulasX][(coordY + 1) % celulasY])


    """Suma los 8 estados de las celulas que estan cerca de x,y.
    como los estados son 0 y 1 la suma da el numero de celulas vecinas vivas."""
    vecinos += estado_inicial[(coordX - 1) % celulasX][(coordY - 1) % celulasY] + estado_inicial[coordX % celulasX][(coordY - 1) % celulasY] + \
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



def eventos(pantalla, matriz):
    """se ven todos los eventos que pueden hacerse.
    1. al presionar el espacio se pausa o despausa.
    2. al darle a la X de la ventana se cierra la ventana.
    3. si se presiona la tecla T se cambia de frontera.
    4. si se presiona + o - se cambia la velocidad.
    5. si se oprime click izq. se coloca una celula viva, si es el click der. se muere"""
    import pygame
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: #si el tipo de evento es QUIT sale del programa
            exit()


        if evento.type == pygame.KEYDOWN:
            """si el tipo de evento es KEYDOWN es decir del teclado, de esta forma
            se pueden tomar todos los eventos del teclado"""
            if pygame.key.name(evento.key) == "space": #si el nombre de la llave es "space" cambia el estado de pausa
                pantalla.pause = not pantalla.pause

            elif pygame.key.name(evento.key) == "t": #si el nombre de la llave es "t" cambia el estado de toroide
                pantalla.toroide = not pantalla.toroide

            elif pygame.key.name(evento.key) == "[+]":
                pantalla.speed -= 0.01

            elif pygame.key.name(evento.key) == "[-]":
                pantalla.speed += 0.01



        mouse = pygame.mouse.get_pressed()
        """get.pressed entrega una tupla de 3 valores booleanos,
        que corresponden a los 3 botones del mouse"""


        if sum(mouse) > 0: #sum() suma los valores que hay dentro de mouse
            """se calcula la posicion de la celula en la que esta el mouse."""
            coordX, coordY = pygame.mouse.get_pos()
            celdax, celday = int(coordX / pantalla.size_cel_x), int(coordY / pantalla.size_cel_y)

            """Y se coloca el valor opuesto al click derecho,
            de tal forma que si se oprime click izq. se crea una celula
            y si se oprime el click derecho se elimina"""
            matriz[celday][celdax] = not mouse[2]



def canon(celulas):
    """patron de ejemplo"""
    celulas[5][2] = True; celulas[6][2] = True

    celulas[5][3] = True; celulas[6][3] = True

    celulas[5][12] = True; celulas[6][12] = True; celulas[7][12] = True

    celulas[4][13] = True; celulas[8][13] = True

    celulas[9][14] = True; celulas[3][14] = True

    celulas[9][15] = True; celulas[3][15] = True

    celulas[6][16] = True

    celulas[8][17] = True; celulas[4][17] = True

    celulas[5][18] = True; celulas[6][18] = True; celulas[7][18] = True

    celulas[6][19] = True

    celulas[5][22] = True; celulas[4][22] = True; celulas[3][22] = True

    celulas[5][23] = True; celulas[4][23] = True; celulas[3][23] = True

    celulas[2][24] = True; celulas[6][24] = True

    celulas[2][26] = True; celulas[6][26] = True; celulas[1][26] = True; celulas[7][26] = True

    celulas[3][36] = True; celulas[4][36] = True

    celulas[3][37] = True; celulas[4][37] = True