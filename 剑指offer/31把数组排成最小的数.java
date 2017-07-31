

// 把数组排成最小的数。
// 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
// 思路：可以构造compare方法来进行排序，或者自己实现一个简单的冒泡，可以AC。比较方法可以是补等长比较或者根据结合结果比较。


class Solution {
    public String PrintMinNumber(int[] numbers) {
        if (numbers == null || numbers.length == 0) return "";
        String[] nums = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) nums[i] = String.valueOf(numbers[i]);
        if (numbers.length == 1) return nums[0];
        for (int i = 0; i < numbers.length; i++)
            for (int j = 0; j < numbers.length - 1; j++)
                if ((nums[j + 1] + nums[j]).compareTo(nums[j] + nums[j + 1]) < 0) {
                    // String 未重载大于号小于号，但是有compareTo
                    String tmp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = tmp;
                }
        StringBuilder sb = new StringBuilder();
        for (String s : nums) sb.append(s);
        return sb.toString();
    }
}