#### 插入排序InsertionSort

1.**插入排序**：假设前面都已经排好序，新元素向前扫描，该交换就交换，不能交换了说明已经好了（类似抓扑克牌）。

假设数据本身大部分有序，那么可以达到O(N)。若大量无序，仍然需要平方级O(N2)。

2.python实现1（原地交换）：

```python
def insertion_sort(alist):
    for j in range(1, len(alist)):
        for i in range(j,0,-1):
            if alist[i] < alist[i-1]:
                alist[i-1], alist[i] = alist[i],alist[i-1]
            else:
                break
```

- 假设了alist是mutable的array。原地双指针，一个记录当前位置，一个逐步逆向探索并交换。
- 这样做的一个坏处就是有可能需要进行多个交换，下一个实现将对这个缺陷进行改进。
- 插入每次只能将数据移动一位，改进有希尔排序跨数据插入，见下文。

3.python实现2（非原地）：

```python
def insertion_sort(alist):
    alist = list(alist)
    for j in range(1, len(alist)):
        i = j-1
        while i >= 0 and alist[i] > alist[j]:
            i -= 1
        alist.insert(i+1,alist.pop(j)) # 就算到达左侧端点，也可以以0索引插入
    return tuple(alist)
```

- 只定位到特殊位置进行插入。
- 不会对全局（外部数据）产生影响，为什么这点是重要的，因为这个数据未必一个线程独占，可能有其他写线程在同时操作这个数据。
- 注意比最左端还小时该如何插入。

4.**希尔排序**（shellsort，也叫**缩小增量排序**）：是改进的**插入排序**，实质是分组插入，复杂度介于O(nlogn)与O(N2)，每次比较相隔较远（gap）位置的数据，不断缩小gap至1（至少要保证一个1的gap的存在，最后一步调用几乎线性的全局插入排序），使得数据逐步有序。（同时消除多个元素的交换）

5.python实现3（原地）：

```python
def shell_sort(alist):
    length = len(alist)
    gap = 1
    while gap < length // 3:
        gap = 3 * gap + 1  # 1,4,13,40,...
    while gap >= 1:
        for i in range(gap,length):
            j = i
            while j >= gap and alist[j] < alist[j-gap]:  # 注意这里需要大于等于，需要达到边缘
                alist[j],alist[j-gap] = alist[j-gap],alist[j]
                j -= gap
        gap = gap // 3  # 注意python2和python3中除法的区别
```

- 注意除法，注意取数据到达边缘，注意一定要取到gap=1的时候（出口条件）。
- 这个实现有个缺陷，就是gap只能以3的倍数的模式来取，在下一个实现中把gap的设置单独解耦出来，更自由一些。

6.python实现4（非原地）：

```python
def shell_sort(arr):
    def gap_gen(size):
        # gap生成器，生成一堆gap
        while size > 1:
            size //= 2
            yield size

    def insertion_sort_reverse(nums):
        nums = nums[:]  # 深拷贝
        N = len(nums)
        for i in range(1, N):
            for j in range(N-1, 0, -1):
                if nums[j] > nums[j - 1]:  # 反向的插入排序
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
        return nums

    for gap in gap_gen(len(arr)):
        arr[::-gap] = insertion_sort_reverse(arr[::-gap])
    return arr
```

- 不管是gap生成器还是排序器都是可插拔的。
- 需要保证一个gap是1，最后一遍全局的排序。