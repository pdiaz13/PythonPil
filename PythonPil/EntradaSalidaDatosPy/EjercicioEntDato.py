from math import sqrt #funcion de raiz cuadrada
print(sqrt(100)) #10.0

a = int(input('Ingresa el valor de A: '))
b = int(input('Ingresa el valor de B: '))
c = int(input('Ingresa el valor de C: '))

x1 = 0
x2 = 0

if((b**2)-(4*a*c)) < 0:
    print('No se puede realizar porque no se puede sacar raiz a un numero negativo')
else:
    x1 = (-b + sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = (-b - sqrt((b**2)-(4*a*c)))/(2*a)
    print('La solucion es: \nx1=',x1, '\nx2=',x2)