# input y nombre por default
# Instrucciones
# variables maximo 100 minimo 1
#intentos vidas = 8
# comando ramdom para obtener un numero de 1 a 100
# contador intentos
# comando while para hacer el juego funcionar mientras tenga vidas
# comando if para verificar si acerto o no
# import random usa todos los comandos de ramdom
# Bibliotecas con funciones especiales
from random import randint

# Saludos e inio del juego
nombre = input("Ingresa tu nombre: ")
print(f"Bueno , {nombre}, he pensado en un numero entre 1 y 100.")
print("Tienes solo 8 intentos para adivinarlo")

# Numero secreto aleatorio
numero_secreto = randint(1, 100)
intentos = 0
vidas = 0
max_intentos = 8

# Ciclo de intentos
while vidas < max_intentos:
    intentos = int(input("Ingresa un numero entre  1 y 100: "))
    if intentos <1 or intentos > 100:
        print("Numero no permitido")
    elif intentos < numero_secreto:
        print(" Incorrecto, el numero secreto es mayor ")
    elif intentos > numero_secreto:
        print(" Incorrecto, el numero secreto es menor ")
    else:
        print(f" Haz, Ganado el numero era {numero_secreto}")
        break
    vidas += 1

