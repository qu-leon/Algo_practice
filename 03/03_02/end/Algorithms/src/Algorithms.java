import java.util.LinkedList;

public class Algorithms {

    public static void main(String[] args) {

        LinkedList<String> listy = new LinkedList<>();
        listy.add("Sally");
        listy.add("Becky");
        listy.add("Nick");
        listy.add("Jack");
        listy.add("Rachel");

        System.out.println(listy.contains("Becky"));
        System.out.println(listy.size());

        listy.removeFirst();

//        for(String item: listy) {
//            System.out.print(item + "->");
//        }

        listy.forEach(x -> System.out.print(x + "->"));
    }
}
