import pygame as pg
import os
from rocket import ALTO, ANCHO
from .caracteres import Nave


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()
    
    def bucle_principal(self):
            pass

class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        
        ruta = os.path.join("resources", "Portada", "ROCKET.png")
        self.logo = pg.image.load(ruta)

        ruta_fonts = os.path.join("resources", "Fonts", "Kenney Blocks.ttf")
        self.fonts = pg.font.Font(ruta_fonts, 25)#Tamaño de la fuente
       

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    salir = True
            self.pantalla.fill((99, 0, 0))
            self.pantalla.blit(self.logo, ((ANCHO/800), (ALTO/600)))
            self.pintar_texto()
            pg.display.flip()
        return False
        
    """def pintar_logo(self):
        ancho_logo = self.logo.get_width()
        pos_x = (ANCHO - ancho_logo) / 2
        pos_y = ALTO/3
        self.pantalla.blit(self.logo, (pos_x, pos_y))
        """
    
    def pintar_texto(self):
        
        mensaje = "Pulsa <espacio> para comezar la partida"
        texto = self.fonts.render(mensaje, True, (255, 255, 255))
        pos_x = ANCHO/2 - texto.get_width()/2
        pos_y = ALTO * 3 / 4
        self.pantalla.blit(texto, (pos_x, pos_y))


class Nivel_1(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
       
        ruta = os.path.join("resources", "fondos", "1.jpg")
        self.fondo = pg.image.load(ruta)
        self.jugador = Nave(self.pantalla)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
            self.pantalla.fill((0, 99, 0))
            self.pantalla.blit(self.fondo, ((ANCHO/800), (ALTO/600)))
            pg.display.flip()
        return False

class Nivel_2(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
       
        ruta = os.path.join("resources", "fondos", "2.jpg")
        self.fondo = pg.image.load(ruta)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
            self.pantalla.fill((0, 99, 0))
            self.pantalla.blit(self.fondo, ((ANCHO/800), (ALTO/600)))
            pg.display.flip()
        return False

class Nivel_3(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
       
        ruta = os.path.join("resources", "fondos", "3.jpg")
        self.fondo = pg.image.load(ruta)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
            self.pantalla.fill((0, 99, 0))
            self.pantalla.blit(self.fondo, ((ANCHO/800), (ALTO/600)))
            pg.display.flip()
        return False

class Jugador(Escena):
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
            self.pantalla.fill((0, 0, 99))
            pg.display.flip()
        return False

