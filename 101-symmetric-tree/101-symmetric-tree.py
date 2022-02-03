# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def solve(r1,r2):
            if r1 is None and r2 is None:
                return True
            elif r1 is None or r2 is None:
                return False
            else:
                if r1.val != r2.val:
                    return False
                else:
                    return solve(r1.left,r2.right) and solve(r1.right,r2.left)
        return solve(root,root) 
        