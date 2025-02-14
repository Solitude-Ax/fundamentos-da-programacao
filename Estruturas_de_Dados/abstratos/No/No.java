package  Complexo.No;

public class No {
    
    int data;
    No next;

    No(Integer data, No next) {
        this.data = data;
        this.next = next;
    };

    No(Integer data) {

        this.data = data;
        this.next = null;

    };

    public static void main(String[] args) {

        No no = new No(3);
        No no_2 = new No(27);

        no.next = no_2;

        System.out.println(no.data);
        System.out.println(no.next.data);

    };

}

//node 1 -> node 2 -> node 3 -> node 4 -> None
// 4           56       25         86  