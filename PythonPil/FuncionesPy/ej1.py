#Crear un programa que tenga una lista, luego crear una 
# funcion con la cual se van a pedir numeros al usuario 
# para agregar a la lista. Debes crear una segunda funcion 
# en donde se ordenen los numeros pares e impares dentro de 
# dos listas nuevas

lista = [] #lista
num = 0 #numero

def pedir():
    i = 0 #crreo el contador 
    while i <= 5: #mientras i sea menorigual a 5
        num = float(input('Ingresa un numero: '))
        lista.append(num) #agrega dato a lista
        i += 1

#pedir()
#print(lista)

def ordenar(): 
    lista.sort()#ordenar lista
    pares = [] #listas
    impares = []
    for i in lista: #recorre lista con i
        if i % 2 == 0: #si i es modulo 0
            pares.append(i) #agregalo aca
        else: 
            impares.append(i) #sino aca
        print(pares)
        print(impares)

pedir()
ordenar()