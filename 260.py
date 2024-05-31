class Solution(object):
    def singleNumber(self, nums):
        k=0
        w=[0,0]
        for i in nums:
            k^=i
        k=k & -k
        for i in nums:
            if (i & k)==0:
                w[0]^=i
            else:
                w[1]^=i
        return w
        
                



        
