# coding = utf-8
# author: dogless
# date: 2017-07-21

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


def demo():
    """
    valid functions
    """
    from random import uniform  # dynamic import
    for i in range(100):
        xs = [uniform(-1000000, 100000) for _ in range(100)]
        assert (tuple(Heap(xs, heap_type="min").pop_all()) == tuple(sorted(xs)))
        assert (tuple(Heap(xs, heap_type="max").pop_all()) == tuple(sorted(xs, reverse=True)))
        assert (tuple(Heap.heapsort(xs)) == tuple(sorted(xs)))
        assert (tuple(Heap.heapsort(xs, reverse=True)) == tuple(sorted(xs, reverse=True)))
    print("it works")


if __name__ == '__main__':
    demo()