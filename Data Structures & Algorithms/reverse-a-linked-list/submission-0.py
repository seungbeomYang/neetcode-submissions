# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        point_e = head
        step = 0
        step_count =0
        if head == None:
            return head
        while point_e.next != None:
            step_count += 1
            point_e = point_e.next
        step = 0
        print("step_count:",step_count)
        
        new_list = ListNode(point_e.val)
        new_pointer = new_list
        step_count-=1
        

       
        while step_count >= 0:
            step = 0
            point_e = head
            while point_e.next != None and step < step_count:
                point_e = point_e.next
                step += 1
            step_count = step-1
            new_pointer.next = ListNode(point_e.val)
            new_pointer = new_pointer.next
           
        return new_list