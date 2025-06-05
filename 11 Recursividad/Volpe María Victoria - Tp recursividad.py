# 1. Crea una función recursiva que calcule el factorial de un número. 
# Luego, utiliza esa  función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el
#  número que indique el usuario 
def factorial (n):
    if n == 0:
        return 1
    else: 
        return n* factorial(n-1)

while True:
    try:
        limite = int(input("Ingresá un número entero mayor o igual a 1: "))
        if limite >= 1:
            break
        else:
            print(" Por favor, ingresá un número mayor o igual a 1.")
    except ValueError:
        print(" Eso no es un número válido. Intentá de nuevo.")
    
print(f"\nFactoriales del 1 al {limite}:")
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")



#2. Serie de Fibonacci
#posición:  0  1  2  3  4  5  6  7  ...
#valor:     0  1  1  2  3  5  8  13 ...

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ingrese hasta qué posición quiere ver la serie de Fibonacci: "))

print(f"El valor de la Serie de fibonnaci en la posición indicada {posicion} es  {fibonacci(posicion)}")

print("Serie completa de Fibonacci:")

for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")




#3.  Crea una función recursiva que calcule la potencia de un número base elevado a un exponente

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Pedir al usuario los valores
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

# Calcular y mostrar el resultado
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es igual a: {resultado}")

#4. Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto. 

def calcula(cociente):
    if cociente == 0:
        return
    
    print(cociente % 2)
    calcula(int(cociente/2))


numero = int(input("Ingresá un número entero positivo: "))
calcula(numero)

#5. Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es. 

def es_palindromo(palabra):
    if len(palabra) <=1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

mipalabra = input("Ingresá una palabra (sin espacios ni tildes): ").lower()

if es_palindromo(mipalabra):
    print("¡Es un palíndromo!")
else:
    print("No es un palíndromo.")


#6. Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 

def suma_digitos(n):
    if n == 0:
        return 0

    return (n % 10) + suma_digitos(n // 10)

print(suma_digitos(1501))
print(suma_digitos(8)) 
print(suma_digitos(442)) 

#7. Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide. 

def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)

bloques = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
total = contar_bloques(bloques)
print(f"El total de bloques que necesitas es: {total}")


#8. Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número

#8. Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número

def contar_digito (numero, digito):
    if numero == 0:
        return 0
    ultimodigito = numero % 10

    if ultimodigito == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito a buscar: "))

resultado = contar_digito(numero, digito)
print(f"El dígito {digito} aparece {resultado} veces en {numero}")