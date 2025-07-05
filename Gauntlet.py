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

mapa_nivel2 = [
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
 [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
 [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

mapa_nivel3 = [
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
 [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
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
    
    return [] 


#Arbol de comportamiento

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
    
    # Dibujar salida del nivel
    salida_rect = pygame.Rect(
        salida_nivel[0] - TILE//2,
        salida_nivel[1] - TILE//2,
        TILE, TILE
    )
    pantalla.blit(salida_imagen, salida_rect)

def colision_pared(x, y):
    tile_x, tile_y = int(x // TILE), int(y // TILE)
    return not (0 <= tile_y < FILAS and 0 <= tile_x < COLUMNAS) or mapa[tile_y][tile_x] == 1

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

    def disparar(self):
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

    def update(self, jugador):
        global puntuacion
        self.arbol_comportamiento.ejecutar(self, jugador)
        
        for proyectil in proyectiles:
            if self.rect.colliderect(proyectil.rect):
                proyectil.kill()
                puntuacion += 100
                self.kill()

# Lado derecho para estadisticas 

def dibujar_hud(jugador):
    panel_ancho = min(200, ANCHO // 5)
    
    panel_surface = pygame.Surface((panel_ancho, ALTO), pygame.SRCALPHA)
    panel_surface.fill((100, 100, 100, 200))
    pantalla.blit(panel_surface, (ANCHO - panel_ancho, 0))
    
    pos_y = 20
    
    titulo = font_pequena.render("ESTADÍSTICAS", True, AMARILLO)
    pantalla.blit(titulo, (ANCHO - panel_ancho + 10, pos_y))
    pos_y += 30
    
    texto_salud = font_pequena.render(f"Salud: {jugador.salud}", True, BLANCO)
    pantalla.blit(texto_salud, (ANCHO - panel_ancho + 10, pos_y))
    
    for i in range(jugador.salud):
        pygame.draw.circle(pantalla, ROJO, (ANCHO - panel_ancho + 100 + i * 25, pos_y + 10), 8)
    pos_y += 30
    
    texto_puntos = font_pequena.render(f"Puntos: {puntuacion}", True, BLANCO)
    pantalla.blit(texto_puntos, (ANCHO - panel_ancho + 10, pos_y))
    pos_y += 30
    
    texto_nivel = font_pequena.render(f"Nivel: {nivel_actual}/3", True, BLANCO)
    pantalla.blit(texto_nivel, (ANCHO - panel_ancho + 10, pos_y))
    pos_y += 40

#Menu Principal

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

#Menu de pausa

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
                if evento.button == 1:  
                    pausa = False
                elif evento.button == 9:  
                    pygame.quit()
                    sys.exit()
    return "continuar"

#Ventana de nivel completado

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

#Juego completado

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

#ventana Game over

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

#Niveles de juego

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
    
   # Para que los enemigos esten en partes aletatorias
    for _ in range(4 + nivel):  
        while True:
            x, y = TILE * random.randint(1, COLUMNAS-2), TILE * random.randint(1, FILAS-2)
            if not colision_pared(x, y):
                enemigo = Enemigo(x, y)
                enemigos.add(enemigo)
                todos.add(enemigo)
                break
    
    return jugador, todos, proyectiles, enemigos