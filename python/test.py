import turtle

MAX_DEPTH = 3

def hoja(profundidad=0):
    if profundidad > MAX_DEPTH:
        return
    global t
    t.pendown()
    longitud = 100 * (2/3)**profundidad

    t.forward(longitud)
    t.left(60)
    hoja(profundidad+1)
    t.right(120)
    hoja(profundidad+1)
    t.right(120)
    t.forward(longitud)
    t.left(180)

window = turtle.Screen()
window.title("División de Rectángulos")
window.setup(width=600, height=600)  
window.tracer(0)  

t = turtle.Turtle()
t.speed(0)  
hoja()
window.update()  # ← Actualiza manualmente la pantalla

window.mainloop()  # Para que la ventana no se cierre inmediatamente
