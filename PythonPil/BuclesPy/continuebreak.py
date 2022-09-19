#sirven para detener una iteracion o saltarnos
#break
for i in range(1,11): 
    print(i) #1-10
    if i == 5: #if si o si para poner el break (si es igual a 5 se para)
        break

#continue
for i in range (1, 11):
    if i == 6: #si es igual a 6 lo saltea
        continue #pasa por alto el num, se omite
    print(i) #se pone despues