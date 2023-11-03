from biblioteca import vaca

g1 = vaca("Tonhão meia bomba", "cor")
g1.emitir_som()
g1.comer()

#---------------------------------------

class animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} foi comer...")

    def emitir_som(self):
        print(f"O {self.nome} esta emitindo som...")
#subclasse
class gato(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class vaca(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class boi(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class cachorro(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class galinha(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class masqueico(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
