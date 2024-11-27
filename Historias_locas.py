#Historias locas

"""
Ejemplo:
frase a completar: Mi nombre es ___________.

nombre = "Santiago Nisi"

print ("Mi nombre es " + nombre)
print ("Mi nombre es {} .format (nombre))
print (f"Mi nombre es {nombre})
"""
adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo: ")

madlib = (f"Programar es tan {adj}! "
          f"Siempre me emociona por que me encanta {verbo1} problemas. "
          f"Aprende a {verbo2} y alcanza tus {sustantivo_plural}!")


print(madlib)
