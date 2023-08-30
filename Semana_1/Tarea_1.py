#Tarea: Vamos a hacer un pequeño programa que haga lo siguiente:
#Pida al usuario que introduzca 5 números.
#Guarde esos números en una lista.
#Calcule y muestre la media de esos números.

numeros = []
for i in range(5):
    num = float(input("Ingrese un número: "))
    numeros.append(num)

suma = sum(numeros)
media = suma / 5

print("La media de los números es:", media)