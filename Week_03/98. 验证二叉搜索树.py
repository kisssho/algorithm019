# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.last = None
        self.flag = True
        self.inorder(root)
        return self.flag

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            if root.val <= self.last:
                self.flag = False
            self.last = root.val
            self.inorder(root.right)