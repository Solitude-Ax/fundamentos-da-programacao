package Encapsulamento;

public class Encapsulamento {

    public static void main(String[] args) {

        ContaBancaria Zezinho = new ContaBancaria("Zézinho", 0);

        Zezinho.depositar(435);
        Zezinho.sacar(138);
        Zezinho.investir(10);
        Zezinho.mostrar_saldo();
        Zezinho.investir(0);

    }
}

class ContaBancaria {

    private String nome;
    private final int id;
    private int dinheiro;
    private int investimentos;

    ContaBancaria(String nome, int id) {

        this.nome = nome;
        this.id = id;
    }

    void depositar(int deposito) {

        if (deposito > 0) {
            this.dinheiro += deposito;
            System.out.println("Saldo pós deposito: " + deposito);
            return;
        }
        System.out.println("Valor insuficiente para depósito");

        return;
    }

    void sacar(int saque) {

        if (this.dinheiro >= saque) {
            this.dinheiro -= saque;
            System.out.println("Saldo pós saque: " + this.dinheiro);
            return;
        }

        System.out.println("Sem saldo o bastante");
        return;
    }

    void investir(int investimento_comprados) {

        int preco = investimento_comprados * 15;

        if (this.dinheiro >= preco) {
            this.dinheiro -= preco;
            this.investimentos += investimento_comprados;
            System.out.println("Investimentos: " + this.investimentos + "\nSaldo pós investimento: " + this.dinheiro);
            return;
        }

        System.out.println("Sem dinheiro o bastante");
        return;
    }

    void mostrar_saldo() {
        System.err.println("saldo: " + this.dinheiro);
    }

}

