def algoritmoalstar(inicio, objetivo, grid):
    # Algoritmo A* para encontrar el camino más corto en una cuadrícula

    def heuristica(nodo_a, nodo_b):
        # Calcula la distancia Manhattan entre dos punto
        return abs(nodo_a[0] - nodo_b[0]) + abs(nodo_a[1] - nodo_b[1])
    

    abiertos = [inicio] # Nodos por explorar
    padres = {inicio: None}  # Diccionario para reconstrucción del camino
    g_costos = {inicio: 0}  # Coste desde el inicio hasta cada nodo
    f_costos = {inicio: heuristica(inicio, objetivo)}  # Estimación del coste total

    while abiertos:
        # Elegir el nodo con el menor costo f
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
            return camino[::-1]  # Devolver en orden correcto

        # Generar vecinos (movimiento en 4 direcciones)
        vecinos = [(actual[0], actual[1] - 1), (actual[0], actual[1] + 1),
                   (actual[0] - 1, actual[1]), (actual[0] + 1, actual[1])]

        for vecino in vecinos:
            if vecino not in grid or grid[vecino] == 1:  # Evitar obstáculos
                continue

            nuevo_g = g_costos[actual] + 1
            if vecino not in g_costos or nuevo_g < g_costos[vecino]:
                g_costos[vecino] = nuevo_g
                f_costos[vecino] = nuevo_g + heuristica(vecino, objetivo)
                padres[vecino] = actual

                if vecino not in abiertos:
                    abiertos.append(vecino)

    return []  # No se encontró camino
