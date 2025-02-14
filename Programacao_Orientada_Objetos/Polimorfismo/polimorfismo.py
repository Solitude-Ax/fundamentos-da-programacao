# Polimorfismo se trata de fazer os métodos que duas subclasses compartilham
# tenham um diferente comportamento dependendo da classe que o chama

# Por exemplo, ambos as classes Peao e Bandido derivam de NPC, e por isso
# tem os mesmos métodos e atributos, porém suas implementações são diferentes
# Isso é extremamente útil para fazer os objetos "interagirem" entre si

class NonPlayableCharacter:

    def __init__(self, vida, composicao, forca, inteligencia, nome):
        self.vida = vida
        self.composicao = composicao
        self.forca = forca
        self.inteligencia = inteligencia
        self.nome = nome

    def lutar(self, target):
        raise NotImplementedError("Esse método não foi implementado por subclasse")

    def fugir(self):
        raise NotImplementedError("Esse método não foi implementado por subclasse")

    def viajar(self, place):
        raise NotImplementedError("Esse método não foi implementado por subclasse")

class Peao(NonPlayableCharacter):

    def lutar(self, target):
        print(f"{self.nome} é fraco demais, e covarde demais pra lutar, é melhor fugir\n")

    def fugir(self):
        print(f"{self.nome} fugiu da batalha, perdendo o resto de qualquer honra que sua familia tinha\n")

    def viajar(self, place):
        print(f"{self.nome} prepara de forma otimista todos os mantimentos e equipamentos necessários para a viagem\n")
        print("Sua mochila acaba se rasgando no caminho\n")
        print(f"{self.nome} chega com fome a cansado a {place}\n")

class Bandido(NonPlayableCharacter):

    def lutar(self, target : NonPlayableCharacter):
        print(f"{self.nome} enfia o dedo no olho de {target.nome}")
        print(f"{self.nome} ataca {target.nome} com uma adaga\n")

    def fugir(self):
        print(f"{self.nome} aponta para o céu e fala:")
        print("\"Olha, um dragão!!\"")
        print(f"{self.nome} foge da batalha, deixando diversas moedas caírem devido sua corrida desajeitada\n")

    def viajar(self, place : str):
        print(f"{self.nome} espera a beira de uma estrada por um bando de aventureiros")
        print(f"{self.nome} convence eles a ir até {place}")
        print(f"{self.nome} rouba os aventureiros na calada da noite perto do final da viagem\n")

if __name__ == "__main__":
    lil_bandit = Bandido(25, 7, 7, 28, "Marco")
    lil_peao = Peao(23, 2, 5, 11, "Aurélio")

    lil_bandit.lutar(lil_peao)
    lil_peao.lutar(lil_bandit)

    lil_bandit.fugir()
    lil_peao.fugir()
