/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode sentLeft = new ListNode(-1, head);
        if (right == 1)
            return head;
        ListNode prevLeft = sentLeft;
        ListNode nextRight = null;
        ListNode slow = head;
        ListNode fast = null;

        var curr = head;
        for (int i = 1; i < right; i++) {
            if (i + 1 == left) {
                prevLeft = curr;
                slow = curr.next;
            }
            curr = curr.next;
        }
        fast = curr;
        nextRight = fast.next;

        // reversing
        curr = slow;
        fast.next = null; // cut out the sublist
        ListNode prev = null;
        while (curr != null) {
            var next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        prevLeft.next = prev;
        slow.next = nextRight;
        return sentLeft.next;
    }
}