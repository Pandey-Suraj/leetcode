# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         curr = head 
#         count = 1
#         while head:
#             count += 1 
#             head = head.next

#         pop = count - n 
#         demo = 0 
#         curr = head 
#         while curr:
#             demo += 1
#             if demo == pop:
#                 curr.next = curr.next.next
#             curr = curr.next
        
#         return head

            ptr, length = head, 0
            while ptr:
                ptr, length = ptr.next, length + 1
            if length == n : return head.next
            ptr = head
            for i in range(1, length - n):
                ptr = ptr.next
            ptr.next = ptr.next.next
            return head
        