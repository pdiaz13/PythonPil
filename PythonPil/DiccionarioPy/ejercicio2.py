'''Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un 
número; el programa debe imprimir el jugador al que hace referencia ese número'''

diccionario = { 1 : "Casillas", 15 : "Ramos", 3 : "Pique", 5 : "Puyol", 11 : "Capdevila", 14 : "Xabi Alonso", 16 : "Busquets", 8 : "Xavi Hernandez", 18 : "Pedrito", 6 : "Iniesta", 7 : "Villa"}

opcion = int(input('Ingrese numero de jugador: '))

if opcion in diccionario : #si opcion esta en diccionario
    print(diccionario[opcion]) #la opcion ingresada del diccionario
else: 
    print('El jugador no se encuentra')