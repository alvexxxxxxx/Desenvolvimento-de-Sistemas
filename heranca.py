class Animal():
    def __init__(self, nome, cor ):
        self.__nome = nome
        self.__cor = cor

    def comer(self):
        print(f"o {self.__nome} esta comendo")

class Gato(Animal):
    def __init__(self, nome, cor ):
        super().__init__(nome, cor)

class Cachorro(Animal):
    def __init__(self, nome, cor ):
        super().__init__(nome, cor)

class Coelho(Animal):
    def __init__(self, nome, cor ):
        super().__init__(nome, cor)




lugano = Gato("Siamês", "preto")

lugano.comer()

bat = Gato("persian", "amarelo")

bat.comer()

thor = Cachorro("viralata", "caramelo")

thor.comer()

lucky = Cachorro("husky", "branco")

lucky.comer()

pipoca = Coelho("lion head", "amarelo")

pipoca.comer()

flocos = Coelho("Mini rex", "flocos")

flocos.comer()