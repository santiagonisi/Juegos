#Adivina el numero computadora
import random

def adivina_el_numero_computadora(x):

    print("======================")
    print("Bienvenido/a al juego!")
    print("======================")

    print(f"Selecciona un numero entre 1 y {x} para que la computadora lo adivine")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""

    # Miestras el usuario no indique que la respuesta es correcta,
    # continuar el proceso.

    while respuesta != "c":
        # Generar predicción
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior  # también podría ser límite_superior porque los límites son iguales.

        # Obtener respuesta del usuario
        respuesta = input(
            f"Mi predicción es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta ingresa (C) ").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"¡Siii! La computadora adivinó tu número correctamente: {prediccion}")


adivina_el_numero_computadora(10)
