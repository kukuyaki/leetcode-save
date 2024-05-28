class Solution(object):
    def magicalString(self, n):
        if n==1 or n==2 or n==3:
            return 1
        s="122"
        i=2
        while i<n:
            for _ in range(int(s[i])):
                if i%2:
                    s+="2"
                else:
                    s+="1"
            i+=1
        return s[:-3].count("1")