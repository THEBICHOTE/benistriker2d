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
