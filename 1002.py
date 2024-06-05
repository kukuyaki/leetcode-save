class Solution(object):
    def commonChars(self, words):
        ans=[]
        for w in max(words):
            t=1
            for k in range(len(words)):
                if w not in words[k]:
                    t=0
                    break
                words[k]=words[k].replace(w,"",1)
            if t:
                ans.append(w)
        return ans
                
