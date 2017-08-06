
// 统计一个数字在排序数组中出现的次数。
// 思路：排序数组，提示了二叉查找。先二叉查找，再线性搜索。


public int GetNumberOfK(int [] array , int k) {
        if (array == null || array.length ==0 )return 0;
        if (array.length == 1) return (k == array[0]) ? 1 :0;
        int start = 0, end = array.length-1, count = 0;
        while (start <= end){
            int mid = start + (end- start) / 2;
            if (array[mid] > k ) end = mid -1;
            else if (array[mid] < k) end = mid+1;
            else {
                int tmp = mid;
                while (tmp >= start && k == array[tmp--]) {count++;}
                tmp = mid;
                while (tmp <= end && k == array[tmp++]) {count++;}
                return --count;
            }
        }
        return count;
    }