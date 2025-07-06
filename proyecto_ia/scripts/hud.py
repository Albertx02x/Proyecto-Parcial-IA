# Albert Medina Familia
# 22-EISN-2-025

from scripts.utils import *
from scripts.control import *

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