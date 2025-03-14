import pygame

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))  # Color rojo para identificarlo
        self.rect = self.image.get_rect(topleft=(x, y))

    def dibujar(self, ventana):
        ventana.blit(self.image, self.rect)
