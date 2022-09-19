#Escribir un programa que pida un numero al usuario y 
# muestre las tablas de multiplicar de ese numero

numero = int(input('ingresa un numero para saber su tabla: ')) #usuario
i = 0 #iterador
multi = 0 #multiplicacion tabla

while i <= 10: #condicion
    multi = numero * i #numusuario por i
    print('{} * {} = {}'.format(numero, i, multi)) #imprime el valor num por i igual a multi
    i += 1 #aumenta el iterador hasta el  10 asi no es infinito porque quedaria en 0


