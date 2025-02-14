import java.util.HashMap;

public class Mapa {

    public static void main(String[] args) {

        HashMap<String, Integer> map = new HashMap<>();
        HashMap<Integer, String> papa = new HashMap<>();

        System.out.println(map.toString());

        for (int x = 0; x < 4; x++) {
            map.put(Integer.toString(x), x);
        }

        System.out.println(map.toString());

        System.out.println(map.keySet());

    }

}