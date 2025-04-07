import turtle

# Configuración de la ventana
main_width = 600
main_height = 600
turtle.setup(main_width, main_height)
turtle.speed(0)  # Velocidad máxima
turtle.bgcolor("white")
turtle.hideturtle()

def dibujar_cuadrado(x, y, size):
    """Dibuja un cuadrado con la esquina inferior izquierda en (x, y)."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

def fractal_cuadrado_apilado(x, y, size, nivel):
    """Dibuja un fractal de cuadrados apilados verticalmente."""
    if nivel == 0:
        return

    # Dibujar el cuadrado actual
    dibujar_cuadrado(x, y, size)

    # Posición del siguiente cuadrado (arriba del actual)
    new_x = x + size * 0.25  # Moverlo un poco hacia el centro
    new_y = y + size          # Apilado arriba
    new_size = size * 0.75    # Reducir tamaño del siguiente cuadrado

    # Dibujar el siguiente cuadrado apilado
    fractal_cuadrado_apilado(new_x, new_y, new_size, nivel - 1)

def main():
    import numpy as np

    # Crear un array de 5 dimensiones con valores aleatorios entre 0 y 10
    numeros_derecha = np.random.randint(0, 10, (2, 3, 4, 5, 6))

    # Ver el array
    print(numeros_derecha)
    """Función principal para dibujar el árbol fractal apilado."""
    size = 200  # Tamaño del cuadrado base
    nivel = 5   # Niveles de profundidad

    # Dibujar el fractal con el cuadrado inicial centrado en la base
    fractal_cuadrado_apilado(-size // 2, -main_height // 2 + 50, size, nivel)

    turtle.done()  # Mantener la ventana abierta

# Ejecutar el dibujo
main()