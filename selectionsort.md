选择排序SelectionSort

每次从待排列表中选出一个最小的元素加入已排序列表。

复杂度O(N2),对输入有序还是无序不敏感。

方式一：使用外部空间依次添加。

方式二：原地，未排序中的与已排序的交换。

1.Python实现1（外部空间）：

```python
def selection_sort(alist):
    alist = list(alist)
    blist = []
    while len(alist):
        min_idx , min_value = 0, alist[0]
        for i, v in enumerate(alist):
            if v < min_value:
                min_idx = i
                min_value = v
        blist.append(alist.pop(min_idx))
    return blist
```

分析：

- 未做类型检查，不能保证list()能正确获得数据列表，不能保证数据类型重载了小于号。
- append和pop语句有可能是代价比较高，将效率依赖于列表的实现了。

2.Python实现2（原地修改）：

```python
def selection_sort(alist):
    for i in range(len(alist) - 1):
        for j in range(i+1, len(alist)):
            if alist[j] < alist[i]:
                alist[j], alist[i] = alist[i], alist[j]
```

分析：

- 将实现依赖于浅拷贝，假想了alist是个list。那么如果alist是个元组或者迭代器呢？
- 可以直观看出使用的技巧是双指针交换法，一个前向探索指针。很容易判断复杂度是平方级，而且是输入有序无序不敏感的。
- 缩进的层次有点多，虽然仍然在可接受的范围（5层）内，影响了可读性。
- 可以看出，选择排序可以是稳定的。

