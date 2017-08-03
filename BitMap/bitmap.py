# coding=utf-8

class BitMap:
    """
    class for bitmap_sort
    """

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.bm = bytearray(b'\0' * self.capacity)
        self.limit_max = capacity * 8 - 1
        self.limit_min = 0
        self.size = 0

    @staticmethod
    def _get_position(x):
        """
        convert key to position in the bitmap
        :param x: int key
        :return: int row, int column
        """
        # imagine one matrix, row at idx_array, column at idx_byte
        idx_array = x >> 3  # x // 8
        idx_byte = x & 0x07  # x % 8
        return idx_array, idx_byte

    def _check_range(self, x):
        """
        check if the key is acceptable
        :param x: int key
        """
        if x > self.limit_max or x < self.limit_min:
            raise ValueError("value:%s is too large or too small" % x)

    def put(self, x):
        """
        add key into the bitmap
        :param x: int key
        """
        self._check_range(x)
        idx_array, idx_byte = self._get_position(x)
        self.bm[idx_array] |= 1 << idx_byte
        self.size += 1

    def remove(self, x):
        """
        remove key from the bitmap
        :param x: int key
        """
        self._check_range(x)
        idx_array, idx_byte = self._get_position(x)
        self.bm[idx_array] &= ~(1 << idx_byte)
        self.size -= 1

    def contains(self, x):
        """
        check if a key is in the bitmap
        :param x: int key
        :return: True or False
        """
        self._check_range(x)
        idx_array, idx_byte = self._get_position(x)
        return self.bm[idx_array] & (1 << idx_byte) != 0

    def reset(self, capacity=None):
        """
        reset the bitmap to a zero-array with new capacity
        :param capacity: int
        """
        self.capacity = capacity if capacity else self.capacity
        self.__init__(self.capacity)

    def put_batch(self, xs):
        """
        put keys into the bitmap
        :param xs: int [] keys
        """
        [self.put(x) for x in xs]

    def decode_bm(self):
        """
        decode the bitmap into a human-readable int array
        :return: int []
        """
        ret = []
        i = self.limit_min
        while i <= self.limit_max:
            if self.contains(i):
                ret.append(i)
            i += 1
        return ret

    def bitmap_sort(self, xs):
        """
        sort numbers using a bitmap
        :param xs: int []
        :return: int []
        """
        capacity = max(xs) // 8 + 1
        self.reset(capacity=capacity)
        self.put_batch(xs)
        return self.decode_bm()

    @classmethod
    def sort(cls, xs):
        """
        just class method for sorting with bitmap
        :param xs: int []
        :return: int []
        """
        capacity = max(xs) // 8 + 1
        bm = BitMap(capacity)
        bm.put_batch(xs)
        return bm.decode_bm()

    def show(self):
        """
        show the bitmap
        :return: int []
        """
        print([mi.__str__() for mi in self.bm])

    def test(self):
        """
        check the functional of the class
        :return: raise or return True
        """
        from random import randint
        x = [randint(0, 1000) for _ in range(20)]
        for _ in range(100):
            try:
                assert tuple(sorted(set(x))) == tuple(BitMap().bitmap_sort(x))
            except AssertionError:
                print sorted(x)
                print BitMap().bitmap_sort(x)
        for _ in range(100):
            try:
                assert tuple(sorted(set(x))) == tuple(BitMap.sort(x))
            except AssertionError:
                print sorted(x)
                print BitMap.sort(x)
        print("it works")
        return True


if __name__ == '__main__':
    BitMap().test()
