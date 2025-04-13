#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), 
# en orden creciente, mostrando un número por línea.

for i in range (101):
    print (i)

-----------------
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 

numero = int(input("Ingrese un número entero: "))
digitos = 0

while numero > 0:
    numero = numero//10
    digitos += 1

print (f"El número ingresado tiene {digitos} dígitos. ")

------------------------
#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

numero1 = int(input("Ingrese un número entero: "))
numero2 = int(input("Ingrese un número entero: "))

suma = 0

if numero1 < numero2:
    for i in range (numero1 +1, numero2):
        suma = suma + i

elif numero1 > numero2:
    for i in range (numero2 +1, numero1):
        suma = suma + i
else:
    print ("Ingresó numeros iguales")

print (f"El total de la suma de los números comprendidos entre {numero1} y {numero2} es {suma}")

-------------------------
#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total
#  acumulado cuando el usuario ingrese un 0.

suma = 0

while True:
    numero = int(input("Ingrese un número entero (ingrese 0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print(f"El la suma total de los números ingresados es {suma}")

------------------

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random

numero_aleatorio = random.randint (0,9)
intentos = 0

while True:
    numero = int(input("Adiviná un número entre 0-9: "))
    if numero == numero_aleatorio:
        break
    intentos += 1

print(f"Adivinaste! El número secreto era {numero_aleatorio}, adivinaste en {intentos} intentos")

----------------------

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

for i in range (100 , 0, -1):
    if i % 2 == 0:
        print (i)

--------------------------------
#7) Crea un programa que calcule la suma de todos los números
#  comprendidos entre 0 y un número entero positivo indicado por el usuario.

suma = 0
numero = int(input("Ingrese un número positivo: "))

for i in range (0, numero+1):
    suma = suma + i
print (f"El total de la suma es {suma}")

---------------------------------
#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range (0,100):
    numero = int(input("Ingrese un número "))
    if numero % 2 == 0:
        pares += 1
    else: 
        impares += 1
    if numero >= 0:
        positivos +=1
    else:
        negativos += 1

print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)

--------------------------------
#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).

suma = 0

for i in range (0, 100):
    numero = int(input("Ingrese un numero: "))
    suma = suma + numero
promedio = suma/100
print("El promedio de los numeros ingresados es", promedio)

--------------------------------
#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#  usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.


digito = 0
inverso = 0
numero = int(input("Ingrese un número entero: "))

while numero != 0:
    digito = numero % 10
    numero = numero//10
    inverso = inverso *10 + digito
print("El inverso al numero ingresado es", inverso) 