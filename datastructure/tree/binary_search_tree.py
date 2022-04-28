from turtle import right


class Node:
    """이진 탐색 트리 노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

def print_inorder(node):
    """주어진 노드를 in-order로 출력해주는 함수"""
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)

class BinarySearchTree:
    "이진 탐색 트리 클래스"
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)  # 삽입할 데이터를 갖는 새 노드 생성

        # 트리가 비었으면 새로운 노드를 root 노드로 만든다
        if self.root is None:
            self.root = new_node
            return

        node = self.root

        while True:
            if node.data < new_node.data:
                if node.right_child is None:
                    node.right_child = new_node
                    new_node.parent = node
                    return
                else: 
                    node = node.right_child
            else:
                if node.left_child is None:
                    node.left_child = new_node
                    new_node.parent = node
                    return
                else: 
                    node = node.left_child

    def search(self, data):
        """이진 탐색 트리 탐색 메소드, 찾는 데이터를 갖는 노드가 없으면 None을 리턴한다"""
        # 코드를 쓰세요
        node = self.root

        while True:
            if node is None:
                return None
            if node.data > data:
                node = node.left_child
            elif node.data < data:
                node = node.right_child
            else:
                return node

    @staticmethod
    def find_min(node):
        """(부분)이진 탐색 트리의 가장 작은 노드 리턴"""
        # 코드를 쓰세요
        while True:
            if node.left_child is None:
                return node
            else:
                node = node.left_child


    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.root) # root 노드를 in-order로 출력한다.

    def delete(self, data):
        """이진 탐색 트리 삭제 메소드"""
        node_to_delete = self.search(data)  # 삭제할 노드를 가지고 온다
        parent_node = node_to_delete.parent  # 삭제할 노드의 부모 노드


        # 경우 1: 지우려는 노드가 leaf 노드일 때 (코드를 쓰세요!)
        if node_to_delete.right_child is None and node_to_delete.left_child is None:
            if node_to_delete.data > parent_node.data:
                parent_node.right_child = None
                return
            else:
                parent_node.left_child = None
                return
        
        # 경우 2: 지우려는 노드가 자식이 하나인 노드일 때: XOR 연산하여 조건중 1개만 참일 때 True
        if (node_to_delete.right_child is None) ^ (node_to_delete.left_child is None):
            if node_to_delete.right_child is not None:
                parent_node.right_child = node_to_delete.right_child
                return
            else:
                parent_node.left_child = node_to_delete.left_child
                return

        # 경우 3: 지우려는 노드가 2개의 자식이 있을 때
        if (node_to_delete.right_child is not None) and (node_to_delete.left_child is not None):
            successor = BinarySearchTree.find_min(node_to_delete.right_child)
            node_to_delete.data = successor.data
            sp = successor.parent
            if sp.left_child is not None:
                sp.left_child = None
            else:
                sp.right_child = None
            return




# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 자식이 두 개 다 있는 노드 삭제
bst.delete(7)
bst.print_sorted_tree()

bst.delete(11)

bst.print_sorted_tree()