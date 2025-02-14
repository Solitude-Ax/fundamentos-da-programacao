import  java.util.Arrays;

public class Array {

    public static void main(String[] args) {

        int[] array = {1, 4, 88, 53, 5, 7, 9};

        System.out.println(Arrays.toString(array));

        System.out.println(array.length);
        System.out.println(array[3]);

        array[6] = 22;

        System.out.println(array);

    }

}