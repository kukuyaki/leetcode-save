class Solution(object):
    def scoreOfString(self, s):
        ans=0
        n=len(s)
        for i in range(0,n-1):
            ans+=abs(ord(s[i])-ord(s[i+1]))
        return ans
        
