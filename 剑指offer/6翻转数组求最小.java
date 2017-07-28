// 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 
// 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
// 思路：使用二分查找，可缩小就缩小，否则使用线性搜索。注意不要贸然使用mid+1和mid-1,另外考虑可能根本就没有翻转过呢。

import java.util.ArrayList;
public class Solution {
    public int minNumberInRotateArray(int [] array) {
        if (array == null) return -1;  // undefined
        if (array.length == 1) return array[0];
        if (array[0] < array[array.length-1]) return array[0];
        int start = 0, end = array.length-1, mid;
        while (start < end ){
            mid = start + (end - start) / 2;
            if (array[mid] > array[start]) start = mid;
            else if (array[mid] < array[end]) end = mid;
            else break;
        }
        int min = array[start];
        for ( int i = start ; i <= end ; i++) if (array[i] < min) min = array[i];
        return min;
    }
}