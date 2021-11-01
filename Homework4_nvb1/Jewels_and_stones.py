class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        res=0
        for i in jewels:
            for j in stones:
                if i in j:
                    res+=1
        return res
