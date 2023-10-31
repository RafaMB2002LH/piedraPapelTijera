import piedra_papel_tijeras.estrategias as estrategias_clasicas
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
    with open("piedra_papel_tijeras/resultados/resultados.txt", "a") as archivo:
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

        maquina = estrategias_clasicas.eleccion_random()
        resultado = determinar_ganador(jugador, maquina)
        print(f"Jugador eligió {jugador}, Máquina eligió {maquina}. Ganador: {resultado}")
        guardar_resultado(resultado)


# Función principal del juego
def juego_piedra_papel_tijeras_inteligente_v1():
    eleccion_jugador = None  # Para rastrear la elección previa del jugador
    
    while True:
        jugador = input("Elige piedra, papel o tijeras (o escribe 'salir' para terminar el juego): ").lower()

        if jugador == "salir":
            break

        if jugador not in ["piedra", "papel", "tijeras"]:
            print("Opción no válida. Elige piedra, papel o tijeras.")
            continue

        maquina = estrategias_clasicas.eleccion_inteligente_v1(eleccion_jugador)
        resultado = determinar_ganador(jugador, maquina)
        print(f"Jugador eligió {jugador}, Máquina eligió {maquina}. Resultado: {resultado}")
        guardar_resultado(resultado)
        
        eleccion_jugador = jugador  # Actualiza la elección previa del jugador

# Función principal del juego
def juego_piedra_papel_tijeras_inteligente_v2():
    elecciones_jugador = []  # Para rastrear las elecciones previas del jugador
    
    while True:
        jugador = input("Elige piedra, papel o tijeras (o escribe 'salir' para terminar el juego): ").lower()

        if jugador == "salir":
            break

        if jugador not in ["piedra", "papel", "tijeras"]:
            print("Opción no válida. Elige piedra, papel o tijeras.")
            continue

        maquina = estrategias_clasicas.eleccion_inteligente_v2(elecciones_jugador)
        resultado = determinar_ganador(jugador, maquina)
        print(f"Jugador eligió {jugador}, Máquina eligió {maquina}. Resultado: {resultado}")
        guardar_resultado(resultado)
        
        elecciones_jugador.append(jugador)  # Agrega la elección del jugador a la lista
