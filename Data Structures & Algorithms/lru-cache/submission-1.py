class Node:
    def __init__(self, next=None, prev=None, val=0, key=None):
        self.next = next
        self.prev = prev
        self.val = val
        self.key = key
    def __str__(self):
        return f"{self.val}, {self.key}"

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current = 0
        self.address = dict()
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail


    def get(self, key: int) -> int:
        if self.address.get(key, None):
            self.update(key, None)
            return self.address[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # print(key,value)
        # print(self.address)
        if self.address.get(key, None):
            self.update(key, value)
        else:
            if self.current == self.capacity:
                node = self.tail.prev
                del self.address[node.key]
                node.prev.next = self.tail
                self.tail.prev = node.prev
                del node
            else:
                self.current += 1

            new_node = Node(val=value, key=key)
            self.address[key] = new_node
            new_node.prev = self.head
            new_node.next = self.head.next
            self.head.next = new_node
            new_node.next.prev = new_node
        # print(self.address)
        
    
    def update(self, key, value=None):
        node = self.address[key]
        if value:
            node.val = value
        node.prev.next = node.next
        node.next.prev = node.prev
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head


        
