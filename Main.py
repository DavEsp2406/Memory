import random

print("Bienvenido al juego de Memory")

tableroVacio = []
tableroEmoji = []
emojisArray = []

emojis = ["😀", "😁", "😂", "🤣", "🤓", "😄", "😅", "😆", "😎", "😐", "🤑", "😭", "😨", "🤯", "🥵"]

# ----------------------ETAPA 1: CREACIÓN DEL TABLERO
crearTablero = False
# bucle para saber cuantas filas y columnas tendra el tablero
while crearTablero == False:
    try:
        f = int(input("Introduce el número de filas (Min = 2x2, Max = 6x5): "))
        c = int(input("Introduce el número de columnas (Min = 2x2, Max = 6x5): "))

        if (f < 2 or f > 6) or (c < 2 or c > 6) or (f == 6 and c == 6):
            print("El número de filas/columnas tiene que estar entre 2 y 6, y no pueden ambas valer 6")
        elif (f * c) % 2 != 0:
            print("El número de filas por columnas debe de ser par")
        else:
            crearTablero = True

    except ValueError:
        print("Por favor, introduce números válidos")

# bucle para crear el tablero vacío
for filas in range(f):
    fila = []
    for columnas in range(c):
        fila.append("-")
    tableroVacio.append(fila)

# bucle para imprimir el tablero vacío
for i in tableroVacio:
    print(" ".join(i))

# bucle con los emojis que van a ser utilizados
while len(emojisArray) != f * c:
    n_aleatorio = random.randint(0, 14)
    if emojis[n_aleatorio] not in emojisArray:
        emojisArray.append(emojis[n_aleatorio])
        emojisArray.append(emojis[n_aleatorio])

# bucle para crear el tablero con emojis
pos = 0
random.shuffle(emojisArray)

for filas in range(f):
    fila = []
    for columnas in range(c):
        fila.append(emojisArray[pos])
        pos += 1
    tableroEmoji.append(fila)

# imprimir tablero emoji

# imprimir tablero emojis
# for i in tableroEmoji:
#     print(" ".join(i))

# ------------------ETAPA 2: JUGADOR CONTRA JUGADOR
print("Tablero creado. ¡Empieza el juego!")


def PvP():
    j1 = input("Introduce el nombre del jugador 1: ")
    j2 = input("Introduce el nombre del jugador 2: ")
    j1P, j2P = 0, 0
    # ---------------- Bucle de la partida jcj
    while True:
        # Turno del jugador 1
        while j1P != len(emojisArray):
            print(f"Turno de {j1}: ")
            try:
                while True:
                    try:
                        print((len(emojisArray)))
                        fc1 = int(input("Selecciona la fila de la primera carta: ")) - 1
                        cc1 = int(input("Selecciona la columna de la primera carta: ")) - 1

                        if 0 <= fc1 < f and 0 <= cc1 < c:
                            if tableroVacio[fc1][cc1] == "-":
                                tableroVacio[fc1][cc1] = tableroEmoji[fc1][cc1]
                                break
                            else:
                                print("No se puede seleccionar una carta ya desvelada")
                        else:
                            print(f"Introduce una posición válida, fila máx: {f} min: 1 y columna máx: {c} min: 1")
                    except ValueError:
                        print("Posición inválida")

                for fila in tableroVacio:
                    print(" ".join(fila))

                while True:
                    try:
                        fc2 = int(input("Selecciona la fila de la segunda carta: ")) - 1
                        cc2 = int(input("Selecciona la columna de la segunda carta: ")) - 1

                        if 0 <= fc2 < f and 0 <= cc2 < c:
                            if tableroVacio[fc2][cc2] == "-":
                                tableroVacio[fc2][cc2] = tableroEmoji[fc2][cc2]
                                break
                            else:
                                print("No se puede seleccionar una carta ya desvelada")
                        else:
                            print(f"Introduce una posición válida, fila máx: {f} min: 1 y columna máx: {c} min: 1")
                    except ValueError:
                        print("Posición inválida")

                for fila in tableroVacio:
                    print(" ".join(fila))

                if tableroVacio[fc1][cc1] == tableroVacio[fc2][cc2]:
                    print("¡Enhorabuena, encontraste una pareja!")
                    j1P += 2
                else:
                    tableroVacio[fc1][cc1] = "-"
                    tableroVacio[fc2][cc2] = "-"
                    print("¡Fallaste!")
                    break
            except ValueError:
                print("Introduce una posición válida.")

        if j1P == len(emojisArray):
            print(f"\nFelicidades {j1}, ganaste la partida con {j1P} puntos")
            break

        # Turno del jugador 2
        while j2P != len(emojisArray):
            print(f"Turno de {j2}: ")
            try:
                while True:
                    try:
                        fc1 = int(input("Selecciona la fila de la primera carta: ")) - 1
                        cc1 = int(input("Selecciona la columna de la primera carta: ")) - 1

                        if 0 <= fc1 < f and 0 <= cc1 < c:
                            if tableroVacio[fc1][cc1] == "-":
                                tableroVacio[fc1][cc1] = tableroEmoji[fc1][cc1]
                                break
                            else:
                                print("No se puede seleccionar una carta ya desvelada")
                        else:
                            print(f"Introduce una posición válida, fila máx: {f} min: 1 y columna máx: {c} min: 1")
                    except ValueError:
                        print("Posición inválida")

                for fila in tableroVacio:
                    print(" ".join(fila))

                while True:
                    try:
                        fc2 = int(input("Selecciona la fila de la segunda carta: ")) - 1
                        cc2 = int(input("Selecciona la columna de la segunda carta: ")) - 1

                        if 0 <= fc2 < f and 0 <= cc2 < c:
                            if tableroVacio[fc2][cc2] == "-":
                                tableroVacio[fc2][cc2] = tableroEmoji[fc2][cc2]
                                break
                            else:
                                print("No se puede seleccionar una carta ya desvelada")
                        else:
                            print(f"Introduce una posición válida, fila máx: {f} min: 1 y columna máx: {c} min: 1")
                    except ValueError:
                        print("Posición inválida")

                for fila in tableroVacio:
                    print(" ".join(fila))

                if tableroVacio[fc1][cc1] == tableroVacio[fc2][cc2]:
                    print("¡Enhorabuena, encontraste una pareja!")
                    j2P += 2
                else:
                    tableroVacio[fc1][cc1] = "-"
                    tableroVacio[fc2][cc2] = "-"
                    print("¡Fallaste!")
                    break
            except ValueError:
                print("Introduce una posición válida.")

        if j2P == len(emojisArray):
            print(f"\nFelicidades {j2}, ganaste la partida con {j2P} puntos")
            break


