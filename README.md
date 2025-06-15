# ¿Qué es el Juego de la Vida?

El Juego de la Vida es un **autómata celular** ideado por el matemático **John Horton Conway**. Es una simulación sin jugadores, donde las células evolucionan según reglas simples:

- Una célula viva con menos de 2 vecinos vivos muere (soledad).
- Una célula viva con 2 o 3 vecinos vivos sobrevive.
- Una célula viva con más de 3 vecinos vivos muere (sobrepoblación).
- Una célula muerta con exactamente 3 vecinos vivos revive (nacimiento).

## Requisitos

- Python 3.6 o superior
- [Pygame](https://www.pygame.org/)

## Instala Pygame ejecutando:

```bash
pip install pygame
```
Clona este repositorio:

```bash
Copiar código
git clone https://github.com/NilhDD/life-game-conway.git
cd life-game-conway
```
Ejecuta el archivo principal:

```bash
Copiar código
python game.py
```

