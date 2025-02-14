# Aqui na herança, você pode ver que a gente constrói novas clásses usando uma classe base
# Isso permitiria que a gente desenvolvesse classes e objetos mais complexos e úteis,
# com diferentes métodos e atributos, porém todas derivando de uma mesma base, além de
# poupar a reescrita de código

# Além disso, como você pode ver em Carro, a gente pode ir construindo encima da Classe herdada,
# colocando novos métodos e funções exclusivas a subclasse

class VeiculoAutomotor:

    def __init__(self, tipo_de_veiculo, rodas, cilindradas, portas, preco):
        self.tipo_de_veiculo = tipo_de_veiculo
        self.rodas = rodas
        self.cilindradas = cilindradas
        self.portas = portas
        self.preco = preco
        self.motor_ligado = False

    def alternar_motor(self):
        self.motor_ligado = not self.motor_ligado

    def status_veiculo(self):
        print(f"\nStatus do {self.tipo_de_veiculo}:")
        print("------------------- \n")
        print(f"Ativação do motor: {self.motor_ligado}")
        print(f"Quantidade de cilindradas: {self.cilindradas}cc")
        print(f"Quantidade de portas (não danificadas): {self.portas}")
        print(f"Quantidade de rodas: {self.rodas}")
        print(f"Preço do veículo: {self.preco}")



class Carro(VeiculoAutomotor):
    def __init__(self, rodas, cilindradas, portas, preco):
        super().__init__("Carro", rodas, cilindradas, portas, preco)
        
    def ligar_faróis(self):
        print("ligando faróis")

    def ajustar_cinto_seguranca(self):
        
        print("Cinto ajustado")

class Moto(VeiculoAutomotor):
    def __init__(self, rodas, cilindradas, portas, preco):
        super().__init__("Moto", rodas, cilindradas, portas, preco)
    
    def ajustar_cinto_seguranaca(self):
        print("Esse veículo não tem cinto")


class Onibus(VeiculoAutomotor):
    def __init__(self, rodas, cilindradas, portas, preco):
        super().__init__("Ônibus", rodas, cilindradas, portas, preco)


class Caminhao(VeiculoAutomotor):
    def __init__(self, rodas, cilindradas, portas, preco):
        super().__init__("Caminhão", rodas, cilindradas, portas, preco)


if __name__ == "__main__":
    dic = {"abc": None}
    Lamborghini = Carro(4, 1800, 4, 450000)
    Lamborghini.alternar_motor()
    Lamborghini.status_veiculo()

    Volvo = Onibus(6, 9500, 4, 395000)
    Volvo.status_veiculo()

    Kenworth = Caminhao(4, 10000, 2, 177000)
    Harley_Davidson = Moto(2, 4600, 0, 49500)

    Harley_Davidson.alternar_motor()
    Kenworth.alternar_motor()
    Kenworth.status_veiculo()

    Harley_Davidson.status_veiculo()
    Harley_Davidson.alternar_motor()
    Harley_Davidson.status_veiculo()
    
    Harley_Davidson.ajustar_cinto_seguranaca()
    Lamborghini.ajustar_cinto_seguranaca()