import random

# Función para que la máquina elija una opción aleatoria
def eleccion_maquina():
    opciones = ["piedra", "papel", "tijeras"]
    return random.choice(opciones)

# Función para determinar el ganador de una partida
def determinar_ganador(jugador, maquina):
    if jugador == maquina:
        return "Empate"
    elif (
        (jugador == "piedra" and maquina == "tijeras") or
        (jugador == "papel" and maquina == "piedra") or
        (jugador == "tijeras" and maquina == "papel")
    ):
        return "Jugador"
    else:
        return "Máquina"

# Función para guardar los resultados en un archivo
def guardar_resultado(resultado):
    with open("resultados/resultados.txt", "a") as archivo:
        archivo.write(resultado + "\n")

# Función principal del juego
def juego_piedra_papel_tijeras():
    while True:
        jugador = input("Elige piedra, papel o tijeras (o escribe 'salir' para terminar el juego): ").lower()

        if jugador == "salir":
            break

        if jugador not in ["piedra", "papel", "tijeras"]:
            print("Opción no válida. Elige piedra, papel o tijeras.")
            continue

        maquina = eleccion_maquina()
        resultado = determinar_ganador(jugador, maquina)
        print(f"Jugador eligió {jugador}, Máquina eligió {maquina}. Resultado: {resultado}")
        guardar_resultado(resultado)

if __name__ == "__main__":
    juego_piedra_papel_tijeras()