import time, pygame
import funciones_game as fgame
pygame.init()

#tamaño de la pantalla
size = width, height = 650, 650

# numero de celulas.
celulasX, celulasY = 100, 100

#tamaño de las celulas dependiendo el tamaño de la ventana
dim_ce_X = (width)/celulasX
dim_ce_Y = (height)/celulasY



ventana = pygame.display.set_mode(size) #ventana con tallaño

co_fondo = 25, 25, 25 #color

ventana.fill(co_fondo) #dar el color del fondo



#estado de celulas, vivas = 1 y muertas = 0
estados = [[0]*celulasX for i in range(celulasY)]
co_estados = []


fgame.canon(estados)

#Pausar
pausa = False


#bucle
while True:

    # crear copia de los estados llamada co_estados
    co_estados = fgame.copia_matriz(co_estados, estados)

    ventana.fill(co_fondo)
    time.sleep(0.1)

    # Teclado

    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            pausa = not pausa

        if evento.type == pygame.QUIT:
            exit()

        mouse = pygame.mouse.get_pressed()

        if sum(mouse) > 0:
            coordX, coordY = pygame.mouse.get_pos()
            celdax, celday = int(coordX / dim_ce_X), int(coordY / dim_ce_Y)
            co_estados[celday][celdax] = not mouse[2]

    # dibujar cuadricula
    for x in range(0, celulasX):
        for y in range(0, celulasY):

            """se crea la "cuadricula" donde estaran todas las celulas"""
            poligono = fgame.cuadros(dim_ce_X, dim_ce_Y, x, y)

            if co_estados[x][y] == 0:
                pygame.draw.polygon(ventana, (130, 130, 130), poligono, 1)  # dibujar la cuadricula


            else:
                pygame.draw.polygon(ventana, (255, 255, 255), poligono, 0)

            if not pausa:  # pausa o no

                # ver el numero de vecinos vivos.
                num_vecinos = fgame.numero_vecinos(estados, celulasX, celulasY, x, y)

                # reglas.
                fgame.reglas(estados, co_estados, x, y, num_vecinos)

    estados = fgame.copia_matriz(estados, co_estados)

    pygame.display.flip()

pygame.quit()