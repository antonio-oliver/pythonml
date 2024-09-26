import random

def jugar():
    opciones = ['piedra', 'papel', 'tijera']

    # Preguntar al jugador por su elección
    jugador = input("Elige piedra, papel o tijera: ")

    # Validar la entrada
    if jugador not in opciones:
        print("Opción no válida, por favor elige de nuevo.")
        return

    # La computadora elige al azar
    computadora = random.choice(opciones)

    # Mostrar las elecciones
    print(f"\nTú elegiste: {jugador}")
    print(f"La computadora eligió: {computadora}\n")

    # Determinar el ganador
    if jugador == computadora:
        print("¡Es un empate!")
    elif (jugador == 'piedra' and computadora == 'tijera') or \
         (jugador == 'papel' and computadora == 'piedra') or \
         (jugador == 'tijera' and computadora == 'papel'):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

# Ejecutar el juego
jugar()