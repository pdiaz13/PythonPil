#Escribir una función que calcule el total de una factura 
# tras aplicarle el IVA. La función debe recibir la cantidad 
# sin IVA y el porcentaje de IVA a aplicar, y devolver el 
# total de la factura. Si se invoca la función sin pasarle 
# el porcentaje de IVA, deberá aplicar un 21%.


def total():
    monto = float(input("Ingresa el valor a pagar: ")) #recibe el monto de compra
    iva= int(input("Ingresa el valor del IVA: ")) #recibe el iva

    if iva != 0: #si iva es diferente a 0 
        if iva > 0 : #si iva es mayor a 0
            totalPagar = ((monto * iva) / 100) + monto #el total es el porcentaje de iva mas el monto
            # monto por iva ingresado div 100
            return totalPagar
        else: #si no es mayor a 0 o sea negativo
            return"El monto de IVA es negativo y no podemos avanzar"
    else: #si el usuario ingresa 0
        totalPagar = (monto * 0.21) + monto #21% por defecto
        return totalPagar

print("El total de su monto es: ", total()) #muestra la funcion