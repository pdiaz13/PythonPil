palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3:
    print("No riman porque tienen menos de 3 caracteres")
    #recordar op logicos OR 
elif palabra1[-3 : ] == palabra2 [-3 : ]:
    print("Las palabras riman")
    #si las ultimas 3 letras de palabra1 y palabra2 
elif palabra1[-2 : ] == palabra2[-2 : ]:
    print("Las palabras riman un poco")
    #si las ultimas 2 letras de palabra1 y palabra2
else: 
    print("Las palabras no riman")
    #sino se cumple nada de lo anterior

    """Ingresa la primera palabra: tormenta
Ingresa la segunda palabra: lamenta
Las palabras riman"""
