class Solution(object):
    def singleNumber(self, nums):
        k=[]
        for i in range(len(nums)):
            if nums[i] not in nums[:i]+nums[i+1:]:
                k.append(nums[i])
        return k
                



        