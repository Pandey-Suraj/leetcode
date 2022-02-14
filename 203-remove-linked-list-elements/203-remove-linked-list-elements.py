# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # cur = ListNode(-1)
        # cur.next = head
        # curr = cur
        # while curr.next != None:
        #     if curr.next.val == val:
        #         curr.next = curr.next.next
        #     else:
        #         curr = curr.next
        # return curr.next
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        return dummy_head.next
    