def pedir_num_cel():
    while True:
        try:
            num_cel = input("\nNumero de celulas en X y Y (g para opcines predeterminadas):")

            if num_cel.upper() == "G":
                num_cel = 100
                break

            num_cel = int(num_cel)

            if 50 <= num_cel <= 200:
                break
            print("Debe de ingresar un numero entero mayor a 50 y menor a 200.\n")

        except:
            print("Debe de ingresar un numero entero mayor a 50 y menor a 200.\n")

    return num_cel, num_cel



def pedir_col_cel():
    while True:
        try:
            color = input("\nIngrese el codigo en rgb del color separelos con , (g para opcines predeterminadas):")

            if color.upper() == "G":
                color = "255,255,255"

            color = color.split(",")

            if len(color) == 3:
                for i in range(3):
                    color[i] = int(color[i])

                if (0 <= color[0] <= 255) and (0 <= color[1] <= 255) and (0 <= color[2] <= 255):
                    return color[0], color[1], color[2]

            else:
                color[0] == int("A")

        except:
            print("\nDebe de ingresar tres enteros que esten entre 0 y 255")



def imprimir_texto(pantalla, ventana, str, num_texto, formato_texto, color = (255, 255, 255)):
    texto = formato_texto.render(str, True, color)
    ventana.blit(texto, (pantalla.size[0]-260, ((num_texto - 1)*20) + 10))



def copia_matriz(matriz_original):
    """crear y retorna una copia de matriz_original"""
    matriz_copia = []
    for i in range(len(matriz_original)):
        matriz_copia.append(matriz_original[i].copy())
    return matriz_copia



def reglas(celula, estado_inicial, nuevo_estado, coordX, coordY, vecinos):
    """diferentes reglas que pueden haber."""
    if celula.regla == "Conway":
        """regla 1: una celula nace si tiene 3 vivas cerca.
        regla 2: una celula sobrevive si tiene 2 o 3 celulas cerca."""
        if estado_inicial[coordX][coordY] == False and (vecinos == 3):
            nuevo_estado[coordX][coordY] = 1


        elif estado_inicial[coordX][coordY] == True and (vecinos < 2 or vecinos > 3):
            nuevo_estado[coordX][coordY] = 0

    elif celula.regla == "Maze":
        """regla 1: una celula nace si tiene 3 vivas cerca.
        regla 2: una celula sobrevive si tiene 1 o 5 celulas cerca."""
        if estado_inicial[coordX][coordY] == False and (vecinos == 3):
            nuevo_estado[coordX][coordY] = 1


        elif estado_inicial[coordX][coordY] == True and (vecinos < 1 or vecinos > 5):
            nuevo_estado[coordX][coordY] = 0

    elif celula.regla == "Day&Night":
        if estado_inicial[coordX][coordY] == False and (vecinos == 3 or vecinos >= 6):
            nuevo_estado[coordX][coordY] = 1


        elif estado_inicial[coordX][coordY] == True and (vecinos < 3 or vecinos == 5):
            nuevo_estado[coordX][coordY] = 0

    elif celula.regla == "Coral":
        if estado_inicial[coordX][coordY] == False and (vecinos == 3):
            nuevo_estado[coordX][coordY] = 1


        elif estado_inicial[coordX][coordY] == True and (vecinos < 4):
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



def eventos(pantalla, celula, matriz):
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
            import sugerencia
            """si el tipo de evento es KEYDOWN es decir del teclado, de esta forma
            se pueden tomar todos los eventos del teclado"""
            if pygame.key.name(evento.key) == "space": #si el nombre de la llave es "space" cambia el estado de pausa
                pantalla.pause = not pantalla.pause

            elif pygame.key.name(evento.key) == "t": #si el nombre de la llave es "t" cambia el estado de toroide
                pantalla.toroide = not pantalla.toroide

            #velocidad
            elif pygame.key.name(evento.key) == "[+]" or pygame.key.name(evento.key) == "+":
                pantalla.speed -= 0.01

            elif pygame.key.name(evento.key) == "[-]" or pygame.key.name(evento.key) == "-":
                pantalla.speed += 0.01

            #sugerencias
            elif pygame.key.name(evento.key) == "[0]" or pygame.key.name(evento.key) == "0":
                sugerencia.vacio(matriz, pantalla, celula)

            elif pygame.key.name(evento.key) == "r":
                sugerencia.random(matriz, pantalla, celula)

            elif pygame.key.name(evento.key) == "[1]" or pygame.key.name(evento.key) == "1":
                sugerencia.canon(matriz, pantalla, celula)

            elif pygame.key.name(evento.key) == "[2]" or pygame.key.name(evento.key) == "2":
                sugerencia.palo(matriz, pantalla, celula)

            elif pygame.key.name(evento.key) == "[3]" or pygame.key.name(evento.key) == "3":
                sugerencia.estables(matriz, pantalla, celula)

            elif pygame.key.name(evento.key) == "[4]" or pygame.key.name(evento.key) == "4":
                sugerencia.penta(matriz, pantalla, celula)

            elif pygame.key.name(evento.key) == "[5]" or pygame.key.name(evento.key) == "5":
                sugerencia.crecimiento(matriz, pantalla, celula)

            elif pygame.key.name(evento.key) == "[6]" or pygame.key.name(evento.key) == "6":
                sugerencia.tech(matriz, pantalla, celula)

            elif pygame.key.name(evento.key) == "[7]" or pygame.key.name(evento.key) == "7":
                sugerencia.diez_inf(matriz, pantalla, celula)

            elif pygame.key.name(evento.key) == "[8]" or pygame.key.name(evento.key) == "8":
                sugerencia.cinco_inf(matriz, pantalla, celula)

            elif pygame.key.name(evento.key) == "[9]" or pygame.key.name(evento.key) == "9":
                sugerencia.inf_lin(matriz, pantalla, celula)

            #reglas
            elif pygame.key.name(evento.key) == "right":
                celula.cambio_reglas_r()

            elif pygame.key.name(evento.key) == "left":
                celula.cambio_reglas_l()





        #eventos de mouse
        mouse = pygame.mouse.get_pressed()
        """get.pressed entrega una tupla de 3 valores booleanos,
        que corresponden a los 3 botones del mouse"""

        try:
            if sum(mouse) > 0: #sum() suma los valores que hay dentro de mouse
                """se calcula la posicion de la celula en la que esta el mouse."""
                coordX, coordY = pygame.mouse.get_pos()
                celdax, celday = int(coordX / celula.size_cel_x), int(coordY /celula.size_cel_y)

                """Y se coloca el valor opuesto al click derecho,
                de tal forma que si se oprime click izq. se crea una celula
                y si se oprime el click derecho se elimina"""
                matriz[celday][celdax] = not mouse[2]
        except:
            continue