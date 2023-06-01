

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = Node(None)

    def __go_to_tail(self):
        current = self.head
        while current.next:
            current = current.next
        return current

    def enqueue(self, data):
        new_tail = Node(data)
        old_tail = self.__go_to_tail()
        old_tail.next = new_tail
        new_tail.prev = old_tail

    def dequeue(self):
        first_node = self.head.next
        if first_node == None:
            return self.head.data
        if first_node.next == None:
            self.head.next = None
            return first_node.data
        self.head.next = first_node.next
        return first_node.data
    

hui = Queue()
hui.enqueue(1)
hui.enqueue(2)
hui.enqueue(3)
print(hui.dequeue())
print(hui.dequeue())
print(hui.dequeue())
print(hui.dequeue())
print(hui.dequeue())
hui.enqueue(1)
hui.enqueue(2)
hui.enqueue(3)
print(hui.dequeue())
print(hui.dequeue())
print(hui.dequeue())