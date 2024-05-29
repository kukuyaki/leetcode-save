class Solution(object):
    def numSteps(self, s):
        s=int(str("0b"+s),2)
        count=0
        while s!=1:
            count+=1
            if s%2:
                s+=1
            else:
                s/=2
        return  count
