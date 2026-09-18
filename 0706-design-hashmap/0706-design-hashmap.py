class MyHashMap(object):

    def __init__(self):
        self.data = [None] * 1000001
        

    def put(self, key, value):
        self.data[key] = value
        

    def get(self, key):
        val = self.data[key]
        return val if val != None else -1
        

    def remove(self, key):
        
        self.data[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)