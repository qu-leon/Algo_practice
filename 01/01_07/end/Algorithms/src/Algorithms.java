public class Algorithms {

    public static String reverse(String s) {
        if(s == null || s.isEmpty()) {
            return s;
        }

        StringBuilder reversed = new StringBuilder();
        for (int i = s.length() - 1; i >= 0; i--) {
            reversed.append(s.charAt(i));
        }

        return reversed.toString();
    }

    public static String reverse2(String s) {
        if(s == null || s.isEmpty()) {
            return s;
        }

        StringBuilder sb = new StringBuilder(s);
        return sb.reverse().toString();
    }

    public static void main(String[] args) {
        System.out.println(reverse2(null));
        System.out.println(reverse2(""));
        System.out.println(reverse2("hello"));
        System.out.println(reverse2("tacos"));
        System.out.println(reverse2("Hi!"));
    }
}
