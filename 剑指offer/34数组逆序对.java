// 求逆序对
// 归并排序，从后而往前归并。
// 若前面的tail1值大于后面的tail2值，那么需要交换tail2-mid个（即）。每次选取剩下值中最大的一个存入临时空间，最后从临时空间拷贝回原地。
// 方案一，使用递归回传。
// 方案二，悬挂全局变量，使用统一的计数入口。好处，如果数据非常大，可以设置锁来锁住计数器进行预览。


class Solution {
    private int [] array = null; // 把数据悬挂在全局，让merge功能专注于merge
    private int [] copy = null;  // 用于临时记录merge完后的值,且可以复用
    public int InversePairs(int [] array) {
        if (array == null || array.length == 0 || array.length == 1) return 0;
        this.array = array;
        this.copy = new int [array.length];
        return merge(0,array.length-1);
    }
    public int merge(int start, int end){
        if (start >= end ) return 0;
        int mid = start + (end-start) /2 ; // in case of overflow%1000000007
        int value  = merge(start,mid)%1000000007 + merge(mid+1,end)%1000000007;
        int tail1 = mid, tail2 = end;
        int tail_copy = end;
        while (tail1 >= start && tail2 >= mid+1){
            if (array[tail1] > array[tail2]) {copy[tail_copy--] =array[tail1--]; value = ((tail2 - mid)%1000000007+value)%1000000007;}
            else {copy[tail_copy--] = array[tail2--];}
        } //需要交换的部分进行拷贝，从后完全merge。
        // 清理末尾，要么进入下第一个while要么下第二个while。
        while (tail1 >= start) { copy[tail_copy--] = array[tail1--];}
        while (tail2 >= mid+1) { copy[tail_copy--] = array[tail2--];}
        for (int i = start; i <= end;i++) {array[i] = copy[i];}
        return value;
    }
}

class Solution {  
    private int [] array = null;  // 把数据悬挂在全局，让merge功能专注于merge
    private int [] copy = null;  // 用于临时记录merge完后的值,且可以复用
    private int count =0 ;
    public int InversePairs(int [] array) {
        if (array == null || array.length == 0 || array.length == 1) return 0;
        this.array = array;
        this.copy = new int [array.length];
        merge(0,array.length-1);
        return this.count;
    }
    public void merge(int start, int end){
        if (start >= end ) return;
        int mid = start + (end-start) /2 ; // in case of overflow
        merge(start,mid);
        merge(mid+1,end);
        int tail1 = mid, tail2 = end;
        int tail_copy = end;
        while (tail1 >= start && tail2 >= mid+1){
            if (array[tail1] > array[tail2]) {copy[tail_copy--] =array[tail1--];
            count = ((tail2 - mid)%1000000007+count)%1000000007;} // 产生计数
            else {copy[tail_copy--] = array[tail2--];}
        } //需要交换的部分进行拷贝，从后完全merge。
        // 清理末尾，要么进入下第一个while要么下第二个while。
        while (tail1 >= start) { copy[tail_copy--] = array[tail1--];}
        while (tail2 >= mid+1) { copy[tail_copy--] = array[tail2--];}
        for (int i = start; i <= end;i++) {array[i] = copy[i];}
    }
}

