#Palíndromos: Un palíndromo es una palabra, frase, número u otro tipo de unidad que se puede leer igual 
#hacia adelante que hacia atrás (ignorando espacios, acentos y signos de puntuación), como "anilina" o 
#"reconocer". Escribe un programa en Python que detecte si una frase dada es un palíndromo

def es_palindromo(frase):
    frase = frase.lower().replace(" ", "").replace(",", "").replace(".", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    return frase == frase[::-1]

frase = input("Introduce una frase: ")

if es_palindromo(frase):
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")
