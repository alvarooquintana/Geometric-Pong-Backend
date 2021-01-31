class Animal:
    name = None

    def morir(self):
        print(f"{self.name} ha muerto")

    def nacer(self):
        print(f"{self.name} ha nacido")



class Perro(Animal):

    def __init__(self, name):
        self.name = name

    def guau(self):
        print(f"{self.name} esta diciendo guau")

    def defecar(self, color):
        print(f"{self.name} ha defecado de color {color}")






perro = Perro("tronco")
perro.nacer()
perro.guau()
perro.defecar("verde")
perro.morir()
