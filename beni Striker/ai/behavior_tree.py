class Node:
    """Nodo base del Árbol de Comportamiento"""
    def run(self, bot):
        pass  # Se sobrescribe en nodos hijos

class Selector(Node):
    """Ejecuta hijos hasta que uno tenga éxito"""
    def __init__(self, hijos):
        self.hijos = hijos

    def run(self, bot):
        for hijo in self.hijos:
            if hijo.run(bot):  
                return True  # Si un hijo tiene éxito, termina
        return False

class Sequence(Node):
    """Ejecuta hijos en orden, falla si uno falla"""
    def __init__(self, hijos):
        self.hijos = hijos

    def run(self, bot):
        for hijo in self.hijos:
            if not hijo.run(bot):  
                return False  # Si un hijo falla, toda la secuencia falla
        return True

class Task(Node):
    """Nodos hoja con acciones específicas"""
    def __init__(self, action):
        self.action = action

    def run(self, bot):
        return self.action(bot)  # Ejecuta la acción y devuelve éxito o fallo
class DispararSiCerca:
    def ejecutar(self, enemigo, jugador):
        # Lógica para disparar si el jugador está cerca
        pass

class PerseguirJugador:
    def ejecutar(self, enemigo, jugador):
        # Lógica para perseguir al jugador
        pass

class Patrullar:
    def ejecutar(self, enemigo, jugador):
        # Lógica para patrullar
        pass

