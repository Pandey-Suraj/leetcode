# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #list is used as stack
        stk=[]#list
        #last in first out
        
        temp=head
        while(temp!=None):
            stk.append(temp)
            temp=temp.next
        
        while(head!=None):
            if(stk.pop().val!=head.val):
                return False
            head=head.next
        return True