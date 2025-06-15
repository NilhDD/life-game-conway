class Pantalla:

    def __init__(self, size = (650, 650), color_pa = (25, 25, 25)):
        """propiedades de la ventana. tamaño de la ventana, numero de celulas,
        tamaño de las celulas, color de la ventana"""
        self.size = (size[0] + 300,size[1])
        self.color_fondo = color_pa
        self.pause = True
        self.toroide = True
        self.speed = 0.1



class Celulas:

    normas = ["Conway", "Maze"]

    def __init__(self, pantalla, n_cel = (100, 100), color_cel = (255, 255, 255)):
        self.nu_cel = n_cel
        self.color_cel = color_cel
        self.size_cel_x = (pantalla.size[0] - 265)/self.nu_cel[0]
        self.size_cel_y = pantalla.size[1]/self.nu_cel[1]
        self.generacion = 0
        self.poblacion = 0
        self.regla = self.normas[0]
        self.estados = [[False] * self.nu_cel[0] for i in range(self.nu_cel[1])]

    def cambio_reglas_r(self):
        posicion = self.normas.index(self.regla)
        try:
            self.regla = self.normas[posicion + 1]
        except:
            self.regla = self.normas[posicion]

    def cambio_reglas_l(self):
        posicion = self.normas.index(self.regla)
        if posicion != 0:
            self.regla = self.normas[posicion - 1]
        else:
            self.regla = self.normas[posicion]