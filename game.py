import time
import pygame
pygame.init()

#tamaño de la pantalla
size = width, height = 700, 650

co_fondo = 25, 25, 25 #color

ventana = pygame.display.set_mode(size) #ventana con tallaño

ventana.fill(co_fondo) #dar el color del fondo


# numero de celulas.
celulasX, celulasY = 60, 60


#tamaño de las celulas dependiendo el tamaño de la ventana
dim_ce_X = (width-1)/celulasX
dim_ce_Y = (height-1)/celulasY


#estado de celulas, vivas = 1 y muertas = 0
estados = [[0]*celulasX for i in range(celulasY)]
co_estados = []


#Pausar
pausa = False


#bucle
while True:

    # crear copia de los estados llamada co_estados
    co_estados=[]
    for i in range(len(estados)):
        co_estados.append(estados[i].copy())


    ventana.fill(co_fondo)
    time.sleep(0.1)


    #Teclado
    space = pygame.event.get()
    for evento in space:
        if evento.type == pygame.KEYDOWN:
            pausa = not pausa

        mouse = pygame.mouse.get_pressed()

        if sum(mouse) > 0:
            coordX, coordY = pygame.mouse.get_pos()
            celdax, celday = int(coordX/dim_ce_X), int(coordY/dim_ce_Y)
            co_estados[celday][celdax] = not mouse[2]



    #dibujar cuadricula
    for x in range(0, celulasX):
        for y in range(0, celulasY):


            """se crea la "cuadricula" donde estaran todas las celulas"""
            poligono = [((y + 1) * dim_ce_X, (x + 1) * dim_ce_Y),
                        ((y) * dim_ce_X, (x + 1) * dim_ce_Y),
                        ((y) * dim_ce_X, (x) * dim_ce_Y),
                        ((y + 1) * dim_ce_X, (x) * dim_ce_Y)]

            if co_estados[x][y] == 0:
                pygame.draw.polygon(ventana, (128, 128, 128), poligono, 1)  # dibujar la cuadricula

            else:
                pygame.draw.polygon(ventana, (255, 255, 255), poligono, 0)



            if not pausa: #pausa o no
                #ver el numero de vecinos vivos
                num_vecinos = estados[(x - 1) % celulasX][(y - 1) % celulasY] + estados[x % celulasX][(y - 1) % celulasY] + estados[(x + 1) % celulasX] [(y - 1) % celulasY] + \
                              estados[(x - 1) % celulasX][(y) % celulasY] +                                                 estados[(x + 1) % celulasX][(y) % celulasY] + \
                              estados[(x - 1) % celulasX][(y + 1) % celulasY] + estados[(x) % celulasX][(y + 1) % celulasY] + estados[(x + 1) % celulasX][(y + 1) % celulasY]


                # regla 2: si una celula muerta tiene 3 vecinos esta nace
                if estados[x][y] == 0 and num_vecinos == 3:
                    co_estados[x][y] = 1


                #regla 1: si una celula tiene menos de 2 o mas de 3 celulas vivas, esta muere
                elif estados[x][y] == 1 and (num_vecinos < 2 or num_vecinos > 3):
                    co_estados[x][y] = 0


    estados=[]
    for j in range(len(co_estados)):
        estados.append(co_estados[j].copy())


    pygame.display.flip()