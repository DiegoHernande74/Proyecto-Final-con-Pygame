from rocket import ALTO, ANCHO
from rocket.game import Rocket

if __name__ == "__main__":
    print(f"Eltamaño de la pantalla es {ANCHO}x{ALTO}")
    juego = Rocket()
    juego.jugar()
