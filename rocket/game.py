import pygame as pg
from rocket import ALTO, ANCHO


class Rocket:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))

    def jugar(self):
        """Este es el bucle principal"""
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True
            self.pantalla.fill((99, 0, 0))
            pg.display.flip()





