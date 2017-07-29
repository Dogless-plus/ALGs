
// 输入一个链表，输出该链表中倒数第k个结点。
// 思路：前向探索指针。注意不够长，成环陷入死循环等问题。


/*
public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}*/
public class Solution {
    public ListNode FindKthToTail(ListNode head,int k) {
        if (head == null || k <= 0) return null;
        ListNode p= head , q = head;
        for (int i =0 ; i < k; i++) {
            if (p == null) return null;
            else p = p.next;
        }
        int count = 100000;
        while (count > 0) {
            count -- ; // dangerous endless loop
            if (p == null) return q;
            else { p= p.next;
            q = q.next;}
        }
        return new ListNode(-1); // undefined
    }
}