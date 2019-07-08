class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return self.slots.index(None)

    def seek_slot(self, value):
        if self.slots.count(None) != 0:
            return self.slots.index(None)
        else:
            return None

    def put(self, value):
        index = self.seek_slot(value)
        if index != None:
            self.slots[index] = value
            return index
        else:
            return None

    def find(self, value):
        if value in self.slots:
            return self.slots.index(value)
        else:
            return None
