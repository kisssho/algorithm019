# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        WHITE = 1
        GREY = 0
        stack = [(WHITE,root)]
        res = []
        while stack:
            color,node = stack.pop()
            if not node:
                continue
            if color==WHITE:
                stack.append((WHITE,node.right))
                stack.append((GREY,node))
                stack.append((WHITE,node.left))
            else:
                res.append(node.val)
        return res