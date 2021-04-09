#!/usr/local/bin/python3

class DNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DList(object):
    def __init__(self):
        self.head = DNode("", "")
        self.tail = DNode("", "")
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        #node.next = self.head.next
        #node.prev = self.head
        #self.head.next = node

        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = DList()
        self.store = {}

    def put(self, key, value):
        if key in self.store:
            node = self.store[key]
            node.value = value
            self.list.remove(node)
            self.list.add(node)
        elif len(self.store) < self.capacity:
            node = DNode(key, value)
            self.store[key] = node
            self.list.add(node)
            tmp = self.list.tail.prev
            print("HE", tmp.key)
        else:
            print(self.store)
            lrunode = self.list.tail.prev
            self.store.pop(lrunode.key)
            self.list.remove(lrunode)
            newnode = DNode(key, value)
            self.list.add(newnode)
            self.store[key] = newnode

    def get(self, key):
        if key not in self.store:
            return -1
        else:
            node = self.store[key]
            self.list.remove(node)
            self.list.add(node)
            return node.value


LC = LRUCache(3)
LC.put('a', 11)
LC.put('b', 12)
LC.put('c', 13)
LC.put('d', 14)

a = LC.get('a')
print("a =", a)
b = LC.get('b')
print("b =", b)
c = LC.get('c')
print("c =", c)
d = LC.get('d')
print("d =", d)
LC.put('e', 15)
b = LC.get('b')
print("b =", b)
c = LC.get('c')
print("c =", c)
d = LC.get('d')
print("d =", d)
