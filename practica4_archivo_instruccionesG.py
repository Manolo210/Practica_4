import turtle
#Configuracion de pantalla
pantalla = turtle.Screen()
pantalla.setup(width=600, height=600)
pantalla.title("Dibujos con instrucciones")
pantalla.bgcolor("pink")
#Funcion para mover la tortuga
def teleport(x, y):
    t = turtle.Turtle()
    t.penup()
    t.goto(x, y)
    t.hideturtle()

#Funcion para dibujar cuadrado
def cuadradodibujo(x, y, lado, color):
    cuadrado = turtle.Turtle()
    cuadrado.speed(5)
    cuadrado.pencolor('red')
    cuadrado.pensize(6)
    cuadrado.fillcolor(color)
    cuadrado.penup()
    cuadrado.goto(x, y)
    cuadrado.setheading(0)
    cuadrado.pendown()
    cuadrado.begin_fill()
    cuadrado.forward(lado)
    cuadrado.left(90)
    cuadrado.forward(lado)
    cuadrado.left(90)
    cuadrado.forward(lado)
    cuadrado.left(90)
    cuadrado.forward(lado)
    cuadrado.left(90)
    cuadrado.end_fill()
    cuadrado.hideturtle()

#Funcion para dibujar triangulos
def triangulodibujo(x, y, lado, color):
    triangulo = turtle.Turtle()
    triangulo.speed(5)
    triangulo.pencolor('blue')
    triangulo.pensize(5)
    triangulo.fillcolor(color)
    triangulo.penup()
    triangulo.goto(x, y)
    triangulo.setheading(0)
    triangulo.pendown()
    triangulo.begin_fill()
    triangulo.forward(lado)
    triangulo.left(120)
    triangulo.forward(lado)
    triangulo.left(120)
    triangulo.forward(lado)
    triangulo.left(120)
    triangulo.end_fill()
    triangulo.hideturtle()

#Funcion para dibujar circulo
def circulodibujo(x, y, radio, color):
    circulo = turtle.Turtle()
    circulo.speed(5)
    circulo.pencolor(color)
    circulo.pensize(5)
    circulo.fillcolor(color)
    circulo.penup()
    circulo.goto(x, y)
    circulo.setheading(0)
    circulo.pendown()
    circulo.begin_fill()
    circulo.circle(radio)
    circulo.end_fill()
    circulo.hideturtle()

#Funion para dibujar linea
def lineadibujo(x, y, longitud, color):
    linea = turtle.Turtle()
    linea.speed(5)
    linea.pencolor(color)
    linea.pensize(5)
    linea.penup()
    linea.goto(x, y)
    linea.setheading(0)
    linea.pendown()
    linea.forward(longitud)
    linea.hideturtle()

#Función para ejecutar una instrucción
def ejecutar_instruccion(linea):
    partes = linea.strip().split()
    if len(partes) == 0:
        return
    comando = partes[0].lower()
    args = partes[1:]
    try:
        if comando == "cuadrado":
            x = float(args[0])
            y = float(args[1])
            lado = float(args[2])
            color = args[3]
            cuadradodibujo(x, y, lado, color)
        elif comando == "triangulo":
            x = float(args[0])
            y = float(args[1])
            lado = float(args[2])
            color = args[3]
            triangulodibujo(x, y, lado, color)
        elif comando == "circulo":
            x = float(args[0])
            y = float(args[1])
            radio = float(args[2])
            color = args[3]
            circulodibujo(x, y, radio, color)
        elif comando == "linea":
            x = float(args[0])
            y = float(args[1])
            longitud = float(args[2])
            color = args[3]
            lineadibujo(x, y, longitud, color)
        elif comando == "teleport":
            x = float(args[0])
            y = float(args[1])
            teleport(x, y)
        else:
            print("Instrucion rara:", linea.strip())
    except Exception as error:
        print("Error en la instruccion'{}': {}".format(linea.strip(), error))

#Lee el aarchivo y ejecuta las intrucciones
try:
    archivo = open("dibujante.txt")
    for linea in archivo:
        ejecutar_instruccion(linea)
    archivo.close()
except FileNotFoundError:
    print("No se encontro el archivo 'dibujante.txt'")

turtle.done()
