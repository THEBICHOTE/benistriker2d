import pygame
import constantes

class bala(pygame.sprite.Sprite):
    def __init__(self, x, y, direccion):
        super().__init__()
        self.image = pygame.Surface([5, 5])
        self.image.fill((255, 255, 0))  # Bala amarilla
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direccion = direccion
        self.velocidad = constantes.BALA_VELOCIDAD

    def update(self):
        self.rect.x += self.velocidad * self.direccion

    def dibujar(self, ventana):
        ventana.blit(self.image, self.rect)