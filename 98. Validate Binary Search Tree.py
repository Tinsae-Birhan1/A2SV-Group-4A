# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def help( node, left, right):
            if not node:
                return True
            if not(node.val < right and node.val > left):
                return False
            
            return(help(node.left, left, node.val) and help(node.right, node.val, right))
        
        return help(root, float("-inf"), float("inf"))