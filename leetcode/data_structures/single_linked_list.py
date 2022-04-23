from leetcode.problems.utils.data_structures.list_node import ListNode

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def add_node(self, value):
        if not self.head:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.tail.next = ListNode(value)
            self.tail = self.tail.next
        self.length += 1
    
    @staticmethod
    def print_list(head):
        current_node = head
        print("[", end="")
        while current_node:
            print(current_node.val, end=", " if current_node.next else "")
            current_node = current_node.next
        print("]", end="")