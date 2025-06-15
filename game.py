import time, pygame
import funciones_game as fgame
pygame.init()


pantalla = fgame.Pantalla()

ventana = pygame.display.set_mode(pantalla.size) #ventana con tallaño

pygame.display.set_caption("Juego de la vida")

ventana.fill(pantalla.color_fondo) #dar el color del fondo



#estado de celulas, vivas = 1 y muertas = 0
estados = [[False]*pantalla.nu_cel[0] for i in range(pantalla.nu_cel[1])]
co_estados = []


fgame.canon(estados)


#bucle
while True:

    # crear copia de los estados llamada co_estados
    co_estados = fgame.copia_matriz(estados)

    ventana.fill(pantalla.color_fondo)

    #velocidad, si el tiempo de espera es negativo da un aviso y no disminuye
    try:
        time.sleep(pantalla.speed)
    except:
        pantalla.speed += 0.01
        print("Velocidad maxima alcanzada.")



    # Teclado
    fgame.eventos(pantalla, co_estados)



    # dibujar cuadricula
    for x in range(pantalla.nu_cel[0]):
        for y in range(pantalla.nu_cel[1]):

            """se crea la "cuadricula" donde estaran todas las celulas"""
            poligono = fgame.cuadros(pantalla.size_cel_x, pantalla.size_cel_y, x, y)

            if co_estados[x][y] == False:
                pygame.draw.polygon(ventana, (130, 130, 130), poligono, 1)  # dibujar la cuadricula


            else:
                pygame.draw.polygon(ventana, pantalla.color_cel, poligono, 0)



            if not pantalla.pause:  # si no esta en pausa

                # ver el numero de vecinos vivos.
                num_vecinos = fgame.numero_vecinos(pantalla, estados, pantalla.nu_cel[0], pantalla.nu_cel[1], x, y)

                # reglas.
                fgame.reglas(estados, co_estados, x, y, num_vecinos)

    estados = fgame.copia_matriz(co_estados)

    pygame.display.flip()

pygame.quit()