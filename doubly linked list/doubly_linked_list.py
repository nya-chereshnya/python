from custom_exeptions import *


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList():
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head

    def __move(self, node, interval):
        current = node
        count = 0
        interval_check = interval < 0
        while count != interval:
            current = current.prev if interval_check else current.next
            count += -1 if interval_check else 1
        return current

    def __clear_head(self):
        self.head.data = None

    def __fill_head(self, data):
        self.head.data = data

    def __connect(self, node_1, node_2):
        node_1.next = node_2
        node_2.prev = node_1

    def __find(self, data):
        current = self.head
        while True:
            if current.data == data:
                return current
            current = current.next
            if current == self.head:
                raise ElementNotFoundError(data)

    def __iter__(self):
        current = self.head
        while True:
            yield current.data
            current = self.__move(current, 1)
            if current == self.head:
                break

    def __next__(self):
        self.current = self.head

    def __getitem__(self, index):
        return self.__move(self.head, index).data

    def __setitem__(self, index, value):
        node = self.__move(self.head, index)
        node.data = value
        return

    def push(self, data):
        if self.head.data == None:
            return self.__fill_head(data)
        if self.head.next == self.head:
            new_node = Node(data)
            self.__connect(self.head, new_node)
            self.__connect(new_node, self.head)
        elif self.head.prev != self.head:
            old_tail = self.head.prev
            new_tail = Node(data)
            self.__connect(old_tail, new_tail)
            self.__connect(new_tail, self.head)
        return self.head.prev.data

    def pop(self):
        lost_node = self.__move(self.head, -1).data
        if self.head.data == None:
            raise EmptyLinkedListError
        if self.head.next == self.head:
            self.__clear_head()
        elif self.head.prev != self.head:
            old_tail = self.__move(self.head, -1)
            new_tail = self.__move(old_tail, -1)
            self.__connect(new_tail, self.head)
        return lost_node

    def display(self):
        current = self.head
        while True:
            print(current.data, end=" ")
            current = self.__move(current, 1)
            if current == self.head:
                break
        print()

    def delete(self, index):
        lost_node = self.__move(self.head, index).data
        if self.__move(self.head, index) == self.head:
            return self.shift()
        previous_node = self.__move(self.head, index-1)
        next_node = self.__move(previous_node, 2)
        self.__connect(previous_node, next_node)
        return lost_node

    def shift(self):
        lost_node = self.head.data
        if self.head.data == None:
            raise EmptyLinkedListError
        if self.head.next == self.head:
            self.__clear_head()
            return lost_node
        self.head.data = self.__move(self.head, 1).data
        self.head.next = self.__move(self.head, 2)
        return lost_node

    def unshift(self, data):
        if self.head.data == None:
            self.head.data = data
        else:
            old_head = Node(self.head.data)
            new_head = self.head
            new_head.data = data
            node_after_old_head = self.__move(self.head, 1)
            self.__connect(new_head, old_head)
            self.__connect(old_head, node_after_old_head)
        return self.head.data

    def remove(self, data):
        count = 0
        if self.head.data == data:
            return self.shift()
        current = self.__move(self.head, 1)
        count = 1
        while current != self.head:
            if current.data == data:
                return self.delete(count)
            current = self.__move(current, 1)
            count += 1
        raise ElementNotFoundError(data)

    def slice(self, start, end):
        new_list = DoublyLinkedList()
        current = self.__move(self.head, start)
        new_list.push(current.data)
        for i in range(abs(end - start)):
            current = self.__move(current, 1)
            new_list.push(current.data)
        return new_list


loh = DoublyLinkedList()
for i in range(12):
    loh.push(i)

loh.display()   
# loh.push(6)
# loh.push(7)
# loh.push(8)
# loh.push(9)

# loh.display()
# loh.delete(3)
# loh.display()

# hui = loh.slice(2, 5)
# hui.display()
