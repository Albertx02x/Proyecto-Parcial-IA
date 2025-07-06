# Albert Medina Familia
# 22-EISN-2-025

import heapq
from scripts.mapa import *
from scripts.cg import TILE , FILAS , COLUMNAS

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
        return [] 
    
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