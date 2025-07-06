# Albert Medina Familia
# 22-EISN-2-025

import pygame
import random
from scripts.entidades import*
from scripts.mapa import*
from scripts.utils import*


def inicializar_nivel(nivel):
    global mapa, salida_nivel, FILAS, COLUMNAS, ANCHO, ALTO, TILE, nivel_actual
    
    nivel_actual = nivel
    
    if nivel == 1:
        mapa = mapa_nivel1
    elif nivel == 2:
        mapa = mapa_nivel2
    elif nivel == 3:
        mapa = mapa_nivel3
    
    
    FILAS = len(mapa)
    COLUMNAS = len(mapa[0])
    salida_nivel = (COLUMNAS * TILE - TILE * 1.5, FILAS * TILE - TILE * 1.5)
    
    info_pantalla = pygame.display.Info()
    ANCHO_BASE = COLUMNAS * TILE
    ALTO_BASE = FILAS * TILE
    
    info = pygame.display.Info()
    if info.current_w < ANCHO_BASE + 200 or info.current_h < ALTO_BASE:
        TILE = min(20, (info.current_w - 200) // COLUMNAS, info.current_h // FILAS)
    
    ANCHO = COLUMNAS * TILE + 200
    ALTO = FILAS * TILE
    
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    
    jugador = Jugador()
    todos = pygame.sprite.Group(jugador)
    proyectiles = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    
    # Pone enemigos en posiciones aleatorias
    for _ in range(3 + nivel):  # Más enemigos en niveles que se pasen
        while True:
            x, y = TILE * random.randint(1, COLUMNAS-2), TILE * random.randint(1, FILAS-2)
            if not colision_pared(mapa, x, y):
                enemigo = Enemigo(x, y)
                enemigos.add(enemigo)
                todos.add(enemigo)
                break
    
    return jugador, todos, proyectiles, enemigos