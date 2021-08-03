from collections import defaultdict

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

HASHMAP_SIZE = 1000

class MyHashMap:
    def __init__(self):
        self.size = HASHMAP_SIZE
        self.table = defaultdict(ListNode)


    def put(self, key: int, value: int):
        index = key % self.size

        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    
    def get(self, key: int):
        index = key % self.size

        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value

            p = p.next
        return -1

    def remove(self, key: int):
        index = key % self.size

        if self.table[index].value is None:
            return

        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prov, p = p, p.next

        