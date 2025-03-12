import pygame

class Jugador:
    def __init__(self, x, y):
        self.forma = pygame.Rect(0, 0, 40, 40)
        self.forma.center = (x, y)
        self.velocidad = 5  # Se puede cambiar la velocidad fácilmente
        self.color = (255, 255, 0)  # Color Amarillo

    def movimiento(self, delta_x, delta_y):
        self.forma.move_ip(delta_x, delta_y)  # Método más eficiente para mover

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, self.forma)
