import time, pygame, clases
import funciones_game as fgame
pygame.init()

#objetos de las clases
pantalla = clases.Pantalla()
celula = clases.Celulas(pantalla, fgame.pedir_num_cel(), fgame.pedir_col_cel())


ventana = pygame.display.set_mode(pantalla.size) #ventana con tamaño

pygame.display.set_caption("Juego de la vida")

ventana.fill(pantalla.color_fondo) #dar el color del fondo


formato_texto = pygame.font.SysFont("Courier", 15)



#estado de celulas, vivas = 1 y muertas = 0
co_estados = []


#bucle
while True:

    # crear copia de los estados llamada co_estados
    co_estados = fgame.copia_matriz(celula.estados)

    ventana.fill(pantalla.color_fondo)

    fgame.imprimir_texto(pantalla, ventana, f"> Generacion: {celula.generacion}", 1, formato_texto)

    fgame.imprimir_texto(pantalla, ventana, f"> Poblacion:  {celula.poblacion}", 2, formato_texto)

    fgame.imprimir_texto(pantalla, ventana, f"> Detenido(space): {pantalla.pause}", 4, formato_texto)

    fgame.imprimir_texto(pantalla, ventana, f"> Frontera(T): {not pantalla.toroide}", 5, formato_texto)

    fgame.imprimir_texto(pantalla, ventana, f"> Normas(flechas): {celula.regla}", 6, formato_texto)

    fgame.imprimir_texto(pantalla, ventana, "> Velocidad con + / -", 8, formato_texto)

    fgame.imprimir_texto(pantalla, ventana, "> Diseño aleatorio con r", 11, formato_texto)

    fgame.imprimir_texto(pantalla, ventana, "> Limpiar hoja con 0", 12, formato_texto)

    fgame.imprimir_texto(pantalla, ventana, "> Poner con click/izq", 14, formato_texto)

    fgame.imprimir_texto(pantalla, ventana, "> Quitar con click/der", 15, formato_texto)


    fgame.imprimir_texto(pantalla, ventana, "> Sugerencias 1: Cañon ", 18, formato_texto)

    fgame.imprimir_texto(pantalla, ventana, "> Sugerencias 2: Palo ", 19, formato_texto)

    fgame.imprimir_texto(pantalla, ventana, "> Sugerencias 3: Estable ", 20, formato_texto)

    fgame.imprimir_texto(pantalla, ventana, "> Sugerencias 4: Penta", 21, formato_texto)

    fgame.imprimir_texto(pantalla, ventana, "> Sugerencias 5: Lineal ", 22, formato_texto)

    fgame.imprimir_texto(pantalla, ventana, "> Sugerencias 6: Tazón ", 24, formato_texto)

    fgame.imprimir_texto(pantalla, ventana, "> Sugerencias 7: Escalado ", 25, formato_texto)

    fgame.imprimir_texto(pantalla, ventana, "> Sugerencias 8: 5 infinito", 26, formato_texto)

    fgame.imprimir_texto(pantalla, ventana, "> Sugerencias 9: Crecimiento", 27, formato_texto)



    #velocidad, si el tiempo de espera es negativo da un aviso y no disminuye
    try:
        time.sleep(pantalla.speed)
    except:
        fgame.imprimir_texto(pantalla, ventana, "Velocidad maxima alcanzada.", 9, formato_texto, (255, 0, 0))



    # Teclado
    fgame.eventos(pantalla, celula, co_estados)



    # dibujar cuadricula
    for x in range(celula.nu_cel[0]):
        for y in range(celula.nu_cel[1]):

            poligono = fgame.cuadros(celula.size_cel_x, celula.size_cel_y, x, y) #se dibuja la cuadricula

            if co_estados[x][y] == False:
                pygame.draw.polygon(ventana, (130, 130, 130), poligono, 1)  # dibujar la cuadricula


            else:
                pygame.draw.polygon(ventana, celula.color_cel, poligono, 0)



            if not pantalla.pause:  # si no esta en pausa


                # ver el numero de vecinos vivos.
                num_vecinos = fgame.numero_vecinos(pantalla, celula.estados, celula.nu_cel[0], celula.nu_cel[1], x, y)

                # reglas.
                fgame.reglas(celula, celula.estados, co_estados, x, y, num_vecinos)

    celula.estados = fgame.copia_matriz(co_estados)


    #cada vez que se hace un ciclo se aumenta 1 la variable de generacion
    if not pantalla.pause:
        celula.generacion += 1

    celula.poblacion = 0 #calcular la poblacion
    for i in celula.estados:
        celula.poblacion += sum(i)

    pygame.display.flip()

pygame.quit()