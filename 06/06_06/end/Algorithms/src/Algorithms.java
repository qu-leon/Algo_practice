public class Algorithms {

    public static void main(String[] args) {
        Node rootNode = new Node();
        rootNode.data = 2;

        BinarySearchTree tree = new BinarySearchTree();
        tree.root = rootNode;

        tree.insert(1);
        tree.insert(3);
        tree.insert(4);

        System.out.println(tree.contains(1));
        System.out.println(tree.contains(2));
        System.out.println(tree.contains(3));
        System.out.println(tree.contains(4));

        System.out.println(tree.contains(5));
        System.out.println(tree.contains(-4));
        System.out.println(tree.contains(0));
        System.out.println(tree.contains(6));
    }
}
