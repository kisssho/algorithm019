# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.depth(root)

    def depth(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        else:
            return 1+max(self.depth(root.left),self.depth(root.right))