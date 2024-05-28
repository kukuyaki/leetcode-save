class Solution(object):
    def findTheLongestSubstring(self, s):
        li1=[]
        for i in range(len(s)):
            for j in range(len(s)-i):
                ana=(s[i:len(s)-j].count("a")+1)%2
                ane=(s[i:len(s)-j].count("e")+1)%2
                ani=(s[i:len(s)-j].count("i")+1)%2
                ano=(s[i:len(s)-j].count("o")+1)%2
                anu=(s[i:len(s)-j].count("u")+1)%2
                if ana and ane and ani and ano and anu:
                    li1.append(s[i:len(s)-j])
        return len(max(li1,key=len))
        