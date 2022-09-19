#Escribir un programa que pregunte al usuario su edad 
# y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

numero = int(input('Ingrese su edad: '))
i = 1

while i <= numero:
    print('Edades hasta la fecha: {}'.format(i))
    i +=1