def algoritmoalstar(inicio, objetivo, grid):
    # Algoritmo A* para encontrar el camino más corto en una cuadrícula

    def heuristica(nodo_a, nodo_b):
        # Calcula la distancia Manhattan entre dos puntos
        return abs(nodo_a[0] - nodo_b[0]) + abs(nodo_a[1] - nodo_b[1])

    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Movimientos en 4 direcciones
    abiertos = [inicio]  # Lista de nodos por explorar
    padres = {inicio: None}  # Diccionario para reconstrucción del camino
    g_costos = {inicio: 0}  # Coste desde el inicio hasta cada nodo
    f_costos = {inicio: heuristica(inicio, objetivo)}  # Estimación del coste total

    while abiertos:
        # Encontrar el nodo con menor f_cost manualmente
        actual = abiertos[0]
        for nodo in abiertos:
            if f_costos[nodo] < f_costos[actual]:
                actual = nodo

        abiertos.remove(actual)

        if actual == objetivo:
            # Reconstruir el camino
            camino = []
            while actual:
                camino.append(actual)
                actual = padres[actual]
            return camino[::-1]  # Devolver el camino en orden correcto

        for dx, dy in movimientos:
            vecino = (actual[0] + dx, actual[1] + dy)

            # Verificar que el vecino está dentro del grid y no es un obstáculo
            if vecino in grid and grid[vecino] == 0:
                nuevo_g = g_costos[actual] + 1  # Costo de moverse a un vecino

                if vecino not in g_costos or nuevo_g < g_costos[vecino]:
                    g_costos[vecino] = nuevo_g
                    f_costos[vecino] = nuevo_g + heuristica(vecino, objetivo)
                    padres[vecino] = actual
                    abiertos.append(vecino)  # Agregar el vecino a la lista de exploración

    return None  # No hay camino posible
