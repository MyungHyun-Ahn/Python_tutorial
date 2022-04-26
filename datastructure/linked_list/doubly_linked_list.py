class Node:
    """더블리 링크드 리스트 노드"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """더블리 링크드 리스트"""
    def __init__(self):
        self.head = None
        self.tail = None

    # 접근 연산
    def find_node_at(self, index):
        """접근 연산 메소드"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next
        return iterator
    
    # 탐색 연산
    def find_node_with_data(self, data):
        """탐색 연산 메소드"""
        iterator = self.head

        while iterator is not None:
            if iterator.data == data:
                return iterator
            iterator = iterator.next
        return None

    # 추가 연산
    def append(self, data):
        """추가 연산 메소드"""
        new_node = Node(data)

        # 링크드 리스트가 비어 있을 때
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # 삽입 연산
    def insert_after(self, previous_node, data):
        """삽입 연산 메소드"""
        new_node = Node(data)
        if previous_node == self.tail:
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node.prev = previous_node
            new_node.next = previous_node.next
            previous_node.next.prev = new_node
            previous_node.next = new_node


    def prepend(self, data):
        """헤드 노드의 앞에 새로운 노드를 삽입하는 메소드"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, node_to_delete):
        """삭제 연산 메소드"""
        if (node_to_delete == self.head) and (node_to_delete == self.tail):
            self.head = None
            self.tail = None
        elif node_to_delete is self.head:
            node_to_delete.next.prev = None
            self.head = node_to_delete.next
        elif node_to_delete is self.tail:
            node_to_delete.prev.next = None
            self.tail = node_to_delete.prev
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev
        return node_to_delete.data

    def __str__(self):
        """링크드 리스트 요소 모두 출력하는 메소드"""
        res_str = "|"
        iterator = self.head
        while iterator is not None:
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next
        return res_str


doublyLinked = DoublyLinkedList()

doublyLinked.append(2)
doublyLinked.append(3)
doublyLinked.append(5)
doublyLinked.append(7)

node_2 = doublyLinked.find_node_at(0)
doublyLinked.insert_after(node_2, 4)

print(doublyLinked)