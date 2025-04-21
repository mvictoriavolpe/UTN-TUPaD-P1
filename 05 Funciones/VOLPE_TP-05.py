# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

print(saludar_usuario (input("Ingrese su nombre: ")))

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
#  Pedir los datos al usuario y llamar a esta función con los valores ingresados
#Funcion
def informacion_personal(nombre, apellido, edad, residencia): 
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

#Pedir datos al usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

#Llamado de la funcion
print(informacion_personal(nombre, apellido, edad, residencia))

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados

import math

def calcular_area_circulo(radio):
    print(f" El área del círculo es: {math.pi * radio **2:.2f}")

def calcular_perimetro_circulo(radio):
    print(f"El área perímetro del círculo es: { 2*math.pi*radio:.2f}")


radio = int(input("Ingrese el radio: "))

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
 # Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_horas(segundos):
    return segundos / 3600

#programa principal
segundos = int(input("Ingresá la cantidad de sengundos: "))
horas = segundos_horas(segundos)
print(f"{segundos} equivale a {horas:.2f} hora/s.")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. 
 # Pedir al usuario el número y llamar a la función

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
numero = int(input("Ingresá un número: "))
tabla_multiplicar(numero)

 #7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una 
 # tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.
 #  Mostrar los resultados de forma clara

def operaciones_basicas(a,b):
    print(f"Suma: {a + b}")
    print(f"Resta: {a - b}")
    print(f"Multiplicación: {a * b}")
    if b != 0:
        print(f"División: {a / b}")
    else:
        print("División: Indefinida (no se puede dividir por cero)")

a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))

operaciones_basicas(a, b)

 # 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC).
 #  Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales

def calcular_imc(peso, altura):
    imc = peso/altura**2
    return imc

peso = float(input("Ingrese su peso: "))

altura = float(input("Ingrese la altura: "))

print(f"Su IMC es {calcular_imc(peso, altura):.2f}")

 # 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. 
 # Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

print(f"{celsius} °C son {celsius_a_fahrenheit(celsius):.2f} °F")

 # 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. 
 # Solicitar los números al usuario y mostrar el resultado usando esta función

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio de los tres números es: {promedio:.2f}")