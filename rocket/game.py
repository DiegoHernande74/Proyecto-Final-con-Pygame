import os
import pygame as pg
from rocket import ALTO, ANCHO
from rocket.escenarios import Portada, Partida, Jugador


class Rocket:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Rocket")

        # Windows: resources\imagenes\icon.png
        """ICONO DE LA ESQUINA DE LA VENTANA"""
        ruta = os.path.join("resources", "icon.png")
        icon = pg.image.load(ruta)
        pg.display.set_icon(icon)

        self.escenarios = [
            Portada(self.pantalla),
            Partida(self.pantalla),
            Jugador(self.pantalla)
        ]

    def jugar(self):
        """Este es el bucle principal"""
        for escena in self.escenarios:
            escena.bucle_principal()




