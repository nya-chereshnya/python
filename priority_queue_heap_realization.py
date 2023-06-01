from math import floor


class MaxHeap:
    def __init__(self):
        self.heap = []

    def sift_up(self, head):
        size = len(self.heap)
        left = head * 2 + 1
        right = head * 2 + 2
        head_val = self.heap[head]
        left_val = self.heap[left] if left < size else None
        right_val = self.heap[right] if right < size else None
        if left_val is None:
            return
        if right_val is None:
            self.heap[head] = left_val if left_val >= head_val else head_val
            self.heap[left] = left_val if left_val < head_val else head_val
            self.sift_up(left)
        elif left_val > head_val or right_val > head_val:
            route_checker = left if left_val > right_val else right
            self.heap[head] = self.heap[route_checker]
            self.heap[route_checker] = head_val
            self.sift_up(route_checker)

    def sift_down(self, new_element_index):
        if new_element_index == 0:
            return
        size = len(self.heap)
        head = floor((new_element_index - 1) / 2)
        # print(self.heap[head]) 
        # new_element_index = size - 1
        # print(self.heap[new_element_index], self.heap[head])
        if self.heap[new_element_index] > self.heap[head]:
            self.heap[new_element_index], self.heap[head] = self.heap[head], self.heap[new_element_index]
            self.sift_down(head)

    def push(self, item):
        self.heap.append(item)
        new_element_index = len(self.heap) - 1
        self.sift_down(new_element_index)
        # print(self.heap)

    def pop(self):
        if len(self.heap) == 1:
            print(self.heap[0])
            self.heap.pop(-1)
            return
        if len(self.heap) == 0:
            print(self.heap)
            return
        lost = self.heap[0]
        print(lost)
        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)
        self.sift_up(0)

    def traverse(self, head):
        left = head * 2 + 1
        right = head * 2 + 2
        # print(self.heap[head], self.heap[left], self.heap[right])
        return left, right


hui = MaxHeap()
itrations = int(input())
for i in range(itrations):
    text = str(input())
    if text == 'ExtractMax':
        hui.pop()
        continue
    command, value = text.split()
    value = int(value)
    hui.push(value)