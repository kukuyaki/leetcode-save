class Solution(object):
    def countTriplets(self, arr):
        n=len(arr)
        def bior(string1):
            x=0
            for i in string1:
                x^=i
            return x
        count=0
        for i in range(0,n):
                for k in range(i+1,n):
                    if bior(arr[:i])^bior(arr[:k+1])==0:
                        count+=k-i
        return count

