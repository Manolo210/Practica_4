# Practica 4

>En esta practica utilizamos de nuevo la libreria de turtle para dibujar las figuras teleport, cuadrado, triangulo, circulo y linea.

### Que es lo que hara?

Vamos a leer el archivo de texto de instrucciones que contendra por ejemplo:

- cuadrado 0 0 100 red\
- triangulo -150 -100 100 blue\
- circulo 150 100 60 black\
- linea 200 -100 -100 green\
- teleport 0 0

Y dibuja esas figuras automáticamente en una ventana de 600x600 con fondo rosa.

### Paso # 1
>Creamos la carpeta "Practica 4". Seguido de eso creamos los tres archivos dentro de esa carpeta que son:
- practica4_archivo_instruccionesG.py.
- dibujante.txt
- README.md

En el archivo practica4... vamos hacer el todo el codigo que hara los dibujos de las figuras. Luego en el archivo dibujante.txt vamos a hacer las instrucciones
que recibira el cel archivo .py, ambos estaran enlazados. Y por ultimo en README.md vamo a hacer
la explicacion o ducmentacion de la practica.

### Paso #2
>#Que tendra el codigo?

+ Configuracion de la pantalla 
+ configuracion de la tortuga

import turtle

    #Configuracion de pantalla

    pantalla = turtle.Screen()\
    pantalla.setup(width=600, height=600)\
    pantalla.title("Dibujos con instrucciones")\
    pantalla.bgcolor("pink")

    #Funcion para mover la tortuga
    def teleport(x, y):

    t = turtle.Turtle()
    t.penup()
    t.goto(x, y)
    t.hideturtle()

### Paso #3

>Vamos a crear las funciones cuadrado, circulo, y triangulo

### Paso #4

>Crearemos la funcion para ejecutar una instruccion

### Paso #5

>Vamos a leer el archivo dibujante.txt para que ejecute las instrucciones.

Asi quedaria esta parte:

    try:
        archivo = open("dibujante.txt")
        for linea in archivo:
            ejecutar_instruccion(linea)
        archivo.close()
    except FileNotFoundError:
        print("No se encontro el archivo 'dibujante.txt'")

### Paso #6

>Por ultimo haremos las instrucciones en el archivo de texto dibujante.txt

###### Cabe aclarar que utilice IA para que me mostrara como enlazar la parte del dibujante.txt al codigo.py y era solo utilizar open() siendo como el "objeto" en poo.

Quedaria asi:

    cuadrado -150 100 99 red
    triangulo -150 -100 100 blue
    circulo 150 100 60 black
    linea 200 -100 -100 green
    teleport 0 0

### Conclusion

Para esta practica utilice mis funciones de las figuras y solo agregue otras funciones como el teleport que ya lo utilice en la practica 1 pero aqui la hacemos funciones
para poder utilizarla en el archivo de texto y que la totuga se mueva al centro y no deje rastro. Tambien usamos except por si no se encuentra el archico dibujante.txt.
