import pygame
import random
import sys
from math import sqrt
import heapq
import time

#Para iniciar Pygame y el joystick
pygame.init()
pygame.joystick.init()

# Mapa

mapa_nivel1 = [
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1],
 [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
 [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
 [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1],
 [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
 [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
 [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

nivel_actual = 1
mapa = mapa_nivel1

#Configuracion de pantalla

FILAS = len(mapa)
COLUMNAS = len(mapa[0])
TILE = 25 

salida_nivel = (COLUMNAS * TILE - TILE * 1.5, FILAS * TILE - TILE * 1.5)

info_pantalla = pygame.display.Info()
ANCHO_BASE = COLUMNAS * TILE
ALTO_BASE = FILAS * TILE

if info_pantalla.current_w < ANCHO_BASE + 200 or info_pantalla.current_h < ALTO_BASE:
    TILE = min(20, (info_pantalla.current_w - 200) // COLUMNAS, info_pantalla.current_h // FILAS)

ANCHO = COLUMNAS * TILE + 200 
ALTO = FILAS * TILE

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Gauntlet")
FPS = 60

#Colores

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (100, 100, 100)
FONDO = (30, 30, 30)
ROJO = (200, 0, 0)
AZUL = (50, 50, 200)
VERDE = (0, 200, 0)
AMARILLO = (255, 255, 0)
MORADO = (128, 0, 128)

puntuacion = 0

#Fuente de letras y tamano 

font = pygame.font.SysFont("Arial", 36)
font_pequena = pygame.font.SysFont("Arial", 20)
font_grande = pygame.font.SysFont("Arial", 72)

#Sonido

pygame.mixer.init()
try:
    pygame.mixer.music.load("C:\\Users\\alber\\Desktop\\Parcial\\musica.mp3")
    pygame.mixer.music.play(-1)
    disparo_sonido = pygame.mixer.Sound("C:\\Users\\alber\\Desktop\\Parcial\\disparo.wav")
    game_over_sound = pygame.mixer.Sound("C:\\Users\\alber\\Desktop\\Parcial\\game_over.wav")
    nivel_completado_sound = pygame.mixer.Sound("C:\\Users\\alber\\Desktop\\Parcial\\nivel_completado.wav")
    juego_completado_sound = pygame.mixer.Sound("C:\\Users\\alber\\Desktop\\Parcial\\juego_completado.wav")
except:
    print("No se encontraron archivos de sonido")

#Sprites

jugador_sprites = {
    "arriba": pygame.image.load("C:\\Users\\alber\\Desktop\\Parcial\\jugador\\arriba.png"),
    "abajo": pygame.image.load("C:\\Users\\alber\\Desktop\\Parcial\\jugador\\abajo.png"),
    "izquierda": pygame.image.load("C:\\Users\\alber\\Desktop\\Parcial\\jugador\\izquierda.png"),
    "derecha": pygame.image.load("C:\\Users\\alber\\Desktop\\Parcial\\jugador\\derecha.png")
}

proyectil_sprites = {
    "arriba": pygame.image.load("C:\\Users\\alber\\Desktop\\Parcial\\disparo\\arriba.png"),
    "abajo": pygame.image.load("C:\\Users\\alber\\Desktop\\Parcial\\disparo\\abajo.png"),
    "izquierda": pygame.image.load("C:\\Users\\alber\\Desktop\\Parcial\\disparo\\izquierda.png"),
    "derecha": pygame.image.load("C:\\Users\\alber\\Desktop\\Parcial\\disparo\\derecha.png")
}

enemigo_imagen = pygame.image.load("C:\\Users\\alber\\Desktop\\Parcial\\enemigo.png")
salida_imagen = pygame.image.load("C:\\Users\\alber\\Desktop\\Parcial\\salida.png")


#Configuracion de control

def inicializar_control():
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(f"Control conectado: {joystick.get_name()}")
        return joystick
    return None

#A*

class NodoAStar:
    def __init__(self, posicion, padre=None):
        self.posicion = posicion
        self.padre = padre
        self.g = 0  # Costo desde inicio
        self.h = 0  # Heurística
        self.f = 0  # Costo total (g + h)
    
    def __eq__(self, other):
        return self.posicion == other.posicion
    
    def __lt__(self, other):
        return self.f < other.f
    
    def __hash__(self):
        return hash(self.posicion)

def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def obtener_enemigos(posicion):
    x, y = posicion
    enemigos = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]  # 4 direcciones
    validos = []
    for v in enemigos:
        if 0 <= v[0] < COLUMNAS and 0 <= v[1] < FILAS and mapa[v[1]][v[0]] == 0:
            validos.append(v)
    return validos

def astar(inicio, fin):
    inicio_tile = (inicio[0] // TILE, inicio[1] // TILE)
    fin_tile = (fin[0] // TILE, fin[1] // TILE)
    
    if mapa[fin_tile[1]][fin_tile[0]] == 1:
        return []  # No hay camino si el destino es una pared
    
    nodo_inicio = NodoAStar(inicio_tile)
    nodo_fin = NodoAStar(fin_tile)
    
    abierta = []
    heapq.heappush(abierta, (nodo_inicio.f, nodo_inicio))
    cerrada = set()
    
    while abierta:
        _, nodo_actual = heapq.heappop(abierta)
        
        if nodo_actual.posicion == nodo_fin.posicion:
            camino = []
            while nodo_actual:
                camino.append((
                    nodo_actual.posicion[0] * TILE + TILE//2,
                    nodo_actual.posicion[1] * TILE + TILE//2
                ))
                nodo_actual = nodo_actual.padre
            return camino[::-1]
        
        cerrada.add(nodo_actual.posicion)
        
        for vecino_pos in obtener_enemigos(nodo_actual.posicion):
            if vecino_pos in cerrada:
                continue
                
            nodo_vecino = NodoAStar(vecino_pos, nodo_actual)
            nodo_vecino.g = nodo_actual.g + 1
            nodo_vecino.h = heuristica(vecino_pos, nodo_fin.posicion)
            nodo_vecino.f = nodo_vecino.g + nodo_vecino.h
            
            en_abierta = False
            for i, (f, nodo) in enumerate(abierta):
                if nodo_vecino.posicion == nodo.posicion:
                    en_abierta = True
                    if nodo_vecino.g < nodo.g:
                        abierta[i] = (nodo_vecino.f, nodo_vecino)
                        heapq.heapify(abierta)
                    break
            
            if not en_abierta:
                heapq.heappush(abierta, (nodo_vecino.f, nodo_vecino))
    
    return []  # No se encontró camino