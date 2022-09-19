#Escribir una función que reciba un número entero 
# positivo y devuelva su factorial.

"""def factorial():
    num = int(input('Ingresa tu numero entero y positivo: '))
    if num > 0:                 #es num mayor a 0
        factorial = 1            #variable factorial
        for i in range(1, num + 1):    #recorre en el rango de 1 a num+1
            factorial *= i          #multiplicacion 
        print(factorial) #muestra el resultado
    else:    #sino
        print('El numero es negativo y no podemos proceder')

factorial()"""


def factorial():
    from math import factorial
    num = int(input('Ingresa tu num positivo y entero: '))
    if num > 0:
        print(factorial(num))
    else: 
        print('No')

factorial()
