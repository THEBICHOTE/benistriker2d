import pygame

class obstaculo (pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        self.image = pygame.Surface([ancho, alto])
        # obstaculo gris
        self.image.fill((128, 128, 128))  
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def dibujar(self, ventana):
        ventana.blit(self.image, self.rect)