# Bucle de la partida de jugador contra la CPU
def PvAI():
    j1 = input("Introduce el nombre del jugador 1: ")
    j1P, cpu = 0, 0
    # ---------------- Bucle de la partida jcj
    while True:
        # Turno del jugador 1
        while j1P != len(emojisArray):
            print(f"Turno de {j1}: ")
            try:
                while True:
                    try:
                        fc1 = int(input("Selecciona la fila de la primera carta: ")) - 1
                        cc1 = int(input("Selecciona la columna de la primera carta: ")) - 1

                        if 0 <= fc1 < f and 0 <= cc1 < c:
                            if tableroVacio[fc1][cc1] == "-":
                                tableroVacio[fc1][cc1] = tableroEmoji[fc1][cc1]
                                break
                            else:
                                print("No se puede seleccionar una carta ya desvelada")
                        else:
                            print(f"Introduce una posición válida, fila máx: {f} min: 1 y columna máx: {c} min: 1")
                    except ValueError:
                        print("Posición inválida")

                for fila in tableroVacio:
                    print(" ".join(fila))

                while True:
                    try:
                        fc2 = int(input("Selecciona la fila de la segunda carta: ")) - 1
                        cc2 = int(input("Selecciona la columna de la segunda carta: ")) - 1

                        if 0 <= fc2 < f and 0 <= cc2 < c:
                            if tableroVacio[fc2][cc2] == "-":
                                tableroVacio[fc2][cc2] = tableroEmoji[fc2][cc2]
                                break
                            else:
                                print("No se puede seleccionar una carta ya desvelada")
                        else:
                            print(f"Introduce una posición válida, fila máx: {f} min: 1 y columna máx: {c} min: 1")
                    except ValueError:
                        print("Posición inválida")

                for fila in tableroVacio:
                    print(" ".join(fila))

                if tableroVacio[fc1][cc1] == tableroVacio[fc2][cc2]:
                    print("¡Enhorabuena, encontraste una pareja!")
                    j1P += 2
                else:
                    tableroVacio[fc1][cc1] = "-"
                    tableroVacio[fc2][cc2] = "-"
                    print("¡Fallaste!")
                    break
            except ValueError:
                print("Introduce una posición válida.")

        if j1P == len(emojisArray):
            print(f"\nFelicidades {j1}, ganaste la partida con {j1P} puntos")
            break

        # Turno de la CPU
        while cpu != len(emojisArray):
            memoria = []
            print("Turno de CPU. ")
            try:
                while True:
                    try:
                        fc1 = random.randint(0, f - 1)
                        cc1 = random.randint(0, c - 1)

                        if 0 <= fc1 < f and 0 <= cc1 < c:
                            if tableroVacio[fc1][cc1] == "-":
                                tableroVacio[fc1][cc1] = tableroEmoji[fc1][cc1]
                                break
                            else:
                                print()
                        else:
                            print()
                    except ValueError:
                        print("Posición inválida")

                for fila in tableroVacio:
                    print(" ".join(fila))
                print()

                while True:
                    try:
                        fc2 = random.randint(0, f - 1)
                        cc2 = random.randint(0, c - 1)

                        if 0 <= fc2 < f and 0 <= cc2 < c:
                            if tableroVacio[fc2][cc2] == "-":
                                tableroVacio[fc2][cc2] = tableroEmoji[fc2][cc2]
                                break
                            else:
                                print()
                        else:
                            print(f"Introduce una posición válida, fila máx: {f} min: 1 y columna máx: {c} min: 1")
                    except ValueError:
                        print("Posición inválida")

                for fila in tableroVacio:
                    print(" ".join(fila))

                if tableroVacio[fc1][cc1] == tableroVacio[fc2][cc2]:
                    print("¡Enhorabuena, encontraste una pareja!")
                    cpu += 2
                else:
                    tableroVacio[fc1][cc1] = "-"
                    tableroVacio[fc2][cc2] = "-"
                    print("¡Fallaste!")
                    break
            except ValueError:
                print()

        if cpu == len(emojisArray):
            print(f"\nHa ganado la CPU con {cpu} puntos")
            break


while True:
    print("- Selecciona un modo de juego -")
    print("-------------------------------")
    print("1 - Jugador contra Jugador")
    print("2 - Jugador contra CPU")
    print("3 - CPU vs CPU")

    modo = int(input())

    match modo:
        case 1:
            PvP()
        case 2:
            PvAI()
        case 3:
            print("Hola")
    break
