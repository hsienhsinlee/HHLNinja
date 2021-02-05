#!/usr/local/bin/python3

"""

Implement a Least-Recently Used (LRU) cache

1. When an item is added or updated it is now the most recently used
item a.k.a. freshest item.

2. When the cache has exceeded capacity, the "least recently used"
item is evicted, memory is not unbounded.

3. Highly performant. O(1) constant/update if possible.

Example:

capacity = 3.

put A, value1
put B, value2
put C, value3
get A                   // A becomes Most Recently Used
put C, value4           // C becomes Most Recently Used
get D, return -1
put D, value5           // B is removed, and D is added.
get B, return -1

"""

class dll:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.length = 0
        self.dict = dict() # to store the key-pointer pair, the pointer points to the doubly-linked list element
        self.head = dll(-1, -1) # head always points to LRU line
        self.tail = self.head

    def size(self):
        return self.capacity

    def listall(self):
        print("From LRU: ", end="")
        node = self.head
        while (node):
            print(node.key, "-->", end="")
            node = node.next
        print()



    def get(self, key):
        if key in self.dict:
            hit_line = self.dict[key]
            if (hit_line != self.tail):
                hit_line.next.prev = hit_line.prev
                hit_line.prev.next = hit_line.next
                hit_line.prev = self.tail
                self.tail.next = hit_line
                hit_line.next = None
                self.tail = hit_line
            return hit_line.value
        else:
            return -1

    def put(self, key, value):
        if key in self.dict:  # a cache hit
            print("put", key," hit")
            line = self.dict[key]
            line.value = value
            if (line != self.tail):
                line.prev.next = line.next
                line.next.prev = line.prev
                self.tail.next = line
                line.next = None
                line.prev = self.tail
                self.tail = line
        else: # a cache miss
            print("put", key, "miss")
            if (self.length == self.capacity): #replacement needed
                print("cache full")
                LRU_line = self.head.next
                LRU_line.next.prev = self.head
                self.head.next = LRU_line.next
                del self.dict[LRU_line.key]
                # insert MRU to the tail
            else:
                self.length += 1
            # a MRU cache line is inserted
            line = dll(key, value)
            self.dict[key] = line
            line.prev = self.tail
            line.next = None
            self.tail.next = line
            self.tail = line


cache = LRUCache(2)
cache.put('a', 1)
cache.put('b', 2)
cache.put('c', 3)
print("a=", cache.get('a'))
cache.listall()
cache.put('c', 4)
cache.listall()
print('d=', cache.get('d'))
cache.put('d', 4)
cache.listall()
print('d=', cache.get('d'))
cache.listall()
print('b=', cache.get('b'))
cache.listall()
cache.put('d', 5)
cache.listall()
print('a=', cache.get('a'))
cache.listall()
cache.put('c', 6)
cache.listall()
