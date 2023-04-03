import os
import pygame as pg
from rocket import ALTO, ANCHO
from rocket.escenarios import Portada, Nivel_1, Nivel_2, Nivel_3, Jugador


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
            Nivel_1(self.pantalla),
            Nivel_2(self.pantalla),
            Nivel_3(self.pantalla),
            Jugador(self.pantalla)
        ]

    def jugar(self):
        """Este es el bucle principal"""
        for escena in self.escenarios:
            finalizado = escena.bucle_principal()
            if finalizado:
                break
        print("Se Acabo el For")
        pg.quit()




