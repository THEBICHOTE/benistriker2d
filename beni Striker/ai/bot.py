import random
from ai.behavior_tree import Selector, Sequence, Task
from ai.tasks import patrullar, detectar_enemigo, atacar, buscar_cobertura

class Bot:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.direccion = random.choice([-1, 1])
        self.speed = 2
        self.vida = 100
        self.target = None  # Se asignará un enemigo

        # Crear el Árbol de Comportamiento
        self.tree = Selector([
            Task(buscar_cobertura),  # Si tiene poca vida, busca cobertura
            Sequence([
                Task(detectar_enemigo),  # Si ve un enemigo...
                Task(atacar)  # ...intenta atacar
            ]),
            Task(patrullar)  # Si no hay enemigo, patrulla
        ])

    def update(self):
        """Actualizar lógica de la IA en cada frame"""
        self.tree.run(self)

    def disparar(self):
        """Simulación de disparo"""
        print("¡Bot dispara!")  
