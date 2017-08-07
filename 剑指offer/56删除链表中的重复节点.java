

// 删除链表中的重复节点
// 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
// 思路：使用双指针。一个前向探索，一个用于记录最后一个有效的位置。


class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}

class Solution {
    public ListNode deleteDuplication(ListNode pHead) {
        if (pHead == null || pHead.next == null) return pHead;
        ListNode prehead = new ListNode(-1); // trick,以防删完没了
        prehead.next = pHead;
        ListNode lastnode = prehead, p = pHead; // 最后一个有效的节点
        while (p != null && p.next != null) {
            if (p.next.val != p.val) { // 需要这个节点
                lastnode = p;
                p = p.next;
            } else {  // 可向前跳跃
                int val = p.val;
                while (p != null && p.val == val) {
                    p = p.next;
                }
                lastnode.next = p;
            }
        }
        return prehead.next;
    }
}