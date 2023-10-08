public class Algorithms {

    public static int findMaximum(int a, int b, int c) {
        if (a > b) {
            if (a > c || a == c) {
                return a;
            }
        }

        if (b > c) {
            return b;
        }

        return c;
    }

    public static int findMaximum2(int a, int b, int c) {
        int max = a;

        if (b > max) {
            max = b;
        }

        if (c > max) {
            max = c;
        }

        return max;
    }

    public static void main(String[] args) {

        System.out.println(findMaximum2(1, 2, 3));
        System.out.println(findMaximum2(8, 8, 1));
        System.out.println(findMaximum2(3, 2, 3));
        System.out.println(findMaximum2(1, 1, 9));
        System.out.println(findMaximum2(1, 9, 9));
    }
}
