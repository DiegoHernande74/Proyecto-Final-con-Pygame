from rocket import ALTO, ANCHO
from rocket.game import Rocket

if __name__ == "__main__":
    print(f"El tamaño de la pantalla es {ALTO}x{ANCHO}")
    juego = Rocket()
    juego.jugar()
