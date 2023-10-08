public class Algorithms {

    public static String reverseEachWord(String s) {
        if (s == null || s.isEmpty()) {
            return s;
        }

        StringBuilder result = new StringBuilder();
        String[] arr = s.split(" ");

        for (int i = 0; i < arr.length; i++) {
            result.append(reverse(arr[i]));
            if (i != arr.length - 1) {
                result.append(" ");
            }
        }

        return result.toString();
    }

    public static String reverse(String s) {
        return new StringBuilder(s).reverse().toString();
    }

    public static void main(String[] args) {
        System.out.println(reverseEachWord(null));
        System.out.println(reverseEachWord(""));
        System.out.println(reverseEachWord(" "));
        System.out.println(reverseEachWord("sally is a great worker"));
        System.out.println(reverseEachWord("racer racecar madam"));
        System.out.println(reverseEachWord("what can I do today"));
    }
}
