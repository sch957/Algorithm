class Node:
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.link:
                current = current.link
            current.link = new_node

    def display_list(self):
        current = self.head
        node_list = []
        while current:
            node_list.append(current.data)
            current = current.link
        return node_list
    
num_nodes = int(input("노드의 개수: "))
linked_list = LinkedList()

for i in range(1, num_nodes + 1):
    data = int(input(f"노드 #{i}의 데이터: "))
    linked_list.add_node(data)

print("리스트의 내용:", linked_list.display_list())