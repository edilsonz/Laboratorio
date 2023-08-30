#Contar caracteres y palabras: Dada la siguiente frase: "Estoy aprendiendo Python y me está
#gustando mucho. ¡Es genial!". Escribe un programa en Python que cuente el número de palabras y de
#caracteres (incluyendo espacios y signos de puntuación)
def contar_caracteres_palabras(frase):
    caracteres_totales = len(frase)
    palabras = frase.split()
    num_palabras = len(palabras)
    
    return caracteres_totales, num_palabras

frase = "Estoy aprendiendo Python y me está gustando mucho. ¡Es genial!"
caracteres, palabras = contar_caracteres_palabras(frase)

print(f"Número de caracteres: {caracteres}")
print(f"Número de palabras: {palabras}")