
class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud
    
    def saludar(self):
        print(f'{self.nombre} -> Hola!')

class Hechicero(Personaje):
    def __init__(self, nombre, salud, tipo, habilidad):
        self.tipo = tipo
        self.habilidad = habilidad
        super().__init__(nombre, salud)

    def magia(self):
        print(f" {self.nombre} usa su habilidad de super {self.habilidad}")

class Caballero(Personaje):
    def __init__(self, nombre, salud, rango, escudo):
        self.rango = rango
        self.escudo = escudo 
        super().__init__(nombre, salud)

    def defensa(self):
        print(f"{self.nombre} ataca con su escudo de {self.escudo}")   

moonlight_1 = Hechicero("Hilda", 800, "bruja", "Inteligencia")
print(f'moonlight_1 -> {moonlight_1.nombre}, {moonlight_1.salud}, {moonlight_1.tipo}, {moonlight_1.habilidad}')
moonlight_1.saludar()
moonlight_1.magia()

knight_1 = Caballero("Adam", 700, "Caballero Dorado", "Metal")
print(f"knight_1 => {knight_1.nombre}, {knight_1.salud},{knight_1.rango}, {knight_1.escudo}")
knight_1.saludar()
knight_1.defensa()
