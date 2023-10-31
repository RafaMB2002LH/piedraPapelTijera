import random

# Función para que la máquina elija una opción aleatoria
def eleccion_maquina():
    opciones = ["piedra", "papel", "tijeras"]
    return random.choice(opciones)

# Función para que la máquina elija una opción basada en la elección previa del jugador
def eleccion_inteligente(eleccion_jugador):
    opciones = ["piedra", "papel", "tijeras"]
    
    # Si es la primera jugada, elige una opción aleatoria
    if eleccion_jugador is None:
        return random.choice(opciones)
    
    # Si no es la primera jugada, la máquina elige la opción que habría ganado a la elección anterior del jugador
    if eleccion_jugador == "piedra":
        return "papel"
    elif eleccion_jugador == "papel":
        return "tijeras"
    else:
        return "piedra"

# Función para que la máquina elija una opción basada en la elección predominante del jugador
def eleccion_inteligente_v2(elecciones_jugador):
    opciones = ["piedra", "papel", "tijeras"]
    
    # Si es la primera jugada, elige una opción aleatoria
    if not elecciones_jugador:
        return random.choice(opciones)
    
    # Calcula la elección predominante del jugador
    eleccion_predominante = max(set(elecciones_jugador), key=elecciones_jugador.count)
    
    # La máquina elige la opción que habría ganado a la elección predominante del jugador
    if eleccion_predominante == "piedra":
        return "papel"
    elif eleccion_predominante == "papel":
        return "tijeras"
    else:
        return "piedra"
    
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
        print(f"Jugador eligió {jugador}, Máquina eligió {maquina}. Ganador: {resultado}")
        guardar_resultado(resultado)

# Función principal del juego
def juego_piedra_papel_tijeras_inteligente():
    eleccion_jugador = None  # Para rastrear la elección previa del jugador
    
    while True:
        jugador = input("Elige piedra, papel o tijeras (o escribe 'salir' para terminar el juego): ").lower()

        if jugador == "salir":
            break

        if jugador not in ["piedra", "papel", "tijeras"]:
            print("Opción no válida. Elige piedra, papel o tijeras.")
            continue

        maquina = eleccion_inteligente(eleccion_jugador)
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

        maquina = eleccion_inteligente_v2(elecciones_jugador)
        resultado = determinar_ganador(jugador, maquina)
        print(f"Jugador eligió {jugador}, Máquina eligió {maquina}. Resultado: {resultado}")
        guardar_resultado(resultado)
        
        elecciones_jugador.append(jugador)  # Agrega la elección del jugador a la lista

if __name__ == "__main__":
    juego_piedra_papel_tijeras_inteligente_v2()