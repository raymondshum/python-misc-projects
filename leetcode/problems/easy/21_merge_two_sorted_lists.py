from leetcode.data_structures.list_node import ListNode
from leetcode.data_structures.single_linked_list import SingleLinkedList
from typing import Optional

class Solution:
    """Key Point: Account for ragged edges (uneven lists).
    
    Link: https://leetcode.com/problems/merge-two-sorted-lists/
    
    Method: Most of the logic is used to account for uneven lists. If
    either list is missing, the remaining is immediately returned. This
    method recursively compares each node from one list against the 
    other. The until the base case (at least one null list) is reached. At
    each method call, the smaller of either node (or node from list1 if
    equal) is ultimately returned.

    Returns:
        ListNode: Head of merged List.
    """
    @staticmethod
    def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: One list is finished and the other is incomplete
        if not list1 or not list2:
            return list1 or list2

        # return the smaller of either list
        # recursive function call determines the next pointer
        if list1.val <= list2.val:
            list1.next = Solution.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = Solution.mergeTwoLists(list1, list2.next)
            return list2
        
def main():
    input = {
        0: {
            "list1": [1,2,4], 
            "list2": [1,3,4]
        },
        1: {
            "list1": [], 
            "list2": []
        },
        2: {
            "list1": [], 
            "list2": [0]
        },
    }
    output = [
        [1,1,2,3,4,4],
        [],
        [0]
    ]
    
    for key, test_case in input.items():
        
        print("Input: ", end="")
        for list in test_case.values():
            my_list = SingleLinkedList()
            for value in list:
                my_list.add_node(value)
            SingleLinkedList.print_list(my_list.head)
        print("")
        
    for test_case in input.values():
        l1 = SingleLinkedList()
        l2 = SingleLinkedList()
        
        for value in test_case['list1']:
            l1.add_node(value)
        
        for value in test_case['list2']:
            l2.add_node(value)
            
        print("Output: ", end="")
        head = Solution.mergeTwoLists(l1.head, l2.head)
        SingleLinkedList.print_list(head)
        print("")
        


if __name__ == '__main__':
    main()