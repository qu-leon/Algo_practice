import java.util.Arrays;

public class Algorithms {

    public static int[] reverse(int[] arr) {
        return arr;
    }


    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5, 6 };

        Arrays.stream(reverse(arr))
                .forEach(System.out::println);
    }
}
