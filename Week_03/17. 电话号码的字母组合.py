class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dic = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        res = []
        s = ''
        def recursion(level,dic,digits,s):
            if level==len(digits):
                res.append(s[:])
                return
            for i in dic[int(digits[level])]:
                s += i
                recursion(level+1,dic,digits,s)
                s = s[:len(s)-1]

        recursion(0,dic,digits,s)
        return res