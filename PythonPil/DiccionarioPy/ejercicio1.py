'''En el siguiente diccionario se encuentran capitales de los paises en el mundo, 
debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, 
en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese 
pais no se encuentra.

{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras",
"Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", 
"Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

'''

paises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Tegucigalpa",
"Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", 
"Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

#pais = input("Ingrese un pais para conocer su capital: ") #pido clave

#letra = pais.capitalize() in diccionario #primera letra en mayus
#in pais capitalize esta en diccionario?
'''
if letra: # se sobreentiende que es true
    print(diccionario[pais.capitalize()]) #si es t devuelve la capital
else: 
    print('El pais no se encuentra en el diccionario')'''

#if pais.capitalize() in diccionario: ||sin hacer la variable letra
#print(diccionario[pais.capitalize()])
#else:
#print('El pais no se encuentra en el diccionario')

pais = input("Ingresa el nombre de un pais para saber su capital:")
pais = pais.title() 
 
if pais in paises:
    print("La capital de {} es:".format(pais),paises[pais]) #paises[pais para que coincida con el pais ingresado]
else:
    print("{} no se encuentra en la lista".format(pais))
 