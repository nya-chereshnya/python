import heapq

text = "beep boop beer!"


class Element:
    def __init__(self, node, pririty, value=None):
        self.node = node
        self.priority = pririty
        self.value = value

        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority


queue = []
while text:
    simbol = text[0]
    simbol_count = text.count(simbol)
    element = Element(simbol, simbol_count)
    heapq.heappush(queue, element)
    text = text.replace(simbol, "")

while len(queue) != 1:
    first = heapq.heappop(queue)
    second = heapq.heappop(queue)
    result = Element([first, second],
                     first.priority + second.priority)
    result.left = first
    result.right = second
    heapq.heappush(queue, result)

main_node = heapq.heappop(queue)
# print(main_node.node[0].node[0].node)

def dfs(node):
    if node is None:
        return

    print(node.node)
    dfs(node.left)
    dfs(node.right)

dfs(main_node)
