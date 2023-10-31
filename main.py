import piedra_papel_tijeras.juego as juego_clasico
import piedra_papel_tijeras_lagarto_spock.juego as juego_extendido

# Función para que el jugador elija la variante del juego
def elegir_variante_de_juego():
    while True:
        print("Elige la variante del juego:")
        print("1. Piedra, papel, tijeras (Clásico)")
        print("2. Piedra, papel, tijeras, lagarto, spock (Extendido)")
        print("3. Salir")
        opcion = input("Ingresa el número de la variante que deseas jugar: ")

        if opcion == "1":
            elegir_estrategia()
        elif opcion == "2":
            juego_extendido.juego_piedra_papel_tijeras_lagarto_spock()
        elif opcion == "3":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Elige una variante válida.")

# Función para que el jugador elija la estrategia de la máquina
def elegir_estrategia():
    while True:
        print("Elige la estrategia de la máquina:")
        print("1. Elección aleatoria (Random)")
        print("2. Estrategia inteligente v1 (Basada en elección previa del jugador)")
        print("3. Estrategia inteligente v2 (Basada en elección predominante del jugador)")
        print("4. Volver al menú principal")
        opcion = input("Ingresa el número de la estrategia que deseas utilizar: ")

        if opcion == "1":
            juego_clasico.juego_piedra_papel_tijeras()
        elif opcion == "2":
            juego_clasico.juego_piedra_papel_tijeras_inteligente_v1()
        elif opcion == "3":
            juego_clasico.juego_piedra_papel_tijeras_inteligente_v2()
        elif opcion == "4":
            return None
        else:
            print("Opción no válida. Elige una estrategia válida.")

if __name__ == "__main__":
    elegir_variante_de_juego()