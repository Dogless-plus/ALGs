// 滑动窗口最大值
// 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
// 思路：每次记住上次最大值的位置，没过位置只需要比较当前末尾值，过了位置需要重新线性扫描。


public ArrayList<Integer> maxInWindows(int [] num, int size)
    {
        if (num == null || size <=0 || size > num.length) return new ArrayList<>();
        int N = num.length;
        ArrayList <Integer> ret = new ArrayList<>(N - size +1);
        int max = num[0], idx_max =0 ;
        for (int k = 0 ; k < size; k++) if (num[k] >= max) { idx_max =k ; max=num[k];}
        ret.add(max);
        System.out.println(max);
        for (int i = 1; i + size <= N ; i++) {
            int j = i + size -1;
            if (i <= idx_max && num[j] < max) { ret.add(max);}
            else if (num[j] >= max) {max = num[j] ;idx_max=j;  ret.add(max);}
            else { max = num[i]; // 重新线性搜索最大值极其位置
                for (int k = i ; k <= j; k++) if (num[k] >= max) {idx_max =k ; max=num[k];}ret.add(max);}
        }
        return ret;
    }