# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        visited = []
        def dfs(root,level):
            if root is None:
                return []
            if len(visited)<level+1:
                visited.append([])
            visited[level].append(root.val)
            if root.left:
                dfs(root.left,level+1)
            if root.right:
                dfs(root.right,level+1)
        dfs(root,0)
        return visited
