# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = ans = head 
        if ptr is None:
            return 
        while ptr and ptr.next:
            if ptr.val != ptr.next.val:
                ptr.val , ptr.next.val = ptr.next.val, ptr.val
            ptr = ptr.next.next
        return ans
            
        