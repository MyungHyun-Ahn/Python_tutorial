from requests import delete


class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data):
        self.data = data # 노드가 저장하는 데이터
        self.next = None # 다음 노드에 대한 레퍼런스

class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None
        self.tail = None

    def find_node_at(self, index):
        """링크드 리스트 인덱스 접근 메소드"""
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next
        return iterator
    
    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def find_node_with_data(self, data):
        """링크드 리스트에서 탐색 연산 메소드."""
        iterator = self.head
        while iterator is not None:
            if iterator.data == data:
                return iterator
            iterator = iterator.next
        return None

    def insert_after(self, previous_node, data):
        new_node = Node(data)
        """가장 마지막 순서 삽입"""
        if previous_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = previous_node.next
            previous_node.next = new_node
        
    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
            self.tail = new_node
            return
        head_node = self.head
        
        new_node.next = head_node
        self.head = new_node    

    def delete_after(self, previous_node):
        """링크드 리스트 뒷 노드 삭제"""
        data = previous_node.next.data

        # 지우려는 노드가 tail 노드 일 때
        if previous_node.next is self.tail:
            previous_node.next = None
        else:
            previous_node.next = previous_node.next.next
        return data

    def pop_left(self):
        """링크드 리스트의 가장 앞 노드 삭제 메소드. 단, 링크드 리스트에 항상 노드가 있다고 가정한다"""
        head_node = self.head
        data = self.head.data
        self.head = head_node.next
        if head_node.next == None:
            self.head = None
            self.tail = None
        else:
            head_node.next = None
        return data
    
    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str

# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

# 노드 순서대로 출력

print(my_list)

node_2 = my_list.find_node_at(2)
my_list.insert_after(node_2, 6)

head_node = my_list.head
my_list.insert_after(head_node, 9)

my_list.delete_after(head_node)

print(my_list)


