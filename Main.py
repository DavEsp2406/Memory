import random
import time
from collections import OrderedDict

print("Bienvenido al juego de Memory")

tableroVacio = []
tableroEmoji = []
emojisArray = []
memoria_cpu = {}
memoria_cpu1 = {}
memoria_cpu2 = {}


emojis = ["😀", "😁", "😂", "🤣", "🤓", "😄", "😅", "😆", "😎", "😐", "🤑", "😭", "😨", "🤯", "🥵"]

# ----------------------ETAPA 1: CREACIÓN DEL TABLERO
crearTablero = False
# bucle para saber cuantas filas y columnas tendra el tablero
while not crearTablero:
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


def pvp():
    j1 = input("Introduce el nombre del jugador 1: ")
    j2 = input("Introduce el nombre del jugador 2: ")
    j1P, j2P = 0, 0
    total = len(emojisArray) // 2
    pTotales = 0
    j1Acierta, j2Acierta = True, True

    # ---------------- Bucle de la partida jcj
    while pTotales < total:
        # Turno del jugador 1
        while j1Acierta and pTotales < total:
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
                    pTotales += 1
                else:
                    tableroVacio[fc1][cc1] = "-"
                    tableroVacio[fc2][cc2] = "-"
                    print("¡Fallaste!")
                    j1Acierta, j2Acierta = False, True
            except ValueError:
                print("Introduce una posición válida.")

        if j1P == len(emojisArray):
            print(f"\nFelicidades {j1}, ganaste la partida con {j1P} puntos")
            break

        # Turno del jugador 2
        while j2Acierta and pTotales < total:
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
                    pTotales += 1
                else:
                    tableroVacio[fc1][cc1] = "-"
                    tableroVacio[fc2][cc2] = "-"
                    print("¡Fallaste!")
                    j1Acierta, j2Acierta = True, False
            except ValueError:
                print("Introduce una posición válida.")

        if j1P > j2P:
            print(f"\n¡Felicidades {j1}! Ganaste la partida con {j1P} puntos")
        elif j2P > j1P:
            print(f"\n¡Felicidades {j2}! Ganaste la partida con {j2P} puntos")
        else:
            print(f"\n¡Es un empate!")

# -------------------------------Bucle de la partida de jugador contra la CPU
def pvcpu(n):
    j1 = input("Introduce el nombre del jugador 1: ")
    j1P, cpu = 0, 0
    total = len(emojisArray) // 2
    pTotales = 0
    memoria_cpu = OrderedDict()
    j1Acierta, j2Acierta = True, True
    # ---------------- Bucle de la partida jcj
    while pTotales < total:
        # Turno del jugador 1
        while j1Acierta and pTotales < total:
            print(f"\nTurno de {j1}: ")
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
                    pTotales += 1
                else:
                    tableroVacio[fc1][cc1] = "-"
                    tableroVacio[fc2][cc2] = "-"
                    print("¡Fallaste!")
                    j1Acierta, j2Acierta = False, True
                    break
            except ValueError:
                print("Introduce una posición válida.")

        # Turno de la CPU
        while j2Acierta and pTotales < total:
            print("\nTurno de CPU. ")
            try:
                while True:
                    try:
                        if n == 1:
                            fc1 = random.randint(0, f - 1)
                            cc1 = random.randint(0, c - 1)
                        elif n == 2 or n == 3:
                            if memoria_cpu:
                                fc1, cc1 = random.choice(list(memoria_cpu.keys()))
                            else:
                                fc1 = random.randint(0, f - 1)
                                cc1 = random.randint(0, c - 1)

                        if 0 <= fc1 < f and 0 <= cc1 < c:
                            if tableroVacio[fc1][cc1] == "-":
                                tableroVacio[fc1][cc1] = tableroEmoji[fc1][cc1]
                                if n == 2:
                                    if len(memoria_cpu) >= 2:
                                        memoria_cpu.popitem(last=False)
                                    else:
                                        memoria_cpu[(fc1, cc1)] = tableroEmoji[fc1][cc1]
                                if n == 3:
                                    memoria_cpu[(fc1, cc1)] = tableroEmoji[fc1][cc1]
                                break
                    except ValueError:
                        print("Posición inválida")

                for fila in tableroVacio:
                    print(" ".join(fila))
                print()

                time.sleep(1.5)

                while True:
                    try:
                        pEncontrada = False

                        for k, v in memoria_cpu.items():
                            if v == tableroEmoji[fc1][cc1] and k != (fc1, cc1):
                                fc2, cc2 = k
                                pEncontrada = True
                                break

                        if not pEncontrada:
                            fc2 = random.randint(0, f - 1)
                            cc2 = random.randint(0, c - 1)

                        if 0 <= fc2 < f and 0 <= cc2 < c:
                            if tableroVacio[fc2][cc2] == "-":
                                tableroVacio[fc2][cc2] = tableroEmoji[fc2][cc2]
                                if n == 2:
                                    if len(memoria_cpu) >= 2:
                                        memoria_cpu.popitem(last=False)
                                    else:
                                        memoria_cpu[(fc2, cc2)] = tableroEmoji[fc2][cc2]
                                if n == 3:
                                    memoria_cpu[(fc2, cc2)] = tableroEmoji[fc2][cc2]
                                break
                    except ValueError:
                        print("Posición inválida")

                for fila in tableroVacio:
                    print(" ".join(fila))

                time.sleep(1.5)

                if tableroVacio[fc1][cc1] == tableroVacio[fc2][cc2]:
                    print("¡Enhorabuena, encontraste una pareja!")
                    cpu += 2
                    pTotales += 1
                    memoria_cpu.pop((fc1, cc1), None)
                    memoria_cpu.pop((fc2, cc2), None)
                else:
                    tableroVacio[fc1][cc1] = "-"
                    tableroVacio[fc2][cc2] = "-"
                    print("¡Fallaste!")
                    j1Acierta, j2Acierta = True, False
            except ValueError:
                print()

    if j1P > cpu:
        print(f"\n¡Felicidades {j1}! Ganaste la partida con {j1P} puntos")
    elif cpu > j1P:
        print(f"\nHa ganado la partida la CPu con {cpu} puntos")
    else:
        print(f"\n¡Es un empate!")

