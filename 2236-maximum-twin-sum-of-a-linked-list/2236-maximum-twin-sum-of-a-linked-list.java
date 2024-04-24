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
    public int pairSum(ListNode head) {
        var ans = 0;

        // 1. find the center
        var fast = head;
        var prev = head;
        var length = 1;
        while (fast.next.next != null) {
            prev = prev.next;
            fast = fast.next.next;
            length++;
        }
        // 2. reverse the second half
        var curr = prev.next;
        for (int i = 0; i < length - 1; i++) {
            var next = curr.next;
            curr.next = next.next;
            next.next = prev.next;
            prev.next = next;
        }
        // 3. iterate over and calculate the sum
        var left = head;
        var center = prev.next;
        for (int i = 0; i < length; i++) {
            ans = Math.max(ans, left.val + center.val);
            left = left.next;
            center = center.next;
        }

        return ans;
    }
}