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


