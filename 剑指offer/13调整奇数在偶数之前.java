
// 调整奇数在偶数之前。
// 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
// 思路：要是不要求『稳定』，原先奇不必在奇之前，那么可以用双指针前后夹或者用前向探索指针。要是要求『稳定』，那么还是牺牲一点空间吧，可以AC的。

public void reOrderArray(int [] array) {
        if (array == null || array.length == 1) return;
        ArrayList <Integer> odd = new ArrayList<>();
        ArrayList <Integer> even = new ArrayList<>();
        for (int x : array) {
            if (x % 2 == 0) even.add(x);
            else odd.add(x);
        }
        for (int x : even) odd.add(x);
        for (int i = 0; i< array.length ;i++) array[i] = odd.get(i);
        return;
    }