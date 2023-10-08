import java.util.Arrays;

public class Algorithms {

    public static int[] findEvenNums(int[] arr1, int[] arr2) {
        return arr1;
    }


    public static void main(String[] args) {
        int[] arr1 = { -9, 3, 2, -8, 12, -16 };
        int[] arr2 = { 0, -3, -8, -35, 40, 20, 7 };

        Arrays.stream(findEvenNums(arr1, arr2))
                .forEach(System.out::println);
    }
}
