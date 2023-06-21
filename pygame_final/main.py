import pygame
import random
from pygame.locals import *
import sys
import pygame_gui
import pygame_gui.elements.ui_text_entry_line

from constantes import *
from constantes import PANTALLA
from colores import WHITE
from boton import Button
from enemigos import Enemy
from jugador import Player
from puntuaciones import crear_base_datos, obtener_dato_de_bd, agregar_dato_a_bd, pedir_nombre, show_ranking

ANCHO = 800
ALTO = 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))

pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.display.set_caption("Invadiendo Saltadilla: Princesa's version")

#boton del teléfono
boton_jugar = Button(BOTON_SUPERFICIE, 400,ANCHO/2)

#creo la base de datos donde guardaré nombres y score
crear_base_datos(DB_PATH)

def collide(obj1, obj2): #maneja todas las colisiones del main, por eso las deje aca
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def main_menu():
    banderita = False
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.checkInput(evento.pos):
                    banderita = True
                    return banderita

        PANTALLA.blit(FONDO, (0,0))
        PANTALLA.blit(TITULO, (250, 200))

        boton_jugar.update()
        pygame.display.flip()

def main():
    pygame.init()
    FPS = 60
    clock = pygame.time.Clock()
    level = 0
    run = True
    player = Player(300, 470)
    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5
    laser_vel = 5

    def redraw_window():
        PANTALLA.blit(FONDO_MAIN, (0,0))
        # dibuja el score y el nivel
        score_label = NOMBRE_SCORE.render(f"Score: {player.score}", 0.005, WHITE)
        level_label = NOMBRE_SCORE.render(f"Nivel: {level}", 1, WHITE)
        PANTALLA.blit(score_label, (10, 10))
        PANTALLA.blit(level_label, (ANCHO - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(PANTALLA)

        player.draw(PANTALLA)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel > 0: # izq
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < ANCHO: #derecha
            player.x += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()
        
        redraw_window()

        if player.health <= 0:
            PANTALLA.blit(END_FONDO, [0, 0])
            lost_sonido = pygame.mixer.Sound("sonidos/tell_my_daddy.wav")
            lost_sonido.set_volume(0.1)
            lost_sonido.play()
            player_name = pedir_nombre()
            agregar_dato_a_bd(DB_PATH, player_name, player.score)
            run = False
            return run

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, ANCHO-100), random.randrange(-1500, -100), random.choice(["bombon", "burbuja", "bellota"]))
                # uso random.choice para que las naves enemigas vayan variando, y le paso los colores que ya tienen cargados
                # las naves y los colores de sus laserss
                enemies.append(enemy)

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                sonido = random.choice(["sonidos/queja.wav", "sonidos/pay_for_that.wav", "sonidos/u_think_yure_good.wav"])
                sonido_quejas = pygame.mixer.Sound(sonido)
                sonido_colision = pygame.mixer.Sound("sonidos/Space Invaders_explosion.wav")
                sonido_colision.set_volume(0.1)
                sonido_quejas.set_volume(0.1)
                sonido_colision.play()
                sonido_quejas.play()
                player.score -= 15
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > ALTO:
                player.score -= 10
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)
        pygame.display.flip()
    pygame.quit()

if main_menu() == True:
    if main() == False:
        show_ranking()
