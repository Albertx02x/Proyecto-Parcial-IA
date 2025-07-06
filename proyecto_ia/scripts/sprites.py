# Albert Medina Familia
# 22-EISN-2-025

import pygame

#Sonidos
pygame.mixer.init()
try:
    pygame.mixer.music.load("proyecto_ia\\assets\\musica\\musica.mp3")
    pygame.mixer.music.play(-1)
    disparo_sonido = pygame.mixer.Sound("proyecto_ia\\assets\\sonido\\disparo.wav")
    game_over_sound = pygame.mixer.Sound("proyecto_ia\\assets\\sonido\\game_over.wav")
    nivel_completado_sound = pygame.mixer.Sound("proyecto_ia\\assets\\sonido\\nivel_completado.wav")
    juego_completado_sound = pygame.mixer.Sound("proyecto_ia\\assets\\sonido\\juego_completado.wav")
except:
    print("No se encontraron archivos de sonido")

#Sprites
jugador_sprites = {
    "arriba": pygame.image.load("proyecto_ia\\assets\\images\\jugador\\arriba.png"),
    "abajo": pygame.image.load("proyecto_ia\\assets\\images\\jugador\\abajo.png"),
    "izquierda": pygame.image.load("proyecto_ia\\assets\\images\\jugador\\izquierda.png"),
    "derecha": pygame.image.load("proyecto_ia\\assets\\images\\jugador\\derecha.png")
}

proyectil_sprites = {
    "arriba": pygame.image.load("proyecto_ia\\assets\\images\\disparo\\arriba.png"),
    "abajo": pygame.image.load("proyecto_ia\\assets\\images\\disparo\\abajo.png"),
    "izquierda": pygame.image.load("proyecto_ia\\assets\\images\\disparo\\izquierda.png"),
    "derecha": pygame.image.load("proyecto_ia\\assets\\images\\disparo\\derecha.png")
}

enemigo_imagen = pygame.image.load("proyecto_ia\\assets\\images\\enemigo.png")
salida_imagen = pygame.image.load("proyecto_ia\\assets\\images\\salida.png")
