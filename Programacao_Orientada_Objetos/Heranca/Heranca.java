package Heranca;
public class Heranca {
    public static void main(String[] args) {
        System.out.println("bananas");

        /*Veiculo_Automotor Carro = new Veiculo_Automotor("Carro", 4, 1400, 4);


        Carro.status_veiculo();
        Carro.alternar_motor();
        Carro.status_veiculo();*/

        Carro Lamborghini = new Carro(4, 1800, 4, 450000);
        Lamborghini.alternar_motor();
        Lamborghini.status_veiculo();

        Onibus Volvo = new Onibus(6, 9500, 4, 395000);
        Volvo.status_veiculo();

        Caminhao Kenworth = new Caminhao(4, 10000, 2, 177000);
        Moto Harley_Davidson = new Moto(2, 4600, 0, 49500);

        Harley_Davidson.alternar_motor();
        Kenworth.alternar_motor();
        Kenworth.status_veiculo();

        Harley_Davidson.status_veiculo();
        Harley_Davidson.alternar_motor();
        Harley_Davidson.status_veiculo();
        
    }
};

class Veiculo_Automotor {

    protected static final String CARRO = "Carro";
    protected static final String MOTO = "Moto";
    protected static final String CAMINHAO = "Caminhão";
    protected static final String ONIBUS = "Ônibus";

    final String tipo_de_veiculo;
    final int rodas;
    final int cilindradas;
    final int portas;
    private int preco;
    private boolean motor_ligado = false;

    Veiculo_Automotor(String tipo_de_veiculo, int rodas, int cilindradas, int portas, int preco) {
        
        this.tipo_de_veiculo = tipo_de_veiculo;
        this.rodas = rodas;
        this.cilindradas = cilindradas;
        this.portas = portas;
        this.preco = preco;

    };

    void alternar_motor() {
        motor_ligado = !motor_ligado;
    };

    void status_veiculo() {

        System.out.println("\nStatus do " + this.tipo_de_veiculo + ":");
        System.out.println("------------------- \n");
        System.out.println("Ativação do motor: " + this.motor_ligado);
        System.out.println("Quantidade de cilindradas: " + this.cilindradas + "cc");
        System.out.println("Quantidade de portas (não danificadas): " + this.portas);
        System.out.println("Quantidade de rodas: " + this.rodas);
        System.out.println("Preço do veículo: " + this.preco);
    };

};

class Carro extends Veiculo_Automotor {

    Carro(int rodas, int cilindradas, int portas, int preco) {
        super(CARRO, rodas, cilindradas, portas, preco);
    }

}

class Moto extends Veiculo_Automotor {

    Moto(int rodas, int cilindradas, int portas, int preco) {
        super(MOTO, rodas, cilindradas, portas, preco);
    }
}

class Onibus extends Veiculo_Automotor {

    Onibus(int rodas, int cilindradas, int portas, int preco) {
        super(ONIBUS, rodas, cilindradas, portas, preco);
    }
    
}

class Caminhao extends Veiculo_Automotor {

    Caminhao(int rodas, int cilindradas, int portas, int preco) {
        super(CAMINHAO, rodas, cilindradas, portas, preco);
    }
}