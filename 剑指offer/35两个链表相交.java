
// 输入两个链表，找出它们的第一个公共结点。
// 思路：两个指针一起走，走到头了切换到另一个链表去。直道相遇。注意需要在末尾处判断空，不要过早判断空。


class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}

class Solution {
    public ListNode FindFirstCommonNode(ListNode pHead1, ListNode pHead2) {
        if (pHead1 == null || pHead2 == null) return null;
        ListNode p = pHead1,q = pHead2;
        while (p != q){
            p = (p == null) ? pHead2 : p.next;
            q = (q == null) ? pHead1 : q.next;
        }
        return p;
    }
}