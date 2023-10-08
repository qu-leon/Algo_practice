public class Algorithms {

    public static boolean isUppercase(String s){
        return s.chars().allMatch(Character::isUpperCase);
    }

    public static boolean isLowercase(String s){
        return s.chars().allMatch(Character::isLowerCase);
    }

    public static void main(String[] args) {
        
        System.out.println(isLowercase("nagg"));
        System.out.println(isUppercase("WHIHCI"));
        System.out.println(isLowercase("SowijfF"));
        System.out.println(isUppercase("FEoowF"));
    }
}
