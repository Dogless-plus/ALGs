冒泡排序BubbleSort

冒泡时两两交换，进行n趟，复杂度平方级。可以是稳定的（原来相等的key保持原来顺序不变）。

1.Python实现1：

```python
def bubble_sort(alist):
    for _ in range(len(alist)):
        for i in range(len(alist) -1):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
    return alist
```

分析：

- 没有做类型检查（对Java等强类型语或许传入的是强类型array，但也要保证有compareTo，或者重载了大于号）。
- 没有确定类型，未必有\__len__()属性。有这个属性，需要满足长度2以上。
- alist使用浅拷贝可能是危险的，除非非常明确他的全局意义，否则无意中可能覆盖全局数据。或者说本身排序是原地的。
- 另外一种风险就是，可能传入的是一个迭代器，数据是流式数据，甚至无法在原地操作，需要设置接收器。

2.python实现2：

```python
def bubble_sort(blist):
    try:
        blist = list(blist)
    except:
        raise ValueError("unacceptable type")
    for _ in range(len(blist)):
        for i in range(len(blist) -1):
            if blist[i] > blist[i+1]:
                blist[i], blist[i + 1] = blist[i + 1], blist[i]
    return blist
```

- try-except 语句本身开销巨大。虽然避免了迭代器或者浅拷贝的风险。
- 另外，blist的返回类型是列表，仍然是不够安全的。改成元组会安全一些，但是后续使用依然是无法保证的。