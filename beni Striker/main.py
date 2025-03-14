import pygame
import constantes
from ai import behavior_tree
from obstaculo import Obstaculo
from Jugador  import Jugador
import bala

# Crear instancia del jugador
jugador = Jugador(x=50, y=50)

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Counter-Strike 2D")

# Crear obstáculos
obstaculo1 =Obstaculo(200, 100, 50, 50)
grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(obstaculo1)
bala.pygame.sprite.Group

# Definir las variables de movimiento
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False
direccion_jugador = 1

time = pygame.time.Clock()
run = True

while run:
# Limpiar la pantalla
    ventana.fill((0, 0, 0))  #Esto funciona correctamente
   
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            mover_izquierda = True
        elif event.key == pygame.K_d:
            mover_derecha = True
        elif event.key == pygame.K_w:
            mover_arriba = True
        elif event.key == pygame.K_s:
            mover_abajo = True
        elif event.key == pygame.K_SPACE:
            nueva_bala = bala(jugador.rect.centerx, jugador.rect.centery, direccion_jugador)
            bala.add(nueva_bala)
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            mover_izquierda = False
        elif event.key == pygame.K_d:
            mover_derecha = False
        elif event.key == pygame.K_w:
            mover_arriba = False
        elif event.key == pygame.K_s:
            mover_abajo = False

# Mover jugador
    if mover_izquierda:
        jugador.rect.x -= 5
    if mover_derecha:
        jugador.rect.x += 5
    if mover_arriba:
        jugador.rect.y -= 5
    if mover_abajo:
        jugador.rect.y += 5

# Llamar a la IA para decidir la accion del NPC
behavior_tree.ejecutar(jugador,Obstaculo)

# Dibujar elementos en pantalla
ventana.fill((0, 0, 0))  #Esto funciona correctamente
Obstaculo.draw(ventana)
jugador.dibujar(ventana)
bala.draw(ventana)

# Actualizar la pantalla
pygame.display.flip()
time.tick(60)

pygame.quit()
