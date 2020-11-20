# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def recursion(root, p, q):
            if not root:
                return
            if p == root or q == root:
                return root
            lson = recursion(root.left, p, q)
            rson = recursion(root.right, p, q)
            if not rson:
                return lson
            if not lson:
                return rson
            return root

        return recursion(root, p, q)