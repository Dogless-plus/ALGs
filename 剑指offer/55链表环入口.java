
// 链表环的入口节点
// 一个链表中包含环，请找出该链表的环的入口结点。
// 思路：双指针一快一慢，相遇后将一指针移至开始，匀速相遇处就是入口。
// 注意：要让slow和quick两个指针进入循环，一开始不能设置相等。quick需要前向探索可行。quick到达尾部也要结束。

/*
 public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}
*/
public class Solution {
    public ListNode EntryNodeOfLoop(ListNode pHead)
    {
        if (pHead == null || pHead.next == null || pHead.next.next == null) return null;
        ListNode slow = pHead.next, quick = pHead.next.next;
        while (quick != null && quick.next != null && quick != slow){
            quick = quick.next.next;
            slow = slow.next;
        }
        if (quick == null || quick.next == null) return null;
        slow = pHead;
        while (quick != slow){
            slow = slow.next;
            quick = quick.next;
        }
        return slow;
    }
}