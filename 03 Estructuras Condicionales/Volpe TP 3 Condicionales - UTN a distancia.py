# Ejercicio 1 Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

print ("***Edad de usuario***")
mayoredad = 18
edadusuario = int(input("Ingrese su edad "))
if edadusuario > mayoredad:
    print ("Eres mayor de edad")
else:
    print ("No eres mayor de edad")


    -----------------------------------

    # Ejercicio 2 ) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por 
# pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar elmensaje “Desaprobado”.

print ("***Notas***")
aprobar = 6
notausuario = int(input("Ingrese su nota:  "))
if notausuario >= aprobar:
    print ("Aprobado")
else:
    print ("Desaprobado")


    -----------------------------------

    # Ejercicio 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.
print ("***Numeros pares e impares***")

numero1 = int(input("Ingrese un numero:  "))
if numero1 % 2 == 0:
    print ("Ha Ingresado un número par")
else:
    print ("Por favor, ingrese un número par")


    ---------------------------------

    # Ejercicio 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece: Niño/a: menor de 12 años. Adolescente: mayor o igual que 12 años y menor que 18 años.
# Adulto/a: mayor o igual que 30 años. Adulto/a: mayor o igual que 30 años.

print ("***Rangos de edad***")

edad = int(input("Ingrese su edad:  "))
if edad < 12:
    print ("Usted pertenece a la categoría: Niño/a, menor de 12 años.")
elif edad >= 12 and edad < 18:
    print ("Usted pertenece a la categoría: Adolescente, mayor o igual que 12 años y menor que 18 años.")
elif edad >= 18 and edad < 30:
    print ("Usted pertenece a la categoría: Adulto/a, mayor o igual que 30 años.")
else: 
    print ("Usted pertenece a la categoría: Adulto/a, mayor o igual que 30 años.")

    -------------------------------------
# Ejercicio 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla 
# "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string

print ("***Contraseña***")

contraseña = (input("Ingrese una contraseña:  "))
caracteres = len(contraseña)

if caracteres <= 14 and caracteres >= 8:
    print ("Ha ingresado una contraseña correcta")
else: 
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

------------------------------
#Ejercicio 6) escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y 
# las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range (5)]
print (f"Los números aleatorios son {numeros_aleatorios}")
moda = mode(numeros_aleatorios)
print(f"La moda es {moda}")
mediana = median(numeros_aleatorios)
print(f"La mediana es {mediana}")
media = mean(numeros_aleatorios)
print(f"La media es {media}")

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else: 
    print("Distribución normal")

-----------------------------------------------
#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.
print("*** Frase ***")

frase = input("Ingrese una frase o palabra: ")
ultima = frase[-1].lower()
if ultima == "a" or ultima == "e" or ultima == "i" or ultima == "o" or ultima == "u":
    print (f"{frase}!")
else:
    print(frase)

-----------------------------------------------
#8)
print("*** Nombre ***")

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese un número:\n1 - Mayúsculas\n2 - Minúsculas\n3 - Primera letra en mayúscula\n"))

if opcion == 1:
    print(nombre.upper())

elif opcion == 2:
    print(nombre.lower())

elif opcion == 3:
    print(nombre.title())

else:
    print("Opcion incorrecta")

------------------------------------------------
#9)
print("*** Terremoto ***")

magnitud = int(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)"
else:
    categoria = "Extremo (puede causar graves daños a gran escala)"

# Mostrar el resultado
print(f"La magnitud ingresada es {magnitud} y se clasifica como: {categoria}")

-----------------------------------------
#10) 
print("*** Período del año ***")

hemisferio = (input("Indique en que hemisferio se encuentra Norte (N) o Sur (S): "))
mes = int(input("Indique el mes con números: "))
dia = int(input("Indique el día: ")) 

if (mes== 12 and dia>21) or mes == 1 or mes == 2 or (mes== 3 and dia<= 20):
    if hemisferio.lower() == "n":
        print("Invierno")
    elif hemisferio.lower() == "s":
        print("Verano")

elif (mes== 3 and dia>21) or mes == 4 or mes == 5 or (mes== 6 and dia<= 20):
    if hemisferio.lower() == "n":
        print("Primavera")
    elif hemisferio.lower() == "s":
        print("Otoño")

elif (mes== 6 and dia>21) or mes == 7 or mes == 8 or (mes== 9 and dia<= 20):
    if hemisferio.lower() == "n":
        print("Verano")
    elif hemisferio.lower() == "s":
        print("Invierno")

elif (mes== 9 and dia>21) or mes == 10 or mes == 11 or (mes== 12 and dia<= 20):
    if hemisferio.lower() == "n":
        print("Otoño")
    elif hemisferio.lower() == "s":
        print("Primavera")

