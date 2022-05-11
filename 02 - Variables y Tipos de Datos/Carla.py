## Variables

##1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

from configparser import ConfigParser
import math
from operator import concat
from pickle import TRUE


a = 5
print(a)


##2) Imprimir el tipo de dato de la constante 8.5

x = 8.5
print(type(x))

##3) Imprimir el tipo de dato de la variable creada en el punto 1

print(type(a))

##4) Crear una variable que contenga tu nombre

variable_nombre = "Soy Carla"
print(variable_nombre)

##5) Crear una variable que contenga un número complejo

complejo = 5j
print(complejo)


##6) Mostrar el tipo de dato de la variable crada en el punto 5

print(type(complejo))


##7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

pi = 3.1416

##8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

#No, no se trata de lo mismo, 'true' es la palabra y True es el booleano

p = 'True'
a = True
print(p)
print(a)


##9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

print(type(p))
print(type(a))

##10) Asignar a una variable, la suma de un número entero y otro decimal

suma = 5 + 5.2
print(suma)

##11) Realizar una operación de suma de números complejos

suma_complejos = 5j + 3j
print(suma_complejos)

##12) Realizar una operación de suma de un número real y otro complejo

suma_real_complejo = 5 + 3j
print(suma_real_complejo)

#13) Realizar una operación de multiplicación

multiplicacion = 5 * 3

#14) Mostrar el resultado de elevar 2 a la octava potencia

potencia = 2**8

##15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

division_cociente = int(27 // 4)
print(division_cociente)

##16) De la división anterior solamente mostrar la parte entera

print(division_cociente)

##17) De la división de 27 entre 4 mostrar solamente el resto

division_resto = 27%4
print(division_resto)

##18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

sumandos = (4 * division_cociente) + division_resto
print(sumandos)
##19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

alfanumericas = (str) ("Carla " + "esta " + "aprendiendo " + "python " + "100 ")
alfa1 = "Copa" " "
alfa2 = "de vino"
print(alfanumericas)
print(alfa1 + alfa2)
##20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
a = 2
b = '2'
print (2 == '2')
print (type (a))
print (type (b))


##21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
b = int ('2')
a = 2
print (a == b)

##22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
## por que 3,8 no es un float es una tupla

##23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido


##24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

##Por que corre 2 lugares a la derecha en binario, queda 100 que en binario es 4

##25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
#print (2 + '2')

#No esta permitido por que es un str y un int.

##26) Realizar una operación válida entre valores de tipo entero y string
var1 = 'este texto se repite '
var2 = 3
print(var1 * var2 + str(var2) + ' veces')