# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root : 
            return 0
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))
        # def find_max(node):
        #     if not node : return 0
        #     left = 1 + find_max(node.left)
        #     right = 1 + find_max(node.right)
        #     return max(left,right)
        # return find_max(root)