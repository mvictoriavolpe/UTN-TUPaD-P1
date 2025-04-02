# Ejercicio 1 Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

print ("***Edad de usuario***")
mayoredad = 18
edadusuario = int(input("Ingrese su edad "))
if edadusuario > mayoredad:
    print ("Eres mayor de edad")
else:
    print ("No eres mayor de edad")