# Crea un juego de Piedra, papel y tijeras

import random

def jugar_piedra_papel_tijeras():
    elementos = ["piedra", "papel", "tijeras"]
    puntuacion = {"jugador": 0, "oponente": 0}

    while True:
        jugador = input("Elige piedra, papel o tijeras: ").lower()
        oponente = random.choice(elementos)

        if jugador in elementos:
            print(f"Oponente elige {oponente}")

            if jugador == oponente:
                print("¡Empate!")
            elif (jugador == "piedra" and oponente == "tijeras") or (jugador == "tijeras" and oponente == "papel") or (jugador == "papel" and oponente == "piedra"):
                print("¡Ganaste esta ronda!")
                puntuacion["jugador"] += 1
            else:
                print("Oponente gana esta ronda.")
                puntuacion["oponente"] += 1

            print(f"Puntuación - Jugador: {puntuacion['jugador']} Oponente: {puntuacion['oponente']}")
        else:
            print("Opción no válida. Elige piedra, papel o tijeras.")

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_nuevamente != 's':
            break

    print("¡Juego terminado!")

if __name__ == "__main__":
    jugar_piedra_papel_tijeras()