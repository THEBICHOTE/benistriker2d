mport pygame
import constantes
from Jugador import Jugador
from obstaculo import obstaculo
from bala import bala

# Crear instancia del jugador
jugador = Jugador(x=50, y=50)

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Counter Striker 2D")

jugador = Jugador(x=50, y=50)
obstaculos = pygame.sprite.Group()
obstaculo1 = obstaculo(200, 200, 100, 50)
obstaculo2 = obstaculo(500, 350, 75, 120)
obstaculos.add(obstaculo1, obstaculo2)
balas = pygame.sprite.Group()
direccion_jugador = 1

# Definir las variables de movimiento
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

clock = pygame.time.Clock()
run = True

while run:
     # Limpiar la pantalla

    ventana.fill((0, 0, 0)) 
    # Calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha:
        delta_x = 5
    if mover_izquierda:
        delta_x = -5
    if mover_arriba:
        delta_y = -5
    if mover_abajo:
        delta_y = 5

    # Mover al jugador
    jugador.movimiento(delta_x, delta_y)
    jugador.dibujar(ventana)

    obstaculo.draw(ventana)

    colisiones = pygame.sprite.spritecollide(jugador, obstaculos, False)
    if colisiones:
        jugador.rect.x -= delta_x
        jugador.rect.y -= delta_y

    balas.update()
    balas.draw(ventana)

    colision_balas_obstaculos = pygame.sprite.groupcollide(balas, obstaculos, True, False)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Detectar teclas presionadas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
            if event.key == pygame.K_SPACE:
                bala = bala(jugador.rect.centerx, jugador.rect.centery, direccion_jugador)
                balas.add(bala)

        # Detectar cuando se sueltan las teclas
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False

 # Actualizar pantalla
    pygame.display.flip() 

     # Limitar FPS a 60
    clock.tick(60) 

pygame.quit()
import pygame
import constantes
from Jugador import Jugardor

Jugardor= Jugardor(x=50,y=50)

pygame.init()

ventana= pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))

pygame.display.set_caption("Counter Striker 2D")
run = True
while run == True:
 Jugardor.dibujar(ventana)
 for event in pygame.event.get():
      
     #para cerrar el juego 
     if event.type == pygame.QUIT:
           run = False
      
if event.type == pygame.KEYDOWN:
      if event .key == pygame.K_a:
            print("Izquierda")
      if event .key == pygame.K_d:
            print("Derecha")
      if event .key == pygame.K_w:
            print("Arriba")
      if event .key == pygame.K_s:
            print("Abajo")

pygame.display.update()

pygame.quit()
