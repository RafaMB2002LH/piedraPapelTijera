import random
# Función para que la máquina elija una opción aleatoria
def eleccion_random():
    opciones = ["piedra", "papel", "tijeras", "lagarto", "spock"]
    return random.choice(opciones)
