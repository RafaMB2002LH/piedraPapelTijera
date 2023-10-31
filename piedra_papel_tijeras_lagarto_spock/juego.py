import piedra_papel_tijeras_lagarto_spock.estrategias as estrategias_extendidas

# Función para determinar el ganador de una partida
def determinar_ganador_lagarto(jugador, maquina):
    if jugador == maquina:
        return "Empate"
    if (
        (jugador == "piedra" and (maquina == "lagarto" or maquina == "tijeras")) or
        (jugador == "papel" and (maquina == "piedra" or maquina == "spock")) or
        (jugador == "tijeras" and (maquina == "papel" or maquina == "lagarto")) or
        (jugador == "lagarto" and (maquina == "spock" or maquina == "papel")) or
        (jugador == "spock" and (maquina == "tijeras" or maquina == "piedra"))
    ):
        return "Jugador"
    else:
        return "Máquina"

# Función principal del juego
def juego_piedra_papel_tijeras_lagarto_spock():
    while True:
        jugador = input("Elige piedra, papel, tijeras, lagarto o spock (o escribe 'salir' para terminar el juego): ").lower()

        if jugador == "salir":
            break

        if jugador not in ["piedra", "papel", "tijeras", "lagarto", "spock"]:
            print("Opción no válida. Elige piedra, papel, tijeras, lagarto o spock.")
            continue

        maquina = estrategias_extendidas.eleccion_random()
        resultado = determinar_ganador_lagarto(jugador, maquina)
        print(f"Jugador eligió {jugador}, Máquina eligió {maquina}. Resultado: {resultado}")
        guardar_resultado(resultado)

        # Función para guardar los resultados en un archivo
def guardar_resultado(resultado):
    with open("piedra_papel_tijeras_lagarto_spock/resultados/resultados.txt", "a") as archivo:
        archivo.write(resultado + "\n")
