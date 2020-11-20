class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        def queen(raw,cur,pie,na,cur_str):
            if raw == n:
                self.res.append(cur_str)
                return
            for i in range(n):
                if i in cur or i + raw in pie or i - raw in na:
                    continue
                queen(raw+1,cur+[i],pie+[i+raw],na+[i-raw],cur_str+['.'*i+'Q'+'.'*(n-i-1)])
        queen(0,[],[],[],[])
        return self.res