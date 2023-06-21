import pygame
from nave import Ship
from constantes import *
from colores import YELLOW3, BLUEVIOLET


def obtener_superficies(path,filas, columnas): #Funcion de Yani para los Sprites
    lista=[]
    superficie_imagen = pygame.image.load(path)
    fotograma_ancho = int(superficie_imagen.get_width()/columnas)
    fotograma_alto = int(superficie_imagen.get_height()/filas)
    for fila in range(filas):
        for columna in range(columnas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            #un pedacito de la imagen del sprite
            superficie_fotograma = superficie_imagen.subsurface(x,y,fotograma_ancho, fotograma_alto)
            lista.append(superficie_fotograma)
    return lista

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.sprites = obtener_superficies("fotos/princesa_volando.png", 2, 1)
        self.rect = self.sprites[0].get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.animacion = self.sprites
        self.ship_img = self.sprites[0]
        self.laser_img = LASER_AMARILLO
        self.score = 0
        self.mask = pygame.mask.from_surface(self.ship_img)
        #la mask dice donde esta estan los pixels de la imagen, entonces cuando colisionen sabemos si le pego a un pixel o no
        #simil colliderect
        self.max_health = health
        self.animacion_iter = 0

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(ALTO):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        self.score += 50
                        sonido_festejo = pygame.mixer.Sound("sonidos/take_that.wav") #BUSCAR OTRO SONIDO ESTE ES MUY LARGO
                        #sonido_colision = pygame.mixer.Sound("take_that.wav")
                        sonido_festejo.set_volume(0.1)
                        sonido_festejo.play()
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, pantalla):
        super().draw(pantalla) #hereda el metodo draw
        self.healthbar(pantalla) #Dibujar la barra de salud de la nave principal
        self.animacion_iter += 1 #Incrementa el iter de la animacion
        if self.animacion_iter >= 500:  # Si el iterador ha alcanzado o superado 500
            self.animacion_iter = 0  # Reiniciar el iterador a 0 para reiniciar la animación
        # Calcular el índice del sprite actual en función del iterador de animación
        sprite_index = self.animacion_iter // (500 // 4)
    
        self.ship_img = self.animacion[sprite_index]  # Actualizar la imagen de la nave principal con el sprite correspondiente
        self.ship_img = self.animacion[self.animacion_iter // (500 // 4)] #Dibujar la barra de salud de la nave principal

    def healthbar(self, window):
        #Acá dibujo en BLUEVIOLET la base que queda fija que hace la totalidad de la vida
        pygame.draw.rect(window, (BLUEVIOLET), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (YELLOW3), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))
        #Y la segunda es la vida actual en amarillo, esa va disminuyendo 
