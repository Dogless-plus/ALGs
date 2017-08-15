优先队列PriorityQueue与堆排HeapSort

1.在优先队列中，元素被赋予优先级，最高优先级的先pop。

2.常被用于调度系统。也被用于数组取top-K。

3.几种优先队列的实现

| 数据结构 | 插入效率    | 移除效率    |
| ---- | ------- | ------- |
| 有序数组 | O(N)    | O(1)    |
| 无序数组 | O(1)    | O(N)    |
| 堆    | O(logN) | O(logN) |

可以认为堆是有序数组和无序数组的折衷。

4.一个堆相关的问题取top-K。

- 堆排的复杂度是对数乘以线性的O(NlogN)，插入和删除堆的复杂度都是这个。
- 复杂度为对数乘以线程的常见排序还有快排（无序情况，若有序则是平方级，有大量重复值考虑三路快排），还有归并排序。快排和堆排都不稳定，归并和插入排序（基于有序可以线性O（N），考虑增强的缩小增量希尔排序）是稳定的。
- 堆是近似的完全二叉树，若不满，则最后一层的后半部分。
- 最小堆认为父节点比左右子节点的值小（或相等），但左右间没有要求。
- 插入插在最后面，进行swimup操作。就是关注最后节点，不断与父节点((i-1)//2处)比较的，不满足条件就交换。否则认为已经满足堆条件，敏捷退出。
- 取出从根节点取，用最后节点补上来，进行sindown操作。就是关注根节点，不断与子节点(2xi+1,2xi+2)处较小的比较，若比较小的大，需要与较小的交换，并且去那个位置继续sinkdown。否则敏捷退出。
- top-k若k较小：(1)可以考虑用一个固定容量的堆，数据流过堆(2)用固定桶是一样的(3)MR方法，在map中各取top-k，m路合并到reduce中取top-k。(4)利用快排的partition方法，partition够用了就在其中取得即可。(5)两路合并取top-k问题：两路各在k//2处，若相等，取出两路。若不等，取出一路，问题规模缩小了一半，继续重来。
- top-k若k较大，考虑全局排序(order by)：(1)胜者树：使用分块，块内排序，k路归并。（2）MR方法，预先扫描10000个数，根据这些随机抽样建立顺序100个分区，有上下界，设计key进入100个reducer中，reducer中在上下界内排序，有序取出这些reducer的结果。
- 堆排看起来像是快排和插排的结合体，根据历史信息进行插入，而且插的时候是二分的插。

5.Python实现堆和堆排

```python
class Heap:
    N_INSTANCE = 0  # num of Heap instances in the memory

    def __init__(self, data = None, heap_type="min"):
        """
        initialize a heap and store it in a list type
        :param data: initial value array, can be None
        :param heap_type: min Heap or max Heap, case insensitive
        """
        self._heap_type = heap_type.lower()
        if self._heap_type not in ("min", "max"): raise ValueError("error heap type")
        self._compare = Heap.compare_smaller if heap_type == "min" else Heap.compare_bigger  # function is object
        self.empty = self.is_empty  # alias entry
        self._storage = []  # 0-based database
        self.size = 0
        if data:
            [Heap.check_float(d) for d in data]  # data type check
            self.push_array(data)
        Heap.N_INSTANCE += 1  # initialized

    def swap(self, idx_i, idx_j):
        """
        exchange locations
        :param idx_i: index_1
        :param idx_j: index_2
        :return: void
        """
        self._storage[idx_i], self._storage[idx_j] = self._storage[idx_j], self._storage[idx_i]

    @staticmethod
    def check_float(x):
        """
        :param x: any type
        :return: legal digit or not
        """
        try:
            float(x)
        except:
            raise ValueError("incompatible data type")

    @staticmethod
    def compare_bigger(left, right):
        """
        operator for maxHeap
        :param left: left digital value
        :param right: right digital value
        :return: left value is bigger than the right value or not
        """
        return left > right

    @staticmethod
    def compare_smaller(left, right):
        """
        operator for minHeap
        :param left: left digital value
        :param right: right digital value
        :return: left value is smaller than the right value or not
        """
        return left < right

    def _swim_up(self):
        """
        balance the last node
        """
        node = self.size - 1
        while node > 0:
            parent = (node - 1) // 2  # notice that floor divide and the difference between Python2 and Python3
            if self._compare(self._storage[node], self._storage[parent]):
                self.swap(node, parent)
                node = parent
            else:
                break  # fail agilely

    def _sink_down(self):
        """
        balance the top node
        """
        node = 0
        while 1:  # 1 is better than True in Python
            child = node * 2 + 1
            if child >= self.size: break  # bound
            values = [(self._storage[child], child), ]
            child += 1
            if child < self.size:
                values.append((self._storage[child], child))
            child = values[0][1]
            if len(values) == 2 and self._compare(values[1][0], values[0][0]):
                # right child is smaller (minHeap) or bigger (maxHeap) than the left child
                child += 1
            if self._compare(self._storage[child], self._storage[node]):
                self.swap(node, child)
                node = child
            else:
                break  # fail agilely

    def push(self, x):
        """
        check one value, then push it into the heap
        :param x: digital(int,float,double,...)
        :return: 'success' or raise error
        """
        Heap.check_float(x)
        self._storage.append(x)
        self.size += 1
        if self.size > 1:
            self._swim_up()
        return "success"

    def push_array(self, xs):
        """
        push multiple values into the heap
        :param xs: digital array
        :return: 'success' or  raise error
        """
        [self.push(x) for x in xs]
        return "success"

    def top(self):
        """
        :return: get the top value of the heap instance
        """
        return self._storage[0] if self.size else "empty"

    def pop(self):
        """
        :return: get the top value, then remove it from heap
        """
        if self.size > 0:
            ret = self._storage[0]
            self._storage[0] = self._storage[-1]  # note the head
            self._storage.pop()
            self.size -= 1
            if self.size > 1: self._sink_down()
            return ret
        else:
            return "empty"

    def pop_all(self):
        """
        get all values out one time
        :return: one digital array
        """
        ret = []
        for i in range(self.size):
            ret.append(self.pop())
        return ret

    def reset_empty(self):
        """
        set heap to empty
        :return: 'success' or raise some error
        """
        self._storage = []
        self.size = 0
        return "success"

    def is_empty(self):
        """
        :return: heap is empty or not
        """
        return self.size == 0

    def print_layers(self):
        """
        only for debugging,show tree view
        """
        layers = []
        layer_size = 1
        start = 0
        end = start + layer_size
        while start < self.size:
            layers.append("+".join([str(si) for si in self._storage[start:end]]))
            start = end
            layer_size *= 2
            end = start + layer_size
        max_width = len(layers[-1])
        for i, layer in enumerate(layers):
            white = " " * ((max_width - len(layer)) // 2)
            layers[i] = white + layer + white
        layers.insert(0, "-" * 20 + "start" + "-" * 20)
        layers.append("-" * 20 + "end" + "-" * 20)
        print("\n".join(layers))

    @classmethod
    def heapsort(cls, data, reverse=False):
        """
        :param data: iterable digital array
        :param reverse: desc sort if set to True
        :return: sorted array
        """
        return Heap(data).pop_all() if not reverse \
            else Heap(data, "max").pop_all()

    def heapsort_with_key(self):
        """
        sort multi-columns
        """
        pass  # todo: require new data structure
```

分析：

- JAVA中有PriorityQueue，但是优先队列的实现不一定要用堆。也可以用无序数组，插入O(1)，取出O(N)。也可以用有序数值，插入O(N)，取出O(1)。堆是介于其中的。JAVA中的优先队列默认是最小堆，如果需要改成最大堆只需要实现Compartor的函数式接口。
- Python的函数可以有处于末尾的默认参数。Java的方法没有默认参数，可以通过重载实现。Python不支持重载。
- Python的Class中的普通方法是实例方法，可以被调用self，类方法是类方法，可以被调用cls，静态方法大家都可以调用。静态方法相当于JAVA中的static，ClassLoad载入，大家共用，静态方法不能调用非静态方法（psvm中调用String除外，因为String是JAVA设计者故意留的特例，String太有用了），原因是非静态方法还没有实例化还不存在无法调用，不然都不知道去哪个实例上去调。
- 构造时O(NlogN),查询顶端是O(1)的,移除顶端是O(logN)的。
