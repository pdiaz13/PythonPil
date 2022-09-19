"""def <nombre func> ():
    <sentencia>
    return #retorno: es un valor que envia la funcion
"""

def entero():
    print('Este es un dato entero: ')
    return 10

def decimal():
    print('Este es un dato decimal:')
    return 90.99

def frase():
    return "Mi nombre es Pri"

def asignacion():
    return 1, 2, 3, 4, 5

print(entero())
print(decimal())
print(frase())

a, b, c, d, e = asignacion()
print(a) #1
print(b) #2 

#Este es un dato entero: 
#10
#Este es un dato decimal:
#90.99
# 
# #variable, variable = 10, 26 crear variables