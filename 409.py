from collections import defaultdict
dicL = defaultdict(int)
class Solution(object):
    def longestPalindrome(self, s):
        dicL.clear()
        for k in s:
            dicL[k]+=1
        ans=0
        odd=0
        for i in dicL:
            if dicL[i]%2:
                odd=1
                ans+=dicL[i]-1
            else:
                ans+=dicL[i]
            
        return ans+odd
