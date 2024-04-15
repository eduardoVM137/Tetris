
import random



# Formas de las piezas
SHAPES = [
    [[1, 1, 1, 1]],#Barra
    [[1, 1], [1, 1]],#cuadro
    [[1, 1, 0], [0, 1, 1]],#Z
    [[0, 1, 1], [1, 1, 0]],#Z invertida
    [[1, 1, 1], [0, 1, 0]],#T
    [[1, 1, 1], [1, 0, 0]],#L IZQ
    [[1, 1, 1], [0, 0, 1]]#L  DER
]

# Colores de las piezas
COLORES = ['R', 'G', 'B', 'Y', 'C', 'M', 'O']

# Función para crear una nueva pieza aleatoria
def crear_pieza():
    forma = random.choice(SHAPES)
    color = random.choice(COLORES)
    return {'forma': forma, 'color': color, 'x': ANCHO // 2 - len(forma[0]) // 2, 'y': 0}

# Función para dibujar el tablero de juego
def dibujar_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))

# Función principal del juego
def jugar_tetris():
    tablero = [['[]' for _ in range(ANCHO)] for _ in range(ALTO)]
    pieza_actual = crear_pieza()

    while True:
        # Dibujar el tablero y la pieza actual
        dibujar_tablero(tablero)
        print()

        # Obtener la entrada del jugador
        movimiento = input("Ingresa 'a' para mover hacia la izquierda, 'd' para mover hacia la derecha o 'q' para salir: ")

        # Salir del juego si el jugador ingresa 'q'
        if movimiento == 'q':
            break

        # Mover la pieza hacia la izquierda
        if movimiento == 'a':
            pieza_actual['x'] -= 1

        # Mover la pieza hacia la derecha
        if movimiento == 'd':
            pieza_actual['x'] += 1

        # Verificar si la posición de la pieza es válida
        if (
            pieza_actual['x'] < 0 or
            pieza_actual['x'] + len(pieza_actual['forma'][0]) > ANCHO or
            pieza_actual['y'] + len(pieza_actual['forma']) > ALTO
        ):
            print("Movimiento inválido")
            continue

        # Colocar la pieza en el tablero
        for y in range(len(pieza_actual['forma'])):
            for x in range(len(pieza_actual['forma'][y])):
                if pieza_actual['forma'][y][x] == 1:
                    tablero[pieza_actual['y'] + y][pieza_actual['x'] + x] = '[' + pieza_actual['color'] + ']'

        # Mover hacia abajo la pieza actual
        pieza_actual['y'] += 1

jugar_tetris()
