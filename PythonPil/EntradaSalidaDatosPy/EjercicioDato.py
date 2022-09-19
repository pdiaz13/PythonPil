practica1 = float(input('Ingrese el valor de la practica 1: '))
practica2 = float(input('Ingrese el valor de la practica 2: '))
practica3 = float(input('Ingrese el valor de la practica 3: '))
ExamenParcial = float(input('Ingrese el valor del examen parcial: '))
ExamenFinal = float(input('Ingrese el valor del examen final: '))

PromedioPractica = (practica1 + practica2 + practica3)/3
PromedioFinal = (PromedioPractica + 2*ExamenParcial + 3*ExamenFinal)/6

print('El promedio final del estudiante es de:\n ',PromedioPractica, '\n Y el promedio final es de:\n',PromedioFinal)