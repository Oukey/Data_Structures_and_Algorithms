# Кэш


class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        if self.is_key(key) is False:
            if self.slots.count(None) != 0:
                return self.slots.index(None)
            else:
                return self.hits.index(min(self.hits))
        else:
            return None

    def put(self, key, value):
        slot = self.hash_fun(value)
        if slot is not None:
            self.slots[slot] = key
            self.values[slot] = value
            self.hits[slot] = 1
            return slot

    def is_key(self, key):
        if key in self.slots:
            return True
        else:
            return False

    def get(self, key):
        if self.is_key(key) is True:
            self.hits[self.slots.index(key)] += 1
            return self.values[self.slots.index(key)]
        else:
            return None
