# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack = []

        def help(root, count):
            if count!="":
                count+="->"
            count += str(root.val)
            
            if root.left:
                help(root.left, count)
            if root.right:
                help(root.right, count)
            if  not root.right  and not root.left:
                stack.append(count)        
        
        help(root, "")
        return stack