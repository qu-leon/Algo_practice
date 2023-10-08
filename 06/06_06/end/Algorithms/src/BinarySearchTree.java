public class BinarySearchTree {
    Node root;

    public void insert(int value) {
        insert(root, value);
    }

    private Node insert(Node root, int value) {
        if (root == null) {
            root = new Node();
            root.data = value;
        } else if (value < root.data) {
            // insert on left
            root.left = insert(root.left, value);
        } else if (value > root.data) {
            root.right = insert(root.right, value);
        }

        return root;
    }

    public boolean contains(int value) {
        return contains(this.root, value);
    }

    private boolean contains(Node root, int value) {
        if (root == null) {
            return false;
        }

        if (value < root.data) {
            return contains(root.left, value);
        }

        if (value > root.data) {
            return contains(root.right, value);
        }

        return true;
    }
}
