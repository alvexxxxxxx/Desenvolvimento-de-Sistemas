class Veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def calcular_imposto(self):
        return self.preco * 0.10


class Carro(Veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca

    def desconto(self):
        return self.preco * 0.05



class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada

    def calcular_imposto(self):
        return self.preco * 0.05


carro1 = Carro("Civic", 2022, 120000.00, "Honda")
moto1 = Moto("CB 500", 2021, 45000.00, 500)


print("=== CARRO ===")
print("Modelo:", carro1.modelo)
print("Marca:", carro1.marca)
print("Imposto:", carro1.calcular_imposto())
print("Desconto:", carro1.desconto())

print("\n=== MOTO ===")
print("Modelo:", moto1.modelo)
print("Cilindrada:", moto1.cilindrada)
print("Imposto:", moto1.calcular_imposto())
