# Albert Medina Familia
# 22-EISN-2-025

import pygame
import random
from math import sqrt
from scripts.utils import  TILE
from scripts.sprites import jugador_sprites, proyectil_sprites, enemigo_imagen, disparo_sonido
from scripts.arbol import *
from scripts.star import *
from scripts.mapa import *



class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = jugador_sprites["abajo"]
        self.rect = self.image.get_rect()
        self.rect.center = (TILE * 1.5, TILE * 1.5)
        self.direccion = "abajo"
        self.salud = 5
        self.invulnerable = False
        self.invulnerable_tiempo = 0
        self.control = inicializar_control()

    def update(self, keys):
        if self.invulnerable:
            if pygame.time.get_ticks() - self.invulnerable_tiempo > 1000:
                self.invulnerable = False

        dx = dy = 0
        
        if self.control:
            eje_x = self.control.get_axis(0)
            eje_y = self.control.get_axis(1)
            
            umbral = 0.3
            if abs(eje_x) > umbral:
                dx = eje_x
            if abs(eje_y) > umbral:
                dy = eje_y
        else:
            dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
            dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]

        nueva_x = self.rect.centerx + dx * 5
        nueva_y = self.rect.centery + dy * 5

        if not colision_pared(nueva_x, self.rect.centery):
            self.rect.centerx = nueva_x
        if not colision_pared(self.rect.centerx, nueva_y):
            self.rect.centery = nueva_y

        if abs(dx) > abs(dy):
            self.direccion = "derecha" if dx > 0 else "izquierda"
        elif dy != 0:
            self.direccion = "abajo" if dy > 0 else "arriba"

        self.image = jugador_sprites[self.direccion]

    def recibir_dano(self):
        if not self.invulnerable:
            self.salud -= 1
            self.invulnerable = True
            self.invulnerable_tiempo = pygame.time.get_ticks()
            return True
        return False

    def disparar(self, proyectiles, todos):
        p = Proyectil(self.rect.centerx, self.rect.centery, self.direccion)
        proyectiles.add(p)
        todos.add(p)
        try:
            disparo_sonido.play()
        except:
            pass

    def en_salida(self):
        distancia = sqrt((self.rect.centerx - salida_nivel[0])**2 + (self.rect.centery - salida_nivel[1])**2)
        return distancia < TILE

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y, direccion):
        super().__init__()
        self.image = proyectil_sprites[direccion]
        self.rect = self.image.get_rect(center=(x, y))
        self.direccion = direccion
        self.velocidad = 10

    def update(self):
        if self.direccion == "arriba": self.rect.y -= self.velocidad
        elif self.direccion == "abajo": self.rect.y += self.velocidad
        elif self.direccion == "izquierda": self.rect.x -= self.velocidad
        elif self.direccion == "derecha": self.rect.x += self.velocidad

        if (self.rect.right < 0 or self.rect.left > ANCHO or self.rect.bottom < 0 or self.rect.top > ALTO
                or colision_pared(self.rect.centerx, self.rect.centery)):
            self.kill()


class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = enemigo_imagen
        self.rect = self.image.get_rect(center=(x, y))
        self.direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])
        self.velocidad = 2 + nivel_actual * 0.5  # Los enemigos son más rápidos en niveles superiores
        self.ataque_delay = 1000
        self.ultimo_ataque = pygame.time.get_ticks()
        self.camino = []
        self.ultima_actualizacion_camino = 0
        self.arbol_comportamiento = self.construir_arbol_comportamiento()

    def construir_arbol_comportamiento(self):
        raiz = Selector()
        
        secuencia_ataque = Secuencia()
        secuencia_ataque.agregar_hijo(Condicion(self.jugador_cerca))
        secuencia_ataque.agregar_hijo(Condicion(self.puede_atacar))
        secuencia_ataque.agregar_hijo(Accion(self.atacar_jugador))
        
        secuencia_perseguir = Secuencia()
        secuencia_perseguir.agregar_hijo(Condicion(self.jugador_cerca))
        secuencia_perseguir.agregar_hijo(Accion(self.perseguir_con_astar))
        
        accion_patrullar = Accion(self.patrullar)
        
        raiz.agregar_hijo(secuencia_ataque)
        raiz.agregar_hijo(secuencia_perseguir)
        raiz.agregar_hijo(accion_patrullar)
        
        return raiz

    def jugador_cerca(self, enemigo, jugador):
        return self.distancia_a_jugador(jugador) < 200

    def puede_atacar(self, enemigo, jugador):
        ahora = pygame.time.get_ticks()
        return (ahora - self.ultimo_ataque >= self.ataque_delay and 
                self.rect.colliderect(jugador.rect))

    def distancia_a_jugador(self, jugador):
        dx = jugador.rect.centerx - self.rect.centerx
        dy = jugador.rect.centery - self.rect.centery
        return sqrt(dx**2 + dy**2)

    def perseguir_con_astar(self, enemigo, jugador):
        ahora = pygame.time.get_ticks()
        if ahora - self.ultima_actualizacion_camino > 500 or not self.camino:
            self.camino = astar((self.rect.centerx, self.rect.centery), 
                               (jugador.rect.centerx, jugador.rect.centery))
            self.ultima_actualizacion_camino = ahora
        
        if self.camino:
            objetivo_x, objetivo_y = self.camino[0]
            dx = objetivo_x - self.rect.centerx
            dy = objetivo_y - self.rect.centery
            distancia = max(1, sqrt(dx**2 + dy**2))
            
            mover_x = (dx / distancia) * self.velocidad
            mover_y = (dy / distancia) * self.velocidad
            
            nueva_x = self.rect.centerx + mover_x
            nueva_y = self.rect.centery + mover_y
            
            if not colision_pared(nueva_x, self.rect.centery):
                self.rect.centerx = nueva_x
            if not colision_pared(self.rect.centerx, nueva_y):
                self.rect.centery = nueva_y
            
            if distancia < 5:
                self.camino.pop(0)
        
        return True

    def atacar_jugador(self, enemigo, jugador):
        self.ultimo_ataque = pygame.time.get_ticks()
        if jugador.recibir_dano():
            print("Jugador golpeado. Salud:", jugador.salud)
        return True

    def patrullar(self, enemigo, jugador):
        dx = dy = 0
        if self.direccion == "arriba":
            dy = -self.velocidad
        elif self.direccion == "abajo":
            dy = self.velocidad
        elif self.direccion == "izquierda":
            dx = -self.velocidad
        elif self.direccion == "derecha":
            dx = self.velocidad
        
        nueva_x = self.rect.centerx + dx
        nueva_y = self.rect.centery + dy
        
        if not colision_pared(nueva_x, nueva_y):
            self.rect.centerx = nueva_x
            self.rect.centery = nueva_y
        else:
            self.direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])
        return True

    def update(self, jugador, proyectiles, enemigos):
        global puntuacion
        self.arbol_comportamiento.ejecutar(self, jugador)
    
        for proyectil in proyectiles:
            if self.rect.colliderect(proyectil.rect):
                proyectil.kill()
                puntuacion += 100
                enemigos.remove(self)
                self.kill()
                return 100
        return 0
