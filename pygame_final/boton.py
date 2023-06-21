import pygame
from pygame.locals import *
import sys
from constantes import *
from colores import WHITE, PINK3

pygame.init()
main_font = pygame.font.SysFont("calibri", 30)

class Button():
    def __init__(self, imagen, x_pos, y_pos) -> None:
        self.imagen = imagen
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.imagen.get_rect(center = (self.x_pos, self.y_pos))
        #self.text_input = text_input
        #self.text = main_font.render(self.text_input, True, WHITE)
        #self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))
    
    def update(self):
        PANTALLA.blit(self.imagen, self.rect)
        #PANTALLA.blit(self.text, self.text_rect)
    
    def checkInput(self, position):
        if self.rect.collidepoint(position):
            return True
        return False


def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, PINK3)
        else:
            self.text = main_font.render(self.text_input, True, WHITE)

""" 
boton_jugar = Button(BOTON_SUPERFICIE, 300,300, "Jugar")
boton_puntajes = Button(BOTON_SUPERFICIE, 500,300, "Puntajes")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            boton_jugar.checkInput(pygame.mouse.get_pos())
            boton_puntajes.checkInput(pygame.mouse.get_pos())

    PANTALLA.blit(FONDO, (0,0))

    boton_jugar.update()
    boton_jugar.changeColor(pygame.mouse.get_pos())
    boton_puntajes.update()
    boton_puntajes.changeColor(pygame.mouse.get_pos())

    pygame.display.update()
"""