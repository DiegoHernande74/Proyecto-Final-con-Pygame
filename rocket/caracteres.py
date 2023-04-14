import os
import pygame as pg
from pygame.sprite import Sprite
from rocket import ANCHO, ALTO
import sys


"""
Inicio de nivel
.Nuestra naveaparecerá en el margen izquierdo de la pantalla en el centro vertical.
.La nave se moverá hacia arriba y abajo con las teclas del cursor.
.La nave se parará en su ascenso y descenso si deja de pulsarse la tecla del cursor que corresponda
.El movimiento hacia arriba y hacia abajo de la nave podrá ser acelerado si se mantiene pulsada la tecla
de flecha.

Restricciones
.La nave no podrá avanzar ni retroceder de derecha a izquierda ni viceversa.
.Una vez alcanzado el nivel superior o inferior de la pantalla la nave se quedará parada.No desaparecerá de la pantalla ni aparecerá por el otro lado.
"""

class Nave(pg.Rect):
    imagen_Ancho = 30
    imagen_Alto = 30
    margen_in = 10
    speed = 5

    
    def __init__(self, pantalla):
        super().__init__()
        self.pantalla = pantalla
        self.image = pg.image.load(os.path.join("resources", "Ships", "spaceShips_001.png"))
        self.image_Ancho = self.image.get_width()
        self.image_Alto = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.centery = pantalla.get_rect().centery
        
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed
        
        self.pantalla.fill((255, 255, 255)) # Limpia la pantalla
        self.pantalla.blit(self.image, self.rect) # Dibuja la imagen en su nueva posición
        pg.display.flip() # Actualiza la pantalla

    
    
