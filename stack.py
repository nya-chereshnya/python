

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None


class Stack:
    def __init__(self) -> None:
        self.head = Node(None)

    def push(self, data):
        old_head = self.head
        self.head = Node(data)
        self.head.prev = old_head
        return self.head.data

    def pop(self):
        if self.head.prev == None:
            return None
        popped_data = self.head.data
        new_head = self.head.prev
        self.head = new_head
        return popped_data

    def peek(self):
        return self.head.data
    
    def is_empty(self):
        return True if self.head.prev == None else False


hui = Stack()
hui.push(1)
hui.push(2)
hui.push(3)
print(hui.pop())
print(hui.pop())
print(hui.pop())
print(hui.pop())
print(hui.pop())
hui.push(1)
hui.push(2)
hui.push(3)
print(hui.pop())
print(hui.pop())
# print(hui.pop())
print(hui.is_empty())
