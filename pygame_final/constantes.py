import pygame
import random
from pygame.locals import *
import sys
import pygame_gui
import pygame_gui.elements.ui_text_entry_line

pygame.font.init()

ANCHO = 800
ALTO = 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
RELOJ = pygame.time.Clock()
FPS = 60

DB_PATH = "baseDatosGalaxy.db" 

NOMBRE_SCORE = pygame.font.SysFont("Arial", 45)

# Background
FONDO_MAIN = pygame.transform.scale(pygame.image.load(("fotos/fondo_saltadilla.png")), (ANCHO, ALTO))
FONDO = pygame.transform.scale(pygame.image.load(("fotos/fondo_corazones.gif")), (ANCHO, ALTO))
TITULO = pygame.transform.scale(pygame.image.load(("fotos/titulo_juego.png")), (376, 134))
END_FONDO = pygame.transform.scale(pygame.image.load(("fotos/end_fondo.jpg")), (ANCHO, ALTO))

#botones:
BOTON_SUPERFICIE = pygame.image.load("fotos/telefono.png")
BOTON_SUPERFICIE = pygame.transform.scale(BOTON_SUPERFICIE, (150,150))


# Load images
BOMBON = pygame.image.load("fotos/bombon_bajando.png")
BELLOTA = pygame.image.load("fotos/bellota_bajando.png")
BURBUJA = pygame.image.load("fotos/burbuja_bajando.png")

# Lasers
LASER_ROJO = pygame.image.load("fotos/pixel_laser_red.png")
LASER_VERDE = pygame.image.load("fotos/pixel_laser_green.png")
LASER_AZUL = pygame.image.load("fotos/pixel_laser_blue.png")
LASER_AMARILLO = pygame.image.load("fotos/pixel_laser_yellow.png")
