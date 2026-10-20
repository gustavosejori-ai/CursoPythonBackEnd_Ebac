class Animal:
    def __init__(self,nome,idade):
        self.nome = str(nome)
        self.idade = int(idade)
    def emitir_som(self):
        print("O animal emitiu um som generico.")


class Cachorro(Animal):
    def emitir_som(self):
        print("O cachorro latiu!")

class Gato(Animal):
    def emitir_som(self):
        print("O gato miou!")


meu_gato = Gato("Thomas",10)
meu_cachorro = Cachorro("Betove", 16)

meu_cachorro.emitir_som()
meu_gato.emitir_som()