// 最小的k个数。
// 使用堆，或者用固定大小堆，注意不够长的问题。使用快排partition。使用mr中在map端各取top-k，在reduce总取top-k。

import java.util.ArrayList;
import java.util.PriorityQueue;


public class Solution {
    public ArrayList <Integer> GetLeastNumbers_Solution(int [] input, int k) {
        if (k>input.length) return new ArrayList<Integer>();
        PriorityQueue <Integer> heap = new PriorityQueue<>();
        for (int x: input){
            heap.add(x);
        }
        ArrayList <Integer> ret = new ArrayList<>();
        int N = Math.min(heap.size(),k);
        for (int i = 0; i < N; i++){
            ret.add(heap.poll());
        }
        return ret;
    }
}