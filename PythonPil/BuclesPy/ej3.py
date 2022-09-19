#Imprimir por pantalla los numeros del 1 al 10, luego, 
# pedir al usuario dos numeros y mostrar el rango de 
# numeros entre ambas cifras

for i in range (1, 11):
    print(i)
    #muestra 1-10

num1 = int(input('Ingresa la primer cifra: '))
num2 = int(input('Ingresa la segunda cifra: '))

for i in range(num1, num2 + 1): #porque el de la der no se toma en cuenta y se suma
    print(i)

#ver si el primer numero es mayor