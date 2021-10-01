class HashMap:
    def __init__(self):
        self.hashmap = {}
    
    def put(self, key, value):
        if key in self.hashmap:
            self.hashmap[key] = value
        self.hashmap[key] = value
    
    def get(self, key):
        if key in self.hashmap:
            return self.hashmap[key]
        return -1
    
    def remove(self, key):
        if key in self.hashmap:
            del self.hashmap[key]
            return self.hashmap
        return -1

obj = HashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
print(obj.get(3))
obj.put(2, 10)
print(obj.get(2))
obj.remove(2)
print(obj.get(2))
