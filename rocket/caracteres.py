import os
import pygame as pg
from pygame.sprite import Sprite
from rocket import ANCHO, ALTO


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

class Nave(Sprite):

    margen_in = 10
    
    def __init__(self,):    
        super().__init__()
        self.image = pg.image.load(os.path.join("resources", "Ships", "knave.png"))
        self.rect = self.image.get_rect(midbottom=(ALTO/2, self.margen_in))
        
    
    def update(self):
        return