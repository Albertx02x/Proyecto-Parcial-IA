# Albert Medina Familia
# 22-EISN-2-025

import pygame

#Sonidos
pygame.mixer.init()
try:
    pygame.mixer.music.load("assets\\musica\\musica.mp3")
    pygame.mixer.music.play(-1)
    disparo_sonido = pygame.mixer.Sound("assets\\sonido\\disparo.wav")
    game_over_sound = pygame.mixer.Sound("assets\\sonido\\game_over.wav")
    nivel_completado_sound = pygame.mixer.Sound("assets\\sonido\\nivel_completado.wav")
    juego_completado_sound = pygame.mixer.Sound("assets\\sonido\\juego_completado.wav")
except:
    print("No se encontraron archivos de sonido")

#Sprites
jugador_sprites = {
    "arriba": pygame.image.load("assets\\images\\jugador\\arriba.png"),
    "abajo": pygame.image.load("assets\\images\\jugador\\abajo.png"),
    "izquierda": pygame.image.load("assets\\images\\jugador\\izquierda.png"),
    "derecha": pygame.image.load("assets\\images\\jugador\\derecha.png")
}

proyectil_sprites = {
    "arriba": pygame.image.load("assets\\images\\disparo\\arriba.png"),
    "abajo": pygame.image.load("assets\\images\\disparo\\abajo.png"),
    "izquierda": pygame.image.load("assets\\images\\disparo\\izquierda.png"),
    "derecha": pygame.image.load("assets\\images\\disparo\\derecha.png")
}

enemigo_imagen = pygame.image.load("assets\\images\\enemigo.png")
salida_imagen = pygame.image.load("assets\\images\\salida.png")
