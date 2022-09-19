#no se la cant de valores se le va a poner a la funcion o datos que se van a ingresar a la misma

def argumento(*num): #* se almacena en una tupla
    for i in num:
        print(i)

print(argumento(10, 20, 30, 40, 50)) #se asigna el valor 
#todos los datos se guardan en una tupla
