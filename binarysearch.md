二叉搜索、二分查找、BinarySearch

效率：O(logN)

前提：数组有序。或者断点有序，比如旋转数组，可以先二分查找，再线性搜索。

思路：前后与折半处比较，调整前后范围，大往大找，小往小找。

```python
def binary_search(key,alist):
    alist = list(alist)  # 使用额外空间有几个好处，第一是不影响这个数据继续被其他线程使用，第二是不容易修改全局数据，第三是支持迭代器过来的流式数据
    left, right = 0, len(alist)-1 
    # 入口判断，若有大量范围外导致的 search miss 应该考虑加上这句『敏捷失败』
    if key < alist[left] or key > alist[right]: return -1
    mid = None  # 注意mid在其他语言中可能需要保持全局，但是在python中其实是可以在while之后将mid穿透到下面去的，并没有销毁
    while left <= right:  # 注意保证相遇处。依赖于mit+1和mid-1的更新式
        mid = left + (right-left) // 2  # 注意两个问题：Python2和Python3的除法略有区别，请使用这种无歧义的写法；
                                        # 第二个问题是溢出问题，其他语言可能考虑直接相加的溢出，Python基本没有这个问题，可以直接相加
        if alist[mid] == key: return mid
        elif alist[mid] > key: right = mid - 1  # 注意这种更新方式仅仅针对整数，若将二分查找用于凸函数的0点求值，可能要考虑无最小增量的更新式，但是带来了新的问题是while条件如果继续使用相等会不会陷入死循环，或许要额外增加判断条件或者使用一个最小增量
        else: left = mid + 1  # 同上
    if abs(alist[mid] - key) < 2: return mid  # 也接受估计结果，这样对于抽样之后进行搜索也是有好处的
    return -1  # 注意可以返回search miss 或者可以返回一个最接近的值left
```

- 一定要保证查询范围是有序的，否则输错了错误的结果。但是有一点可以确定是不会陷入死循环。
- 改成递归是简单的，或者可以在全局悬挂一个search hit 状态进行『敏捷成功』。但是不要去写递归，递归是低效的。