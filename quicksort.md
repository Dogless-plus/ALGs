快速排序QuickSort

1.快速排序：通过一趟排序将要排序的数据分割为独立的两个部分，其中一部分比哨兵大，一部分比哨兵小，每部分递归的进行。

2.缺点：

- **输入敏感**：若数据**无序，能达到O(NlogN)**的复杂度（归并和堆排都能达到这个）。若数据基本有序或者大量重复值，性能降低为平方级O(N2)，原因是partition偏向一边去了。所以输入请一般先随机shuffle一下。
- **快排不稳定。（至少书上是这么说的，具体还得看实现）**

3.快排优点：

- 使用广泛，容易实现，时间复杂度小
- 可以不需要额外空间（而堆排和归并需要）in-place
- 可提升：片段小时可以用插排改进，可以设置双哨兵，三路快排（3-way quicksort）。而堆排没有这些改进。
- 对分块（partition）**可并行**。

4.python实现1（单边扫描）:

```python
def quick_sort(alist):
    if len(alist) <= 1:
        return alist
    dog = alist[0]
    left, right = [], []
    [left.append(v) if v <= dog else right.append(v) for v in alist[1:]]
    return quick_sort(left) + [dog, ] + quick_sort(right)
```

- 需要额外临时空间
- 递归比循环效率低
- 扫描不如双边快
- 对于重复值不够友好

5.python实现2（双边扫描递归版）：

```python
# 哨兵位置用于交换，右扫置左，左扫置右
def quick_sort(alist,left,right):  # 传入数据列表，左右范围
    if left >= right: return alist  # 跳出条件
    dog = alist[left]  # 既是哨兵。也通过记录历史，空出了dog的位置用于交换。
    low,high = left, right  # 对入口范围进行记录
    while left < right:
        while left < right and alist[right] >= dog:
            right -= 1  
        alist[left] = alist[right]  # 确保右边大，第一次dog位置可用于存储
        while left < right and alist[left] <= dog:
            left += 1  # 接下来右边多余的位置可用于存储 
        alist[right] = alist[left]
    alist[left] = dog   # 此时left == right，放回哨兵
    quick_sort(alist,low,left-1)  # 递归
    quick_sort(alist,left+1,high)
    return alist
```

- 技巧在于哨兵的位置可以用于交换，而之前交换完的空位又可以用于交换。最后扫描到不能扫描。
- 注意仍然是递归的，是原地的，可能是有害的。

6.python实现3（双边扫描非递归版）：

```python
def quick_sort(alist):
    alist = list(alist)
    to_scan_pairs = [(0,len(alist)-1),]
    while to_scan_pairs:
        left, right = to_scan_pairs.pop(0)
        if left >= right: continue
        dog = alist[left]  # 既是哨兵。也通过记录历史，空出了dog的位置用于交换。
        low,high = left, right  # 对入口范围进行记录
        while left < right:
            while left < right and alist[right] >= dog:
                right -= 1
            alist[left] = alist[right]  # 确保右边大，第一次dog位置可用于存储
            while left < right and alist[left] <= dog:
                left += 1  # 接下来右边多余的位置可用于存储
            alist[right] = alist[left]
        alist[left] = dog   # 此时left == right，放回哨兵
        to_scan_pairs.append((low,left-1))
        to_scan_pairs.append((left+1,high))
    return alist
```

- 只需要将待扫描情况压入队列即可实现循环版的双边扫描快排。
- 支持了迭代器输入，非原地修改。

7.**三路快排**3-way QuickSort（jdk采用过三分区的三路快排，也采用过五分区的双基准快排）

针对的问题：**重复数据多**，若采用双边扫描很容易O(N2),何不增加一个分区用来解决这个问题，当然也可以考虑归并排序。

```python
def quick_sort(alist, left, right):
    if left >= right: return alist
    dog = alist[left]  # 取出哨兵
    lt, gt, i = left, right, left
    while i <= gt:  # 用一个指针向右扫描,直到到达右侧边界
        if alist[i] > dog:  # 若应该处于右侧，那么换到右边，并且将右边边界左移
            alist[i], alist[gt] = alist[gt], alist[i]
            gt -= 1
        elif alist[i] < dog:  # 若应该处于左侧，那么换到左边，并且将左边边界前推，且这个指针前推
            alist[i], alist[lt] = alist[lt], alist[i]
            lt += 1
            i += 1
        else:
            i += 1  # 若相等，那么前推
    quick_sort(alist, left, lt)  # 左半边都是比哨兵小的
    quick_sort(alist, gt+1, right) # 右半边都是比哨兵大的，注意这里是gt+1
    return alist
```

- 注意是原地的，递归的，改进可以参考上一种实现。

8.**双基准排序**，使用两个哨兵，理论上比单个哨兵要快一些（为什么这么说，实现更复杂了，那么效率还更低那是说不过去的）。实现可参考网上或者jdk源码，我暂时不做研究。

9.快排注意事项：

- 内存占用问题
- 考虑边界
- 混乱度输入敏感
- 注意循环结束条件
- 注意稳定性问题