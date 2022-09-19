"""Crear un programa que pida al usuario una 
letra, y si es vocal, muestre el mensaje "Es vocal". 
Sino, decirle al usuario que no es vocal"""

letra = input("Ingresa una letra: ")

if letra.lower() in "aeiuo":
    print("es una vocal")
else:
    print("NO es vocal")
