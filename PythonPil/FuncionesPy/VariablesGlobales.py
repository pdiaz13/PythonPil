def valores():
    global num1
    global num2
    num1 = 110
    num2 = 40
    resultado = num1 + num2
    return resultado

print(valores()) #150
print(valores())
print(valores())

#funcion estatica

resta = num1 - num2  
print(resta)        #70

#englobar una variable por fuera y por dentro