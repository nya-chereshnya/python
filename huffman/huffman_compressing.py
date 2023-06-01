

class Node:
    def __init__(self, frequency, char) -> None:
        self.frequency = frequency
        self.char = char
        self.code = ''

    def __lt__(self, other):
        return self.frequency < other.frequency


class Tree:
    def __init__(self, left, right) -> None:
        self.frequency = left.frequency + right.frequency
        self.left = left
        self.right = right
        self.left_code = ''
        self.right_code = ''
        self.char = ''

    def __lt__(self, other):
        return self.frequency < other.frequency


class PriorityQueue:
    def __init__(self) -> None:
        self.arr = []

    def __len__(self):
        return len(self.arr)

    def put(self, item):
        self.arr.append(item)
        self.arr = sorted(self.arr, key=lambda x: x, reverse=False)

    def get(self):
        return self.arr.pop(0)


class Huffman:
    def __init__(self, text) -> None:
        self.text = text
        self.nodes_queue = PriorityQueue()
        self.tree = None
        self.one = '1'
        self.zero = '0'
        self.dict = {}
        self.codes = ''
        self.amount = 0

    def _create_queue(self, text):
        while text:
            node = Node(text.count(text[0]), text[0])
            self.nodes_queue.put(node)
            text = text.replace(text[0], '')
        self.amount = len(self.nodes_queue)
        return self.nodes_queue

    def _create_tree(self, queue, ):

        while len(self.nodes_queue) > 1:
            right = queue.get()
            left = queue.get()
            tree = Tree(left, right)
            tree.left_code = self.one
            tree.right_code = self.zero
            queue.put(tree)
        self.tree = queue.get()
        return self.tree

    def _traverse(self, tree, code=''):
        if type(tree) == Node:
            tree.code = code
            self.dict[tree.char] = code
            return

        left_code = code + tree.left_code
        right_code = code + tree.right_code

        self._traverse(tree.left, left_code)
        self._traverse(tree.right, right_code)

    def _create_codes(self):
        self._create_queue(self.text)
        if len(self.nodes_queue) == 1:
            self.dict[self.nodes_queue.get().char] = '0'
            return
        self._create_tree(self.nodes_queue)
        self._traverse(self.tree)

    def display(self):
        self._create_codes()
        for i in self.text:
            self.codes += self.dict[i]
        print(self.amount, len(self.codes))
        for key, value in self.dict.items():
            print(f'{key}: {value}')
        print(self.codes)


text = str(input())
gavno = Huffman(text).display()
