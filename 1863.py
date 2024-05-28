class Solution(object):
    def subsetXORSum(self, nums):
        ans=0
        n=len(nums)
        for i in range(1<<n):
            t=0
            for k in range(n):
                if i & 1<<k:
                    t^=nums[k]
            ans+=t
        return ans


        