package Polimorfismo;
public class Polimorfismo {

    public static void main (String[] args) {

        Bandido lil_bandit = new Bandido(25, 7, 7, 28, "Marco");
        Peao lil_peao = new Peao(23, 2, 5, 11, "Aurélio");

        lil_bandit.lutar(lil_peao);
        lil_peao.lutar(lil_bandit);

        lil_bandit.fugir();
        lil_peao.fugir();

    }
}

abstract class NonPlayableCharacter {

    int vida;
    int composicao;
    int forca;
    int inteligencia;
    String nome;

    NonPlayableCharacter(int vida, int composicao,int forca, int inteligencia, String nome) {

        this.vida = vida;
        this.composicao = composicao;
        this.forca = forca;
        this.inteligencia = inteligencia;
        this.nome = nome;

    };

    abstract void lutar(NonPlayableCharacter target);

    abstract void fugir();

    //abstract void conversar(NonPlayableCharacter target);

    abstract void viajar(String place);

};

class Peao extends  NonPlayableCharacter {

    Peao(int vida, int composicao, int forca, int inteligencia, String nome) {
        super(vida, composicao, forca, inteligencia, nome);

    };

    @Override
    void lutar(NonPlayableCharacter target) {
        
        System.out.println(this.nome + " é fraco demais, e covarde demais pra lutar, é melhor fugir \n");
    };

    @Override
    void fugir() {

        System.out.println(this.nome + " fugiu da batalaha, perdendo o resto de qualquer honra que sua familia tinha \n");
    }

    @Override
    void viajar(String place) {

        System.out.println(this.nome + " prepara de forma otimista todos os mantimentos e equipamentos necessários para a viagem \n");
        System.out.println("Sua mochila acaba se rasgando no caminho \n");
        System.out.println(this.nome + " chega com fome a cansado a " + place + " \n");
    }

};

class Bandido extends NonPlayableCharacter {

    Bandido(int vida, int composicao,int forca, int inteligencia, String nome) {
        super(vida, composicao, forca, inteligencia, nome);
    }

    @Override
    void lutar(NonPlayableCharacter target) {
        System.out.println(this.nome + " enfia o dedo no olho de " + target.nome);
        System.out.println(this.nome + " ataca " + target.nome + " com uma adaga \n");
    }

    @Override
    void fugir() {
        System.out.println(this.nome + " aponta para o céu e fala:");
        System.out.println("\"Olha, um dragão!!\"");
        System.out.println(this.nome + " foge da batalha, deixando diversas moedas caírem devido sua corrida desajeitada \n");
    }

    @Override
    void viajar(String place) {
        System.out.println(this.nome + " espera a beira de uma estrada por um bando de aventureiros");
        System.out.println(this.nome + " convence eles a ir até " + place);
        System.out.println(this.nome + " rouba os aventureiros na calada da noite perto do final da viagem\n");
    }
}

