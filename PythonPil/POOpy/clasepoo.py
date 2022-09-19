#atributos de clase = global ej:especie ="mamiferos"
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad


    #def hablar(self, sonido):
       # print(sonido)

    

class Perro(Animal): #se puede cambiar por Gato o cualquier animal
    
    
    def __init__(self, nombre, raza, especie, edad): 
#constructor le da determinados parametros a los objetos
#self a mi mismo queremos construir un obj que se va a referenciar a si mismo
#atributos de instancia 
        self.nombre = nombre 
        self.raza = raza 
        super().__init__(especie, edad)   
       #pass #nos permite omitir lo que esta adentro

    #metodos: lo que los obj pueden hacer (acciones)   

    
    def saludar(self):
        print(f'{self.nombre} me dio la pata')

perro_1 = Perro("Rex", "Collie", "Perro", 5) #inicializado el objeto
#print(perro_1.raza)
#print(perro_1.nombre)
#print(perro_1.especie)

print(f'perro_1-> {perro_1.nombre}, {perro_1.raza}, {perro_1.especie}, {perro_1.edad}')
perro_1.saludar()

#print(type(perro_1)) # class main.perro

"""
class Perro:
    def __init__(self):
        self.nombre = ' '
        self.raza = ' '
        
perro_1 = Perro()
perro_1.nombre = 'Firulais'
perro_1.raza = 'Salchicha' 
print(f'perro_1-> {perro_1.nombre}, {perro_1.raza}')
"""


