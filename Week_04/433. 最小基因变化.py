class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        possible = {
            'A':'CGT',
            'C':'AGT',
            'G':'ACT',
            'T':'ACG'
        }
        queue = [(start,0)]

        while queue:
            word,step = queue.pop(0)
            if word == end:
                return step
            for i,c in enumerate(word):
                for j in possible[c]:
                    tmp = word[:i] + j + word[i+1:]
                    if tmp in bank:
                        bank.remove(tmp)
                        queue.append((tmp,step+1))
        return -1