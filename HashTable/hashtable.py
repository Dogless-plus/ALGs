# coding = utf-8


class HashTable:
    class KV:
        """
        for storage
        """
        def __init__(self, k, v):
            self.k = k
            self.v = v

        def __repr__(self):
            return "k:%s,v:%s" % (self.k, self.v)

    def __init__(self, init_capacity=4, init_load_factor=0.75):
        self.capacity = init_capacity
        self.load_factor = init_load_factor
        self.size = 0
        self.buckets = None
        self._init()
        self.hash = self._mod_hash

    def _init(self):
        """
        prepare buckets
        :return: bucket tuple
        """
        self.buckets = tuple([] for _ in range(self.capacity))  # list is mutable, whilst tuple is immutable

    def _rehash(self):
        """
        inflate table
        """
        self.capacity = self.capacity << 1
        new_buckets = tuple([] for _ in range(self.capacity))
        for bucket in self.buckets:
            for item in bucket:
                idx = self.hash(item.k)
                kv = HashTable.KV(item.k, item.v)
                new_buckets[idx].append(kv)
        tmp = self.buckets
        self.buckets = new_buckets
        del tmp

    def _mod_hash(self, key):
        """
        alternative hash function
        :param key: int key
        :return: int idx
        """
        return key % self.capacity

    def contains(self, key):
        """
        in or not in the table
        :param key: int key
        :return: True or False
        """
        idx = self.hash(key)
        for item in self.buckets[idx]:
            if key == item.k:
                return True
        return False

    def put(self, k, v):
        """
        put item
        :param k: int item_key
        :param v: object item_value
        """
        bucket = self.buckets[self.hash(k)]  # shallow copy
        need_insert = True
        for item in bucket:
            if item.k == k:
                item.v = v  # update value
                need_insert = False
        if need_insert:
            kv = HashTable.KV(k, v)
            bucket.insert(0, kv)
            self.size += 1
        if float(self.size) >= self.capacity * self.load_factor:
            self._rehash()
        return self

    def delete(self, key):
        """
        try to remove item
        :param key: int item_key
        """
        deleted = False
        idx = self.hash(key)
        bucket = self.buckets[idx]  # shallow copy
        for i, item in enumerate(bucket):
            if key == item.k:
                bucket.pop(i)
                self.size -= 1
                deleted = True
        return deleted

    def __repr__(self):
        return self.buckets.__str__()
