from random import choice
#Funcion para elegir la palabra al azar
def palabra_al_azar():
    return choice(["Perro", "Dog", "Cat", "Gato","Conejo","Mouse"])
#Funcion para convertir la palabra a guiones
def convertir_guiones(palabra_secreta):
    guiones = []
    for n in palabra_secreta:
        guiones.append("_")
    return guiones
#Funcion para verificar si se ingresa una letra
def verificar ():
    letra = "%"
    while letra not in "abcdefghijklmnñopqrstuvwxyz":
        letra = input("Ingresa una letra: ")
    return letra
#Funcion Comienza el juego
palabra_secreta = list(palabra_al_azar())
guiones = convertir_guiones(palabra_secreta)
lista_incorrectos = []
vidas = 7
print("""
Bienvenido a el juego ahorcado 
el juego se trata que adivines la palabra de animales 
puedes escribir una letra para adivinar la palabra tienes 7 vidas 

""")
while True:
    intento = verificar()
    if intento in palabra_secreta:
        for n in range(len(palabra_secreta)):
            if intento == palabra_secreta[n]:
                guiones[n] = intento
                print(guiones)
        if guiones == palabra_secreta:
            print("Felicidades adivinaste!")
            palabra = "".join(palabra_secreta)
            print(f" La palabra es {palabra}")
    else:
        lista_incorrectos.append(intento)
        print("Lista de intentos incorrectos ")
        print(lista_incorrectos)
        vidas -= 1

        if vidas == 0:
            print("Game over")
            palabra = "".join(palabra_secreta)
            print(f" La palabra era {palabra}")
            break