#------------Bucle de la partida del modo de juego CPu vs CPU
def cpuvcpu(n):
    cpu1, cpu2 = 0, 0
    j1Acierta, j2Acierta = True, True
    memoria_cpu1 = OrderedDict()
    memoria_cpu2 = OrderedDict()
    pTotales = 0
    total = len(emojisArray) // 2
    while pTotales < total:
        # Turno de la CPU1
        while j1Acierta and pTotales < total:
            time.sleep(1.5)
            print("\nTurno de la CPU 1. ")
            try:
                while True:
                    try:
                        if n == 1:
                            fc1 = random.randint(0, f - 1)
                            cc1 = random.randint(0, c - 1)
                        elif n == 2 or n == 3:
                            if memoria_cpu1:
                                fc1, cc1 = random.choice(list(memoria_cpu1.keys()))
                            else:
                                fc1 = random.randint(0, f - 1)
                                cc1 = random.randint(0, c - 1)

                        if 0 <= fc1 < f and 0 <= cc1 < c:
                            if tableroVacio[fc1][cc1] == "-":
                                tableroVacio[fc1][cc1] = tableroEmoji[fc1][cc1]
                                if n == 2:
                                    if len(memoria_cpu1) >= 2:
                                        memoria_cpu1.popitem(last=False)
                                    else:
                                        memoria_cpu1[(fc1, cc1)] = tableroEmoji[fc1][cc1]
                                if n == 3:
                                    memoria_cpu1[(fc1, cc1)] = tableroEmoji[fc1][cc1]
                                break
                    except ValueError:
                        print("Posición inválida")

                for fila in tableroVacio:
                    print(" ".join(fila))
                print()

                time.sleep(1.5)

                while True:
                    try:
                        pEncontrada = False

                        for k, v in memoria_cpu1.items():
                            if v == tableroEmoji[fc1][cc1] and k != (fc1, cc1):
                                fc2, cc2 = k
                                pEncontrada = True
                                break

                        if not pEncontrada:
                            fc2 = random.randint(0, f - 1)
                            cc2 = random.randint(0, c - 1)

                        if 0 <= fc2 < f and 0 <= cc2 < c:
                            if tableroVacio[fc2][cc2] == "-":
                                tableroVacio[fc2][cc2] = tableroEmoji[fc2][cc2]
                                if n == 2:
                                    if len(memoria_cpu1) >= 2:
                                        memoria_cpu1.popitem(last=False)
                                    else:
                                        memoria_cpu1[(fc2, cc2)] = tableroEmoji[fc2][cc2]
                                if n == 3:
                                    memoria_cpu1[(fc2, cc2)] = tableroEmoji[fc2][cc2]
                                break
                    except ValueError:
                        print("Posición inválida")

                for fila in tableroVacio:
                    print(" ".join(fila))

                if tableroVacio[fc1][cc1] == tableroVacio[fc2][cc2]:
                    print("¡Enhorabuena, encontraste una pareja!")
                    cpu1 += 2
                    pTotales += 1
                    memoria_cpu1.pop((fc1, cc1), None)
                    memoria_cpu1.pop((fc2, cc2), None)
                else:
                    tableroVacio[fc1][cc1] = "-"
                    tableroVacio[fc2][cc2] = "-"
                    print("¡Fallaste!")
                    j1Acierta = False
                    j2Acierta = True
            except ValueError:
                print()

            if cpu1 == len(emojisArray):
                print(f"\nHa ganado la CPU 1 con {cpu1} puntos")
                break

        while j2Acierta and pTotales < total:
            time.sleep(1.5)
            print("\nTurno de la CPU 2. ")
            try:
                while True:
                    try:
                        if n == 1:
                            fc1 = random.randint(0, f - 1)
                            cc1 = random.randint(0, c - 1)
                        elif n == 2 or n == 3:
                            if memoria_cpu2:
                                fc1, cc1 = random.choice(list(memoria_cpu2.keys()))
                            else:
                                fc1 = random.randint(0, f - 1)
                                cc1 = random.randint(0, c - 1)

                        if 0 <= fc1 < f and 0 <= cc1 < c:
                            if tableroVacio[fc1][cc1] == "-":
                                tableroVacio[fc1][cc1] = tableroEmoji[fc1][cc1]
                                if n == 2:
                                    if len(memoria_cpu2) >= 2:
                                        memoria_cpu2.popitem(last=False)
                                    else:
                                        memoria_cpu2[(fc1, cc1)] = tableroEmoji[fc1][cc1]
                                if n == 3:
                                    memoria_cpu2[(fc1, cc1)] = tableroEmoji[fc1][cc1]
                                break
                    except ValueError:
                        print("Posición inválida")

                for fila in tableroVacio:
                    print(" ".join(fila))
                print()

                time.sleep(1.5)

                while True:
                    try:
                        pEncontrada = False

                        for k, v in memoria_cpu2.items():
                            if v == tableroEmoji[fc1][cc1] and k != (fc1, cc1):
                                fc2, cc2 = k
                                pEncontrada = True
                                break

                        if not pEncontrada:
                            fc2 = random.randint(0, f - 1)
                            cc2 = random.randint(0, c - 1)

                        if 0 <= fc2 < f and 0 <= cc2 < c:
                            if tableroVacio[fc2][cc2] == "-":
                                tableroVacio[fc2][cc2] = tableroEmoji[fc2][cc2]
                                if n == 2:
                                    if len(memoria_cpu2) >= 2:
                                        memoria_cpu2.popitem(last=False)
                                    else:
                                        memoria_cpu2[(fc2, cc2)] = tableroEmoji[fc2][cc2]
                                if n == 3:
                                    memoria_cpu2[(fc2, cc2)] = tableroEmoji[fc2][cc2]
                                break
                    except ValueError:
                        print("Posición inválida")

                for fila in tableroVacio:
                    print(" ".join(fila))

                if tableroVacio[fc1][cc1] == tableroVacio[fc2][cc2]:
                    print("¡Enhorabuena, encontraste una pareja!")
                    cpu2 += 2
                    pTotales += 1
                    memoria_cpu2.pop((fc1, cc1), None)
                    memoria_cpu2.pop((fc2, cc2), None)
                else:
                    tableroVacio[fc1][cc1] = "-"
                    tableroVacio[fc2][cc2] = "-"
                    print("¡Fallaste!")
                    j2Acierta = False
                    j1Acierta = True
            except ValueError:
                print()

    if cpu2 > cpu1:
        print(f"\n¡La CPU 2 gana con {cpu2} puntos!")
    elif cpu1 > cpu2:
        print(f"\n¡La CPU 1 gana con {cpu1} puntos!")
    else:
        print(f"\n¡Es un empate!")


def menu():
    print("- Selecciona un modo de juego -")
    print("-------------------------------")
    print("1 - Jugador contra Jugador")
    print("2 - Jugador contra CPU")
    print("3 - CPU vs CPU")


def dificultad():
    print("- Selecciona la dificultad de la CPU -")
    print("--------------------------------------")
    print("1 - Fácil")
    print("2 - Normal")
    print("3 - Dificil")



while True:
    menu()
    modo = int(input())
    match modo:
        case 1:
            pvp()
        case 2:
            dificultad()
            dif = int(input())
            pvcpu(dif)
        case 3:
            dificultad()
            dif = int(input())
            cpuvcpu(dif)
        case _ :
            print("Selecciona un modo válido")
    break


