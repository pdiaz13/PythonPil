diccionario = {'Nombre' : 'Priscila', 'Apellido' : 'Diaz', 'Estatura' : 165}

print(diccionario.keys()) #devuelve las claves 
#dict_keys(['Nombre', 'Apellido', 'Estatura'])

print(diccionario.values()) #devuelve valores 
#dict_values(['Priscila', 'Diaz', 165])

print(diccionario['Estatura']) #llama a una clave 
#165

diccionario['Peso'] = '50 kg' #agrega clave y valor nuevos
print(diccionario) #{'Nombre': 'Priscila', 'Apellido': 'Diaz', 'Estatura': 165, 'Peso': '50 kg'}

diccionario['Nombre'] = 'Nahir' #cambia el valor de una clave
print(diccionario) 