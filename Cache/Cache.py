# Кэш


class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def put(self, key, value):
        if self.is_key(key) is True:
            slot = self.find(key)
        else:
            slot = self.seek_fun(key)
        self.slots[slot] = key
        self.values[slot] = value
        self.hits[slot] = 1

    def hash_fun(self, key):
        code = 0
        for c in str(key):
            code = code * 11 + ord(c)
        return code % self.size

    def seek_fun(self, key):
        if self.slots.count(None) == 0:
            return self.hits.index(min(self.hits))
        slot = self.hash_fun(key)
        count = 0
        while count < self.size:
            if self.slots[slot] is None:
                return slot
            slot += 1
            if slot + 1 > self.size:
                slot -= self.size
            count += 0

    def find(self, key):
        if self.slots[self.seek_fun(key)] == key:
            return self.seek_fun(key)
        #for i in range(self.size):
            #if self.slots[i] == key:
                #return i

    def is_key(self, key):
        if self.find(key) is not None:
            return True
        else:
            return False

    def get(self, key):
        if self.is_key(key) is not False:
            slot = self.find(key)
            self.hits[slot] += 1
            return self.values[slot]


'''
# логи
nc = NativeCache(3)
nc.put('2', 2)
print('find', nc.find('2'))
print('get', nc.get('2'))
print('slots', nc.slots)
print('valies', nc.values)
print('hits', nc.hits)
print('is_key', nc.is_key('2'))


nc.put('2', 30)
nc.put('1', 1)
nc.put('3', 3)

nc.get('3')
nc.put('4', 4)
print('slots', nc.slots)
print('valies', nc.values)
print('hits', nc.hits)
'''
