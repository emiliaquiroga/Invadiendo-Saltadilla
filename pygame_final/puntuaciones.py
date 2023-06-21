import pygame
from pygame.locals import *
import sys
import pygame_gui
import pygame_gui.elements.ui_text_entry_line
import sqlite3
from constantes import *
from colores import WHITE

def crear_base_datos(path):
    with sqlite3.connect(path) as conexion:
        try:
            sentencia = ''' create table jugadores
                            (
                            id integer primary key autoincrement,
                            nombre text,
                            score integer
                            )
                        '''
            conexion.execute(sentencia)
            print("Se creo la tabla jugadores")
        except sqlite3.OperationalError:
            print("La tabla jugadores ya existe")

def agregar_dato_a_bd(path,nombre,score):
    with sqlite3.connect(path) as conexion:
        try:
            conexion.execute("insert into jugadores(nombre,score) values (?,?)", (nombre, score))
            conexion.commit()
        except:
            print("Error")

def obtener_dato_de_bd(path):
    with sqlite3.connect(path) as conexion:
        datos = conexion.execute("SELECT * FROM jugadores order by score desc")
        lista_datos = []
        for fila in datos: 
            nombre = fila[1]          
            score = str(fila[2])         
            lista_datos.append((nombre,score))
        return lista_datos



MANAGER = pygame_gui.UIManager((ANCHO, ALTO))

TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((280, 500),(250,50)), manager = MANAGER, 
                                                                            object_id = "main_text_entry")

def pedir_nombre():
    run = True
    player_name = ""
    while run:
        UI_REFRESH_RATE = RELOJ.tick(60) / 1000
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and evento.ui_object_id == "main_text_entry":
                player_name = evento.text
                run = False  # Salir del bucle

            MANAGER.process_events(evento)

        MANAGER.update(UI_REFRESH_RATE)

        PANTALLA.blit(END_FONDO, (0, 0))
        MANAGER.draw_ui(PANTALLA)

        pygame.display.update()
    pygame.quit()
    return player_name

def show_ranking():
    pygame.init()
    PANTALLA = pygame.display.set_mode((800, 600))
    PANTALLA.blit(FONDO, (0, 0))
    # Display ranking on the game window
    espacio_posicion_ranking_jugador = 0
    eje_y_jugador_posicion = 200
    lista_datos = obtener_dato_de_bd("baseDatosGalaxy.db")
    for elemento in lista_datos:
        nombre_jugador = elemento[0]
        score_jugador = elemento[1]

        fuente_texto_score = pygame.font.SysFont("gamer",50)
        texto_score = fuente_texto_score.render(score_jugador, True, WHITE)

        fuente_texto_nombre = pygame.font.SysFont("gamer", 50)
        texto_nombre = fuente_texto_nombre.render(nombre_jugador+":", True, WHITE)

        PANTALLA.blit(texto_score, [550, eje_y_jugador_posicion + espacio_posicion_ranking_jugador])
        PANTALLA.blit(texto_nombre, [200, eje_y_jugador_posicion + espacio_posicion_ranking_jugador])
        espacio_posicion_ranking_jugador += 40

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()