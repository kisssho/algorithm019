class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res_list = []
        self.generate(n,1,0,0,'')
        return self.res_list

    def generate(self,n,level,left,right,res):
        if level>2*n:
            self.res_list.append(res)
        if left<n:
            self.generate(n,level+1,left+1,right,res+'(')
        if right<left:
            self.generate(n,level+1,left,right+1,res+')')