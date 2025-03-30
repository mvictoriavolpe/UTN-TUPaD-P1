#-------------------- problema 1
print ("Hola Mundo!")

#-------------------- problema 2
nombre = input ("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#-------------------- problema 3
nombre = input ("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Infrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#-------------------- problema 4
import math
radio = int(input("Ingrese el radio de un círculo: "))
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
print(f"El área del círculo es {area}")
print(f"El perimetro del círculo es {perimetro}")

#-------------------- problema 5
segundos = int(input("Ingrese la cantidad de segundos: "))
porcionhora = segundos/3600
print(f"La cantidad de segundos ingresados {segundos} corresponde a  {porcionhora} horas")

#-------------------- problema 6
multiplica = int(input("Ingrese un número: "))
print(f"La tabla de multiplicar de {multiplica} es: ")
print(f" {multiplica} x 1 = {multiplica * 1}")
print(f" {multiplica} x 2 = {multiplica * 2}")
print(f" {multiplica} x 3 = {multiplica * 3}")
print(f" {multiplica} x 4 = {multiplica * 4}")
print(f" {multiplica} x 5 = {multiplica * 5}")
print(f" {multiplica} x 6 = {multiplica * 6}")
print(f" {multiplica} x 7 = {multiplica * 7}")
print(f" {multiplica} x 8 = {multiplica * 8}")
print(f" {multiplica} x 9 = {multiplica * 9}")
print(f" {multiplica} x 10 = {multiplica * 10}")

#-------------------- problema 7
numero1 = int(input("Ingrese un número entero distitno del 0: "))
numero2 = int(input("Ingrese un número entero distitno del 0: "))
print(f"{numero1} + {numero2} = {numero1+numero2}")
print(f"{numero1} - {numero2} = {numero1-numero2}")
print(f"{numero1} x {numero2} = {numero1*numero2}")
print(f"{numero1} / {numero2} = {numero1/numero2}")

#-------------------- problema 8
peso = float(input("Ingrese su peso en kg: "))
altura= float(input("Ingrese su altura en metros: "))
masacorporal= peso/(altura**2)
print(f"Su Iíndice de Masa corporal es: {masacorporal}")

#-------------------- problema 9
celsius = float(input("Ingrese la temperatura en grados celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius} ° C equivalen a {fahrenheit}° F")

#-------------------- problema 10
numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese un número: "))
numero3= int(input("Ingrese un número: "))
promedio = (numero1 + numero2 + numero3) /3
print(f"El promedio es: {promedio}")
