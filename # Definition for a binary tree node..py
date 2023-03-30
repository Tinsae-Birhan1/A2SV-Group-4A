# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        def help( root):
            if not root:
                return 
            
            help(root.left)
            stack.append(root.val)
            help(root.right)
        help(root)
        return stack

