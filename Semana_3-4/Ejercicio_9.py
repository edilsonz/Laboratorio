#Cifrado César: El cifrado César es una técnica de cifrado simple en la que cada letra en el texto original se 
#reemplaza por una letra un cierto número de posiciones más adelante en el alfabeto. Por ejemplo, con un 
#desplazamiento de 1, "A" se reemplazaría por "B", "B" se convertiría en "C", etc. Escribe un programa que 
#implemente el cifrado César para un mensaje y un desplazamiento dados
mensaje = input("Introduce el mensaje a cifrar: ")
desplazamiento = int(input("Introduce el desplazamiento: "))

mensaje_cifrado = ""

for letra in mensaje:
    if letra.isalpha():
        letra_cifrada = chr((ord(letra) - 65 + desplazamiento) % 26 + 65)
    else:
        letra_cifrada = letra
    mensaje_cifrado += letra_cifrada

print("El mensaje cifrado es:", mensaje_cifrado)