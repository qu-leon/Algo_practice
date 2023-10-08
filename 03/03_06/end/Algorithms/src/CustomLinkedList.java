public class CustomLinkedList {

    Node head;

    public void displayContents() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + "->");
            current = current.next;
        }
        System.out.println();
    }

    public void deleteKthNodeFromEnd(int k) {

        if (head == null || k == 0) {
            return;
        }

        // list = [a, b, c, d]; k = 2
        Node first = head; // a
        Node second = head; // a

        for (int i = 0; i < k; i++) {
            second = second.next;
            if (second.next == null) {
                // K >= length of list
                if (i == k - 1) {
                    head = head.next;
                }
                return;
            }
        }

        // second = c

        while (second.next != null) {
            first = first.next;
            second = second.next;
        }

        // first = b
        // second = d

        first.next = first.next.next;


    }
}
