// 输入一个链表，从尾到头打印链表每个节点的值。

/**
*    public class ListNode {
*        int val;
*        ListNode next = null;
*
*        ListNode(int val) {
*            this.val = val;
*        }
*    }
*
*/
import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
        ArrayList <Integer> ret = new ArrayList<>();
        if (listNode == null) return ret;
        ListNode node = listNode;
        while (node != null){
            ret.add(node.val);
            node = node.next;
        }
        ArrayList <Integer> ret2 = new ArrayList<>();
        for (int i = ret.size()-1; i>=0;i--)
            ret2.add(ret.get(i));
        ret = null;
        return ret2;
    }
}