class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        now = 1
        res = 0
        while n > 0:
            if n & 1 == 1:
                res |= 1 << 32 - now
            n >>= 1
            now += 1
        return res