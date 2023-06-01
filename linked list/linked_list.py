from custom_exeptions import *


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = Node(head)
        self.tail = self.head

    def _get_node(self, index):
        if index < 0:
            raise IndexOutOfBoundError(index)
        current = self.head
        for i in range(index):
            if current.next is None:
                raise IndexOutOfBoundError(index)
            current = current.next
        return current

    def __getitem__(self, index):
        node = self._get_node(index)
        return node.data

    def __setitem__(self, index, value):
        node = self._get_node(index)
        node.data = value

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def push(self, data):
        new_node = Node(data)
        if self.head.data == None:
            self.head = new_node
        self.tail.next = new_node
        self.tail = new_node
        return self.tail.data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def _insert_in_head(self, data):
        new_node = Node(data)
        if self.head.data == None:
            self.head = new_node
            return self.head.data
        new_node.next = self.head.next
        self.head.next = new_node
        return new_node.data

    def _move_to_index(self, index):
        current = self.head
        for i in range(index):
            if current.next is None:
                raise IndexOutOfBoundError(index)
            current = current.next
        return current

    def _update_tail(self, new_tail):
        new_tail.next = None
        self.tail = new_tail

    def insert(self, index, data):
        if index < 0:
            raise IndexOutOfBoundError(index)
        if index == 0:
            return self._insert_in_head(data)
        current = self._move_to_index(index)
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        current = current.next
        if current.next == None:
            self._update_tail(new_node)
        return current.data

    def remove(self, data):
        if self.head.data == data:
            return self.shift()
        if self.tail.data == data:
            return self.pop()
        current = self.head
        while current.next:
            first = current
            second = first.next
            third = second.next
            if second.data == data:
                first.next = third
                return True
            current = current.next
        raise ElementNotFoundError(data)

    def remove_all(self, data):
        found = False
        while self.head.data == data:
            self.shift()
            found = True
        while self.tail.data == data:
            self.pop()
            found = True
        current = self.head
        while current.next:
            first = current
            second = first.next
            third = second.next
            if second.data == data:
                first.next = third
                found = True
            current = current.next
        if not found:
            raise ElementNotFoundError(data)
        return True

    def delete(self, index):
        if index < 0:
            raise IndexOutOfBoundError(index)
        if index == 0 and self.head.next == None:
            raise EmptyLinkedListError
        current = self.head
        if index == 0:
            self.head = self.head.next
            return True
        for i in range(index-1):
            if current.next == None:
                raise IndexOutOfBoundError(index)
            current = current.next
        current.next = current.next.next
        if current.next == None:
            self._update_tail(current)
        return True

    def pop(self):
        currnet = self.head
        if currnet.next == None:
            raise EmptyLinkedListError
        while currnet.next.next:
            currnet = currnet.next
        currnet.next = None
        self.tail = currnet

    def length(self):
        currunt = self.head
        length = 0
        while currunt:
            length += 1
            currunt = currunt.next
        return length

    def to_array(self):
        return list(self.__iter__())

    def find(self, data):
        index = 0
        current = self.head
        while current:
            if current.data == data:
                return index
            index += 1
            current = current.next
        raise ElementNotFoundError(data)

    def find_all(self, data):
        indexes = []
        current_index = 0
        current = self.head
        while current:
            if current.data == data:
                indexes.append(current_index)
            current_index += 1
            current = current.next
        if len(indexes) == 0:
            raise ElementNotFoundError(data)
        return indexes

    def swap(self, index_1, index_2):
        current = self.head
        count = 0
        first_node = None
        second_node = None
        while current:
            if count == index_1:
                first_node = current
            if count == index_2:
                second_node = current
            count += 1
            current = current.next
        if first_node == None:
            raise IndexOutOfBoundError(index_1)
        if second_node == None:
            raise IndexOutOfBoundError(index_2)
        first_node.data, second_node.data = second_node.data, first_node.data
        return True

    def shift(self):
        current = self.head
        if current.next == None:
            raise EmptyLinkedListError
        self.head = current.next
        return self.head.data

    def unshift(self, value):
        new_node = Node(value)
        if self.head.data == None:
            self.tail = new_node
            return self._insert_in_head(value)
        new_node.next = self.head
        self.head = new_node
        return self.head.data


linked_list = LinkedList(1)
linked_list.push(2)
linked_list.push(3)
linked_list.push(4)
linked_list.push(5)
# linked_list.display()
for i in linked_list:
    print(i)
# class LinkedList has methods to push and pop, and display, and remove, and find, and find_all, and swap, and unshift, and shift
# linked_list.push(4)
# linked_list.push(5)
# linked_list.push(6)
# linked_list.display()
# linked_list.remove(2)
# linked_list.display()
# print(linked_list.tail.data, "tail")
# linked_list.push(3)
# linked_list.pop()
# linked_list.display()
# linked_list.push(4)
# linked_list.display()
# linked_list.push(5)
# linked_list.display()
# linked_list.pop()
# linked_list.display()
# linked_list.delete(5)
# linked_list.display()
# print(linked_list)

# IERATIONS = 10000

# a = []

# for i in range(IERATIONS):
#     a.append(text)

# start_time_ARRAY = time.time()
# for i in range(IERATIONS):
#     random_index_1 = random.randint(0, IERATIONS-1)
#     random_index_2 = random.randint(0, IERATIONS-1)
#     a.insert(random_index_2, "hui")
#     a.pop(random_index_1)
# end_time_ARRAY = time.time()
# execution_time_ARRAY = end_time_ARRAY - start_time_ARRAY


# linked_list = LinkedList()
# for i in range(IERATIONS):
#     linked_list.push(text)


# start_time_LINKED_LIST = time.time()
# for i in range(IERATIONS):
#     random_index_1 = random.randint(0, IERATIONS-1)
#     random_index_2 = random.randint(0, IERATIONS-1)
#     linked_list.insert(random_index_2, text)
#     linked_list.delete(random_index_1)
# end_time_LINKED_LIST = time.time()
# execution_time_LINKED_LIST = end_time_LINKED_LIST - start_time_LINKED_LIST

# print(execution_time_ARRAY, execution_time_LINKED_LIST)
