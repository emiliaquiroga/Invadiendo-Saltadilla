import pygame
from laser import Laser
from constantes import *

class Ship:
    COOLDOWN = 30 # Constante para el tiempo de espera entre disparos
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health #vida que se ve en la barrita
        self.ship_img = None #imagen de el jugador o enemigos
        self.laser_img = None #imagen laser
        self.animacion_iter = 0 #iterador de animacion
        self.lasers = [] # Lista para almacenar los láseres disparados
        self.cool_down_counter = 0   # Contador para el tiempo de espera entre disparos

    def draw(self, pantalla):
        pantalla.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(pantalla) # Dibujar cada láser de la lista en la pantalla
        # Actualizar animación de la nave
        if self.animacion_iter < len(self.animacion)-1:
            self.animacion_iter += 1
        else:
            self.animacion_iter = 0
        self.ship_img = self.animacion[self.animacion_iter]
        self.animacion_iter += 1
        
    def move_lasers(self, vel, obj):
        self.cooldown() # Actualiza el tiempo de espera entre disparos asi no salen todos juntos
        for laser in self.lasers:
            laser.move(vel) #mover cada laser de la lista
            if laser.off_screen(ANCHO): # Comprobar si el láser está fuera de la pantalla
                self.lasers.remove(laser) #eliminar laser en caso de estarlo
            elif laser.collision(obj):  # Comprobar si el láser colisiona con el objeto especificado
                obj.health -= 10  # Reducir la salud del objeto objetivo
                sonido_auch = pygame.mixer.Sound("sonidos/auch.wav")
                sonido_auch.set_volume(0.1)
                sonido_auch.play()
                self.lasers.remove(laser) #elimina laser si colisiona

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN: # Comprobar si el tiempo de espera entre disparos ha finalizado
            self.cool_down_counter = 0 # Crear un nuevo láser en la posición de la nave
        elif self.cool_down_counter > 0: # Agregar el láser a la lista de láseres disparados
            self.cool_down_counter += 1  # Iniciar el tiempo de espera entre disparos

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img) #crea nuevo laser
            self.lasers.append(laser) #agrega el laser a la lista de los disparados
            self.cool_down_counter = 1 #indica el tiempo de espera entre los tiros
            sonido_disparo = pygame.mixer.Sound("sonidos/laser1.wav")
            sonido_disparo.set_volume(0.1)
            sonido_disparo.play()

    def get_width(self):
        return self.ship_img.get_width() #obtener el ancho de la nave jugador/enemigo

    def get_height(self):
        return self.ship_img.get_height() #obtener altura de la nave jugador/enemigo
