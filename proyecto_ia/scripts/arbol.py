# Albert Medina Familia
# 22-EISN-2-025

import pygame
from scripts.utils import *
from scripts.mapa import *

class Nodo:
    def __init__(self):
        self.hijos = []
    
    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)
        return self

class Selector(Nodo):
    def ejecutar(self, enemigo, jugador):
        for hijo in self.hijos:
            if hijo.ejecutar(enemigo, jugador):
                return True
        return False

class Secuencia(Nodo):
    def ejecutar(self, enemigo, jugador):
        for hijo in self.hijos:
            if not hijo.ejecutar(enemigo, jugador):
                return False
        return True

class Condicion(Nodo):
    def __init__(self, condicion):
        super().__init__()
        self.condicion = condicion
    
    def ejecutar(self, enemigo, jugador):
        return self.condicion(enemigo, jugador)

class Accion(Nodo):
    def __init__(self, accion):
        super().__init__()
        self.accion = accion
    
    def ejecutar(self, enemigo, jugador):
        return self.accion(enemigo, jugador)

def dibujar_mapa():
    for y, fila in enumerate(mapa):
        for x, celda in enumerate(fila):
            rect = pygame.Rect(x*TILE, y*TILE, TILE, TILE)
            color = AZUL if celda == 1 else FONDO
            pygame.draw.rect(pantalla, color, rect)
    
    salida_rect = pygame.Rect(
        salida_nivel[0] - TILE//2,
        salida_nivel[1] - TILE//2,
        TILE, TILE
    )
    pantalla.blit(salida_imagen, salida_rect)

def colision_pared(x, y):
    tile_x, tile_y = int(x // TILE), int(y // TILE)
    return not (0 <= tile_y < FILAS and 0 <= tile_x < COLUMNAS) or mapa[tile_y][tile_x] == 1