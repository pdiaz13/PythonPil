class Jugador:
    def __init__(self, nombre, inteligencia, fuerza, defensa, vida):
        self.nombre = nombre
        self.inteligencia = inteligencia
        self.fuerza = fuerza
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="") 
        print("- Inteligencia:",self.inteligencia)
        print("- Fuerza:",self.fuerza)
        print("- Defensa:",self.defensa)
        print("- Vida:",self.vida)   

    def subir_nivel(self, inteligencia, fuerza, defensa):
         self.inteligencia = self.inteligencia + inteligencia
         self.fuerza = self.fuerza + fuerza
         self.defensa = self.defensa + defensa

    def vivo(self):
        return self.vida > 0
    
    def muerte(self):
        self.vida = 0
        print(self.nombre, "está muerto")

    def daño(self, enemigo): #nuestro personaje y personaje enemigo
        return self.fuerza - enemigo.defensa
        #print(personaje1.daño(enemigo1))

    def atacar(self, enemigo):
        daño = self.daño(enemigo) #guardar en var
        enemigo.vida = enemigo.vida - daño 
        print(self.nombre, "hizo", daño, "puntos de daño a", enemigo.nombre) #info rel
        if enemigo.vivo(): #agregar if por si el enemigo muere 
            print("La vida de", enemigo.nombre, "es de", enemigo.vida)
        else:
            enemigo.muerte()

class Guerrero(Jugador):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        super().atributos()
        print("·Espada:", self.espada)

    def daño(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa

class Hechicero(Jugador):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("·Libro:", self.libro)

def daño(self, enemigo):
		if self.fuerza > enemigo.defensa:
			return self.fuerza - enemigo.defensa
		else:
			return 0

def combate(jugador_1,jugador_2):
	turno = 0

	if jugador_1.daño(jugador_2) > 0 or jugador_2.daño(jugador_1)>0:
		while jugador_1.vivo() and jugador_2.vivo():
			print('\nTurno', turno)
			print('>>> Acción de', jugador_1.nombre, ':')
			jugador_1.atacar(jugador_2)
			print('>>>Acción de',jugador_2.nombre,':')
			jugador_2.atacar(jugador_1)
			turno = turno + 1

		if jugador_1.vivo():
			print("\nHa ganado",jugador_1.nombre)
		elif jugador_2.vivo():
			print('\nHa ganado', jugador_2.nombre)
		else:
			print('\nEmpate')

	else:
		print('\nEmpate, ningun jugador inflinge daño al oponente.')


personaje_1 = Guerrero("Jim", 12, 9, 4, 100, 4)
personaje_2 = Hechicero("Pam", 15, 9, 4, 100, 5)
###############################################
personaje_1.atributos()
personaje_2.atributos()      

combate(personaje_1, personaje_2)