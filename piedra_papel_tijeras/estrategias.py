import random

# Función para que la máquina elija una opción aleatoria
def eleccion_random():
    opciones = ["piedra", "papel", "tijeras"]
    return random.choice(opciones)

# Función para que la máquina elija una opción basada en la elección previa del jugador
def eleccion_inteligente_v1(eleccion_jugador):
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
    