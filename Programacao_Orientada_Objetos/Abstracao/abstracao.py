# A Abstração é um conceito em que você "abstrai" o código, isto é, deixa ele mais vago sobre o que exatamente
# ele faz, mas em troca, você faz com que seja mais rápido o desenvolvimento e manutenção de um código

# Suponha que temos uma função que cria uma jánela, porém existem diversas coisas que são necessárias no
# processo de criar uma jánela, como nome, processamento, renderização...
#
# Ao invés de colocar todas essas variáveis, métodos e criação de clásses espalhadas pelo código, a gente
# abstrae o código, criando uma função como:
#
# criarJanela(tamanho, nome, ...)
#
# E dentro dessa segunda função, poderiamos abstrair ainda mais as coisas, como por exemplo:
#
# processarTask(task)
# renderizarTela(janelaId)
# converterArquivo(arquivo)
#
# Com isso, a gente poderia ir até cada uma dessas funções e trabalhar nelas individualmente pra consertar
# algum erro no código delas, ao invés de ter que procurar entre diversas linhas de código espaguete


class DispositivoEletronico:
    def __init__(self, tipo):
        self.tipo = tipo

    def ligar(self):
        self._ativar_componentes_internos()
        self._iniciar_processos()
        print(f"{self.tipo} ligado.")

    def desligar(self):
        self._desativar_componentes_internos()
        self._fechar_processos()
        print(f"{self.tipo} desligado.")

    def _ativar_componentes_internos(self):
        print(f"\nAtivando componentes do {self.tipo}")

    def _desativar_componentes_internos(self):
        print(f"\nDesativando componentes do {self.tipo}")

    def _iniciar_processos(self):
        print(f"Iniciando processos do {self.tipo}\n")

    def _fechar_processos(self):
        print(f"Fechando processos do {self.tipo}\n")

class HandHeld(DispositivoEletronico):
    def __init__(self, tipo):
        super().__init__(tipo)
        self.bateria = 100

    def consumir_bateria(self):
        self.bateria -= 1

    def carregar_bateria(self):
        self.bateria = 100

    def tirar_foto(self):
        print("\nTirando foto...")
        print("Foto tirada!\n")

class Celular(HandHeld):
    def __init__(self):
        super().__init__("Celular")

class Tablet(HandHeld):
    def __init__(self):
        super().__init__("Tablet")

class DetectorDeFantasmas(HandHeld):
    def __init__(self):
        super().__init__("Detector de Fantasmas Falsificado")
        self.bb = ['a', 'b', 'c']

    def detectar_fantasmas(self):
        print("Detectando fantasmas...")
        for _ in range(2):
            print("Erro! Erro! Abortar! Abortar!\nErro! Erro! Abortar! Abortar!")
        print("Nenhum fAA-antassss ee-enCOOoontRAAado... (puff)")

    def tirar_foto(self):
        print("Isto não era suposto a tirar fotos...")

if __name__ == "__main__":
    Xiaomi = Celular()
    Xiaomi.ligar()
    Xiaomi.desligar()

    Super_Detector_3000 = DetectorDeFantasmas()
    Super_Detector_3000.ligar()
    Super_Detector_3000.detectar_fantasmas()
    Super_Detector_3000.desligar()

    Galaxy = Tablet()
    Galaxy.ligar()
    Galaxy.tirar_foto()
    Galaxy.tirar_foto()
    Galaxy.Tdesligar()
