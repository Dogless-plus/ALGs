
// 有序链表归并。

// 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
// 思路：同归并排序，注意边界条件，末尾处注意。trick，设置一个头。

/*
public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}*/
public class Solution {
    public ListNode Merge(ListNode list1,ListNode list2) {
        if (list1 == null) return list2;
        if (list2 == null) return list1;
        ListNode prehead = new ListNode(-1);
        ListNode p = prehead;
        while (list1 != null && list2 !=null){
            if (list1.val < list2.val) {
                p.next = list1 ; list1 = list1.next ; p = p.next;
            }
            else {
                p.next = list2 ; list2 = list2.next ; p = p.next;
            }
        }
        p.next = (list1 == null) ? list2 : list1;
        return prehead.next;
    }
}