# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        step1 = list1
        step2 = list2
        if step1 is None:
            return list2
        elif step2 is None:
            return list1
        if list1.val <= list2.val:
            new_list = ListNode(list1.val)
            step1 = step1.next
        else:
            new_list = ListNode(list2.val)
            step2 = step2.next
        current = new_list

        while step1 is not None and step2 is not None:
            if step1.val <= step2.val:
                current.next = step1
                current = current.next
                step1 = step1.next
            else:
                current.next = step2
                current = current.next
                step2 = step2.next
        
        
        if step1 is not None:
            current.next = step1
            
        if step2 is not None:
            current.next = step2
        return new_list



        

        