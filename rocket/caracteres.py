import os
import pygame as pg
from pygame.sprite import Sprite
from rocket import ANCHO, ALTO , FPS



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


class Nave():

    margen_in = 20
    speed = 5
    fps_animacion = 15
    limite_animacion = FPS // fps_animacion
    iteracion = 0

    def __init__(self):
        imgen = pg.image.load(os.path.join("resources", "Ships", "spaceShips_001.png"))
        self.image = pg.transform.scale(imgen,(30,60))
        self.rect = self.image.get_rect(
            midbottom=(ANCHO/2, ALTO-self.margen_in))
        
        

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed
        
        self.pantalla.fill((255, 255, 255)) # Limpia la pantalla
        self.pantalla.blit(self.image, self.rect) # Dibuja la imagen en su nueva posición
        pg.display.flip() # Actualiza la pantalla
    
        

    
    
