归并排序MergeSort

1.归并排序：两两归并，merge的时候从头比较比较只需O(n)。整体复杂度为O(NlogN)。

注：也可以多路归并，可以可以从尾部开始比较，比如剑指offer上一道题求数组的逆序对。

可以top-down递归，也可以bottom-up循环。

流程：sort(left)、sort(right)、merge(left、right) 

改进：

- 当片段足够小时可以使用其他的排序，比如插入排序。
- 先线性测试是否有序，若有序就不用排了。
- merge时与辅助空间切换着用，少一半拷贝。

2.python实现1（递归top-down）：

```python
def merge_sort(alist):
    alist = list(alist)
    if len(alist) <= 1:
        return alist
    elif len(alist) == 2:
        if alist[0] > alist[1]:
            alist[1], alist[0] = alist[0], alist[1]
        return alist
    mid = len(alist) // 2
    left = merge_sort(alist[:mid + 1])
    right = merge_sort(alist[mid + 1:])
    ret = []
    while len(left) and len(right):
        if left[0] <= right[0]:
            ret.append(left.pop(0))
        else:
            ret.append(right.pop(0))
    ret.extend(left)
    ret.extend(right)
    return ret
```

- 递归的效率比循环低，很多编程语言对递归层次有限制。
- pop方式或许效率有点低，改用索引可能好一点，但是注意尾部。append的效率可能也是低的。
- list(alist)和alist[:]的效率情况未知，但是前者至少支持迭代器过来的流式数据。

3.python实现2（循环bottom-up）

```python
def merge_sort(alist):
    delta = 1
    indexs = list(range(len(alist)))
    while delta < len(alist):
        for start in indexs[::2*delta]:
            mid = start + delta
            end = mid + delta
            left = alist[start:mid]
            right = alist[mid:end]
            copy = []
            while left and right:
                if left[0] <= right[0]:
                    copy.append(left.pop(0))
                else:
                    copy.append(right.pop(0))
            copy.extend(left)
            copy.extend(right)
            alist[start:end] = copy
        delta *= 2
    return alist
```

- 使用循环比递归效率高。
- 在其他语言中不能直接使用end，end可能数组越界，而python中在编程语言级别自动解决了end问题。
- pop和append效率是低的，仍然建议使用指针，同时还是手动解决一下越界问题吧。
- copy数组建议是与原数组来回切换着用，减少一半拷贝量。
- 同时注意到alist实际上是原地的，只是借助了辅助空间copy数组，这样可能仍然是危险的。
- 基于这个代码改多路归并是简单的，只需要改delta的跳跃范围与merge逻辑。