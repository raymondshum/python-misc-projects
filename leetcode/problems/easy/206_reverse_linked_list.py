from leetcode.data_structures.list_node import ListNode
from leetcode.data_structures.single_linked_list import SingleLinkedList
from typing import Optional
        
class Solution:
    """Key Point: Current, next and prev hold the structure of the linked list as you are
    reversing the direction of the pointers.
    
    Link: https://leetcode.com/problems/reverse-linked-list/
    
    Method: Current, next and prev hold the structure of the linked list as you are
    reversing the direction of the pointers.

    Returns:
        ListNode: Head of the reversed linked list.
    """
    @staticmethod
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        current = head
        next = None
        prev = None
        
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        return prev
    
def main():
    input = {
        0: {
            "head": [1,2,3,4,5]
        },
        1: {
            "head": [1,2]
        },
        2: {
            "head": []
        },
    }
    output = [
        [5,4,3,2,1],
        [2,1],
        []
    ]

    # Using custom test driver
    for key, test_case in input.items():
        my_list = SingleLinkedList()
        
        for value in test_case["head"]:
            my_list.add_node(value)
            
        print("Input:", end=" ")
        SingleLinkedList.print_list(my_list.head)
        
        print(" | Output: ", end="")
        SingleLinkedList.print_list(Solution.reverseList(my_list.head))
        print()
    
if __name__ == '__main__':
    main() 