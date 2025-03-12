# Counter-Strike 2D - Pygame

## 📌 Descripción

Este es un juego 2D inspirado en Counter-Strike, desarrollado con **Pygame**.\
Incluye un sistema de movimiento para el jugador y un **NPC con inteligencia artificial** que usa el **algoritmo A**\* para encontrar el camino más corto hacia el jugador.

## 🎮 Controles del Juego

- **Moverse**:
  - `W` → Arriba
  - `S` → Abajo
  - `A` → Izquierda
  - `D` → Derecha
- **Cerrar el juego**: Presionar `Esc` o cerrar la ventana

## 🛠️ Requisitos

Para ejecutar el juego necesitas tener instalado **Python 3**.

## 🚀 Instalación y Ejecución

1. **Clonar el repositorio** o descargar los archivos.
2. **Ejecutar el juego** con el siguiente comando:
   ```bash
   python main.py
   ```

## 🧠 Algoritmo A\*

El juego implementa el **algoritmo A**\* para calcular la mejor ruta entre dos puntos evitando obstáculos.\
El código se encuentra en `algoritmoalstar.py`.

## 📂 Estructura del Proyecto

```
📁 Counter-Strike 2D
│── main.py                 # Código principal del juego
│── jugador.py              # Clase del jugador
│── algoritmoalstar.py      # Implementación del algoritmo A*
│── constantes.py           # Variables del juego
│── README.md               # Este archivo
```

## 📢 Créditos

Desarrollado por Wilbel Benitez.
