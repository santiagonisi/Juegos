#Adivina el numero

import random


def adivina_el_numero (x):

    print("======================")
    print("Bienvenido/a al juego!")
    print("======================")

    print("El objetivo del juego es adivinar el numero generado por la computadora")

    numero_aleatorio = random.randint(1, x)
    prediccion = 0

    while prediccion != numero_aleatorio:
        #El usuario ingresa un numero:
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: ")) #f-string

        if prediccion < numero_aleatorio:
            print("Intentalo de nuevo, el numero ingresado es muy chico.")

        elif prediccion > numero_aleatorio:
            print("Intentalo de nuevo, el numero ingresado es muy grande.")

    print(f"Felicitaciones! adivinaste el numero {numero_aleatorio}")


adivina_el_numero(20)