class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

"노드 인스턴스 생성"
nodeA = Node(2)
nodeB = Node(3)
nodeC = Node(5)
nodeD = Node(7)
nodeE = Node(11)

nodeA.left_child = nodeB
nodeA.right_child = nodeC
nodeB.left_child = nodeD
nodeB.right_child = nodeE

test_node1 = nodeA.left_child

print(test_node1.data)

test_node2 = nodeB.right_child

print(test_node2.data)
