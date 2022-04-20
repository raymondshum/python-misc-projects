from leetcode.problems.utils.data_structures.list_node import ListNode
from leetcode.problems.utils.data_structures.single_linked_list import SingleLinkedList
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Edge case: One list is finished and the other is incomplete
        if not list1 or not list2:
            return list1 or list2

        # return the smaller of either list
        # recursive function call determines the next pointer
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
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

if __name__ == '__main__':
    main()