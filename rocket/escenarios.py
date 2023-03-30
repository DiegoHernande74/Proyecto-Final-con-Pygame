import pygame as pg
import os
from rocket import ALTO, ANCHO


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
    
    def bucle_principal(self):
            pass

class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta = os.path.join("resources", "Portada", "ROCKET.png")
        self.logo = pg.image.load(ruta)
       

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True
            self.pantalla.fill((99, 0, 0))
            self.pantalla.blit(self.logo, ((ANCHO/800), (ALTO/600)))
            pg.display.flip()

        
    """def pintar_logo(self):
        ancho_logo = self.logo.get_width()
        pos_x = (ANCHO - ancho_logo) / 600
        pos_y = ALTO/800
        self.pantalla.blit(self.logo, (pos_x, pos_y))
        """

class Partida(Escena):
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True
            self.pantalla.fill((0, 99, 0))
            pg.display.flip()

class Jugador(Escena):
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True
            self.pantalla.fill((0, 0, 99))
            pg.display.flip()

