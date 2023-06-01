

class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self) -> None:
        self.head = Node(None, float("inf"))

    def __traverse(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __connect(self, node_1, node_2, node_3=None):
        if node_3:
            node_1.next = node_2
            node_2.next = node_3
        else:
            node_1.next = node_2

    def __empty_head_check(self, node):
        if self.head.next:
            return False
        if self.head.data == None:
            self.head = node
        elif self.head.next == None:
            self.head.next = node
        return True

    def __head_piority_check(self, node):
        if self.head.priority > node.priority:
            old_head = self.head
            self.head = node
            self.__connect(self.head, old_head, old_head.next)
            return True
        return False

    def __insert_node(self, new_node):
        tail = None
        for current in self.__traverse():
            if not current.next:
                break
            tail = current.next
            if current.next.priority > new_node.priority:
                return self.__connect(current, new_node, current.next)
        return self.__connect(tail, new_node)

    def enqueue(self, data, priority):
        new_node = Node(data, priority)
        if self.__head_piority_check(new_node):
            return 0
        if self.__empty_head_check(new_node):
            return 0
        return self.__insert_node(new_node)

    def dequeue(self):
        lost_node = Node(self.head.data, self.head.priority)
        if self.head.data == None:
            return None
        if self.head.next == None:
            self.head.data = None
        else:
            self.head = self.head.next
        return lost_node
    
    def shift(self):
        node = self.head
        for current in self.__traverse():
            if current.next.next:
                print(current.next.data)
                current.next = None
                break
            node = current
        self.head = node

    def display(self):
        for current in self.__traverse():
            print(f'{current.data} - data, {current.priority} - priority')

