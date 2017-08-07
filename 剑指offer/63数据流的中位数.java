// 数据流的中位数
// 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
// 思路：使用一个大顶堆和一个小顶堆，小顶堆都比大顶堆大。插入时若是奇数插入大顶堆，需要先在小顶堆过滤一遍，若偶则相反。取出时若奇取大顶堆，若偶求大小顶堆平均。


import java.util.PriorityQueue;
import java.util.Comparator;

public class Solution {
	private PriorityQueue <Integer> minheap = new PriorityQueue<>();
    private PriorityQueue <Integer> maxheap = new PriorityQueue<Integer>(10, new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            return o2 - o1;
        }
    });
    private int count = 0;
    public void Insert(Integer num) {
        if (count % 2 ==0 ) {minheap.add(num); maxheap.add(minheap.poll());} 
        else {maxheap.add(num);minheap.add(maxheap.poll());}
        count ++;
    }

    public Double GetMedian() {
        if (count % 2 ==1) return (double)maxheap.peek();
        else return (double) (maxheap.peek() + minheap.peek())/2.0;
    }
}