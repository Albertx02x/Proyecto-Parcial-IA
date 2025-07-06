# Albert Medina Familia
# 22-EISN-2-025

import pygame
import sys
from scripts.cg import TILE , FILAS , COLUMNAS
from scripts.sprites import *

pygame.init()
pygame.joystick.init()


def colision_pared(mapa, x, y):
    tile_x, tile_y = int(x // TILE), int(y // TILE)
    return not (0 <= tile_y < FILAS and 0 <= tile_x < COLUMNAS) or mapa[tile_y][tile_x] == 1


# Posición de salida del nivel (esquina inferior derecha)
salida_nivel = (COLUMNAS * TILE - TILE * 1.5, FILAS * TILE - TILE * 1.5)

# Obtener información de la pantalla
info_pantalla = pygame.display.Info()
ANCHO_BASE = COLUMNAS * TILE
ALTO_BASE = FILAS * TILE

if info_pantalla.current_w < ANCHO_BASE + 200 or info_pantalla.current_h < ALTO_BASE:
    TILE = min(20, (info_pantalla.current_w - 200) // COLUMNAS, info_pantalla.current_h // FILAS)

ANCHO = COLUMNAS * TILE + 200  # Espacio para el panel
ALTO = FILAS * TILE

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Gauntlet")
FPS = 60

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (100, 100, 100)
FONDO = (30, 30, 30)
ROJO = (200, 0, 0)
AZUL = (50, 50, 200)
VERDE = (0, 200, 0)
AMARILLO = (255, 255, 0)
MORADO = (128, 0, 128)

# Variable global
puntuacion = 0

# Fuente
font = pygame.font.SysFont("Arial", 36)
font_pequena = pygame.font.SysFont("Arial", 20)
font_grande = pygame.font.SysFont("Arial", 72)

#Configuracion de control
def inicializar_control():
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(f"Control conectado: {joystick.get_name()}")
        return joystick
    return None

def mostrar_menu():
    pantalla.fill(NEGRO)
    titulo = font_grande.render("GAUNTLET", True, VERDE)
    iniciar = font.render("Iniciar partida (ENTER)", True, BLANCO)
    salir = font.render("Salir (ESC)", True, BLANCO)
    
    pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, ALTO//4))
    pantalla.blit(iniciar, (ANCHO//2 - iniciar.get_width()//2, ALTO//2))
    pantalla.blit(salir, (ANCHO//2 - salir.get_width()//2, ALTO//1.5))
    
    pygame.display.flip()
    
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    esperando = False
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if evento.type == pygame.JOYBUTTONDOWN:
                if evento.button == 1:  # Botón X para iniciar
                    esperando = False

def mostrar_pausa():
    pausa = True
    while pausa:
        pantalla.fill(FONDO)
        titulo = font.render("JUEGO EN PAUSA", True, BLANCO)
        resume = font.render("Reanudar (R)", True, VERDE) 
        restart = font.render("Reiniciar (N)", True, BLANCO)
        salir = font.render("Salir (ESC)", True, ROJO)
        
        pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, ALTO//4))
        pantalla.blit(resume, (ANCHO//2 - resume.get_width()//2, ALTO//2.5))
        pantalla.blit(restart, (ANCHO//2 - restart.get_width()//2, ALTO//2))
        pantalla.blit(salir, (ANCHO//2 - salir.get_width()//2, ALTO//1.7))
        
        pygame.display.flip()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    pausa = False
                elif evento.key == pygame.K_n:
                    return "reiniciar"
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if evento.type == pygame.JOYBUTTONDOWN:
                if evento.button == 1:  # Botón X para reanudar
                    pausa = False
                elif evento.button == 9:  # Botón Options para salir
                    pygame.quit()
                    sys.exit()
    return "continuar"

def mostrar_nivel_completado():
    try:
        nivel_completado_sound.play()
    except:
        pass
    
    pantalla.fill(NEGRO)
    titulo = font_grande.render("NIVEL COMPLETADO", True, VERDE)
    texto_puntos = font.render(f"Puntuación: {puntuacion}", True, BLANCO)
    siguiente = font.render("Siguiente nivel (N)", True, BLANCO)
    salir = font.render("Salir (ESC)", True, BLANCO)
    
    pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, ALTO//8))
    pantalla.blit(texto_puntos, (ANCHO//2 - texto_puntos.get_width()//2, ALTO//3))
    pantalla.blit(siguiente, (ANCHO//2 - siguiente.get_width()//2, ALTO//2))
    pantalla.blit(salir, (ANCHO//2 - salir.get_width()//2, ALTO//1.5))
    
    pygame.display.flip()
    
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_n:
                    esperando = False
                    return "siguiente"
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if evento.type == pygame.JOYBUTTONDOWN:
                if evento.button == 1:
                    esperando = False
                    return "siguiente"
    return "salir"

def mostrar_juego_completado():
    try:
        juego_completado_sound.play()
    except:
        pass
    
    pantalla.fill(NEGRO)
    
    # Configuración de fuentes y textos
    titulo = font_grande.render("¡JUEGO COMPLETADO!", True, VERDE)
    subtitulo = font.render("Felicidades", True, AMARILLO)
    texto_puntos = font.render(f"Puntuación final: {puntuacion}", True, BLANCO)
    reiniciar = font.render("Reiniciar (R)", True, BLANCO)
    salir = font.render("Salir (ESC)", True, BLANCO)
    
    # Posiciones fijas para cada elemento
    pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, ALTO//9))
    pantalla.blit(subtitulo, (ANCHO//2 - subtitulo.get_width()//2, ALTO//3.7))
    pantalla.blit(texto_puntos, (ANCHO//2 - texto_puntos.get_width()//2, ALTO//2.5))
    pantalla.blit(reiniciar, (ANCHO//2 - reiniciar.get_width()//2, ALTO//2))
    pantalla.blit(salir, (ANCHO//2 - salir.get_width()//2, ALTO//1.5))
    
    pygame.display.flip()
    
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    esperando = False
                    return "reiniciar"
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if evento.type == pygame.JOYBUTTONDOWN:
                if evento.button == 1:
                    esperando = False
                    return "reiniciar"
    return "salir"

def mostrar_game_over():
    global puntuacion
    try:
        game_over_sound.play()
    except:
        pass
    
    pantalla.fill(NEGRO)
    titulo = font_grande.render("GAME OVER", True, ROJO)
    texto_puntos = font.render(f"Puntuación final: {puntuacion}", True, BLANCO)
    reiniciar = font.render("Reiniciar (R)", True, BLANCO)
    salir = font.render("Salir (ESC)", True, ROJO)
    
    pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, ALTO//8))
    pantalla.blit(texto_puntos, (ANCHO//2 - texto_puntos.get_width()//2, ALTO//3))
    pantalla.blit(reiniciar, (ANCHO//2 - reiniciar.get_width()//2, ALTO//2))
    pantalla.blit(salir, (ANCHO//2 - salir.get_width()//2, ALTO//1.5))
    
    pygame.display.flip()
    
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    esperando = False
                    return "reiniciar"
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if evento.type == pygame.JOYBUTTONDOWN:
                if evento.button == 1:
                    esperando = False
                    return "reiniciar"
    return "salir"

