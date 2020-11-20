# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def recursion(preorder_left,preorder_right,inorder_left,inorder_right):
            if preorder_left>preorder_right:
                return
            root = preorder[preorder_left]
            i = dic[root]
            p = TreeNode(root)
            tree_length = i - inorder_left
            p.left = recursion(preorder_left+1,preorder_left+tree_length,inorder_left,i-1)
            p.right = recursion(preorder_left+tree_length+1,preorder_right,i+1,inorder_right)
            return p

        n = len(preorder)
        dic = {k:j for j,k in enumerate(inorder)}
        return recursion(0,n-1,0,n-1)