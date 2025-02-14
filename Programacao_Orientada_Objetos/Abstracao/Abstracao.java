package Abstracao;
public class Abstracao {

    public static void main (String[] args) {
    
        Celular Xiaomi = new Celular();
    
        Xiaomi.ligar();
        Xiaomi.desligar();

        Detector_de_Fantasmas Super_Detector_3000 = new Detector_de_Fantasmas();

        Super_Detector_3000.ligar();
        Super_Detector_3000.detectar_fantasmas();
        Super_Detector_3000.desligar();

        Tablet TabletName = new Tablet();

        TabletName.ligar();
        TabletName.tirar_foto();
        TabletName.tirar_foto();
        TabletName.desligar();

    }
    }

abstract class Dispositivo_Eletronico {

    final String tipo;

    Dispositivo_Eletronico(String tipo) {
        this.tipo = tipo;
    };

    void ligar() {
        this.ativar_componentes_inernos();
        this.iniciar_processos();
        System.out.println(this.tipo + " ligado.");
    };

    void desligar() {
        this.desativar_componentes_inernos();
        this.fechar_processos();
        System.out.println(this.tipo + " desligado.");
    };

    private void ativar_componentes_inernos() {
        System.out.println("\nAtivando componentes do " + this.tipo);
    };

    private void desativar_componentes_inernos() {
        System.out.println("\nDesativando componentes do " + this.tipo);
    };

    private void iniciar_processos() {
        System.out.println("Iniciando processos do " + this.tipo + "\n");
    };

    private void fechar_processos() {
        System.out.println("Fechando processos do " + this.tipo + "\n");
    };
        
}

class Hand_Held extends Dispositivo_Eletronico {

    protected int bateria;
    
    Hand_Held(String tipo) {
        super(tipo);
        this.bateria = 100;
    }

    void consumir_bateria() {
        this.bateria -= 1;
    };

    void carregar_bateria() {
        this.bateria = 100;
    };

    void tirar_foto() {
        System.out.println("\nTirando foto...");
        System.out.println("Foto tirada!\n");
    }
}

class Celular extends Hand_Held {

    Celular() {
        super("Celular");
    }

}

class Tablet extends Hand_Held {

    Tablet() {
        super("Tablet");
    }
}

class Detector_de_Fantasmas extends Hand_Held {

    Detector_de_Fantasmas() {
        super("Detector de Fantasmas Falsificado");
    }

    void detectar_fantasmas() {
        System.out.println("Detectando fantasmas...");
        
        for (int x=0; x < 2; x++) {
        System.out.println("Erro! Erro! Abortar! Abortar!\nErro! Erro! Abortar! Abortar!");
        }
        System.out.println("Nenhum fAA-antassss ee-enCOOoontRAAado... (puff)");
    }

    @Override
    void tirar_foto() {
        System.out.println("Isto não era suposto a tirar fotos...");
    };
    
}