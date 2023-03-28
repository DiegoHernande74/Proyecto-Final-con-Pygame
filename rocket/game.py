import pygame as pg
from rocket import ALTO, ANCHO
from rocket.escenarios import Portada, Partida, Jugador


class Rocket:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Rocket")

        self.escenarios = [
            Portada(self.pantalla),
            Partida(self.pantalla),
            Jugador(self.pantalla)
        ]

    def jugar(self):
        """Este es el bucle principal"""
        for escena in self.escenarios:
            escena.bucle_principal()




