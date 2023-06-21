import pygame
from constantes import *
from nave import Ship
from laser import Laser


class Enemy(Ship):
    COLOR_MAP = {
        "bombon": (BOMBON, LASER_ROJO),
        "bellota": (BELLOTA, LASER_VERDE),
        "burbuja": (BURBUJA, LASER_AZUL)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move(self, velocidad):
        self.y += velocidad

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
