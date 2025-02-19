import pygame
import constantes
pygame.init ()
ANCHO_VENTANA = 900
Alto_VENTANA = 680
ventana= pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Counter Striker 2D")
run = True


while run == True:
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
          run = False
pygame.quit()
