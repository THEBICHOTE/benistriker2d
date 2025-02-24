import pygame

class Jugardor():
    def __init__ (self, x, y):
        self.forma = pygame.Rect(0,0,40,40)
        self.forma.center = (x,y)

    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, (255, 255,0), self.forma)
                 
