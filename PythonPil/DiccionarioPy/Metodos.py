diccionario = {1 : 2, 2 : 3, 3: 4}
diccionario2 = {4: 5, 6: 7}
'''diccionario.pop(3) #elimina clave y valor 3
print(diccionario)
# 1:2 2:3

diccionario.clear() #limpia el diccionario
print(diccionario)
# diccionario vacio {}'''

print(diccionario.get(3)) #recibe un parametro y devuelve valor de la clave

diccionario.setdefault(4, 5)  #recibe el valor de la clave nueva (clave, valor)
print(diccionario) #{1: 2, 2: 3, 3: 4, 4: 5}

diccionario.update(diccionario2) #actualiza
print(diccionario) #{1: 2, 2: 3, 3: 4, 4: 5, 6: 7}

diccionario.copy() #genera una copia
print(diccionario)