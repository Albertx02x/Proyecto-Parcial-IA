# Albert Medina Familia
# 22-EISN-2-025

import pygame
import sys
from math import sqrt

from scripts.utils import *
from scripts.arbol import *
from scripts.star import *
from scripts.control import *
from scripts.entidades import *
from scripts.hud import *
from scripts.mapa import *
from scripts.sprites import *
from scripts.cg import *


def main():
    global puntuacion, todos, proyectiles, ANCHO, ALTO, TILE, nivel_actual
    
    while True:
        nivel_actual = 1
        puntuacion = 0
        
        jugador, todos, proyectiles, enemigos = inicializar_nivel(nivel_actual)
        
        mostrar_menu()
        
        clock = pygame.time.Clock()
        corriendo = True
        
        while corriendo:
            clock.tick(FPS)
            keys = pygame.key.get_pressed()
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        corriendo = False
                        pygame.quit()
                        sys.exit()
                    elif evento.key == pygame.K_SPACE:
                        jugador.disparar(proyectiles,todos)
                    elif evento.key == pygame.K_p:
                        resultado = mostrar_pausa()
                        if resultado == "reiniciar":
                            corriendo = False
                            break
                elif evento.type == pygame.JOYBUTTONDOWN:
                    if evento.button == 0:  # Botón X para disparar
                        jugador.disparar(proyectiles,todos)
                    elif evento.button == 9:  # Botón Options para pausa
                        resultado = mostrar_pausa()
                        if resultado == "reiniciar":
                            corriendo = False
                            break
            
            if not corriendo:
                break
            
            jugador.update(keys)
            proyectiles.update()
            for enemigo in enemigos:
                    enemigo.update(jugador, proyectiles, enemigos)


            pantalla.fill(FONDO)
            dibujar_mapa()
            todos.draw(pantalla)
            dibujar_hud(jugador)
            
            pygame.display.flip()

            if jugador.salud <= 0:
                pygame.time.delay(500)
                resultado = mostrar_game_over()
                if resultado == "reiniciar":
                    break
                else:
                    corriendo = False
                    pygame.quit()
                    sys.exit()
            
            if jugador.en_salida():
                if nivel_actual < 3:
                    resultado = mostrar_nivel_completado()
                    if resultado == "siguiente":
                        nivel_actual += 1
                        jugador, todos, proyectiles, enemigos = inicializar_nivel(nivel_actual)
                    else:
                        corriendo = False
                        pygame.quit()
                        sys.exit()
                else:
                    resultado = mostrar_juego_completado()
                    if resultado == "reiniciar":
                        break
                    else:
                        corriendo = False
                        pygame.quit()
                        sys.exit()
        
        if not corriendo:
            break

if __name__ == "__main__":
    main()