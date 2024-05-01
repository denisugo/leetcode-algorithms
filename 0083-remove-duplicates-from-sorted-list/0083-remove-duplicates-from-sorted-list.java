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
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null)
            return null;
        var slow = head;
        var fast = slow.next;

        while (fast != null) {
            if (fast.val == slow.val)
                slow.next = fast.next;
            else
                slow = fast;
            fast = fast.next;
        }

        return head;

    }
}