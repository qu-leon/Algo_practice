import java.util.Arrays;

public class Algorithms {

    public static void rotateArrayLeft(int[] arr) {
        int temp = arr[0];
        for (int i = 0; i < arr.length - 1; i++) {
            // [2, 3, 4, 5, 6, 6]
            arr[i] = arr[i+1];
        }
        arr[arr.length - 1] = temp;
    }

    public static void rotateArrayRight(int[] arr) {
        int temp = arr[arr.length - 1];
        for (int i = arr.length - 1; i > 0; i--) {
            // [ 1, 1, 2, 3, 4, 5]
            arr[i] = arr[i - 1];
        }
        arr[0] = temp;
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5, 6 };
        rotateArrayLeft(arr);
        rotateArrayRight(arr);
        Arrays.stream(arr).forEach(System.out::println);
    }
}
