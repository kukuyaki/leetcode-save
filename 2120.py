# def move(matrix,sPinDef,i,s):
#     dic={"L":-1,"R":1,"U":-1,"D":1}
#     t=0
#     for w in s[i:]:
#         if w in "LR":
#             t+=1
#             sPinDef[1]+=int(dic[w])
#         elif w in "UD":
#             t+=1
#             sPinDef[0]+=int(dic[w])
#         if sPinDef[0]>matrix-1 or sPinDef[0]<0 or sPinDef[1]>matrix-1 or sPinDef[1]<0:
#             return t-1
# matrix=3
# startP=[0,1]
# sP=startP.copy()
# s="RRDDLU"
# li1=[0 for _ in range(len(s))]
# for i in range(len(s)):
#     li1[i]=move(matrix,startP,i,s)
#     startP=sP.copy()
# print(li1)
class Solution(object):
    def executeInstructions(self, n, startPos, s):
        sP=list(startPos)
        dic={"L":-1,"R":1,"U":-1,"D":1}
        li1=[0 for _ in range(len(s))]
        for i in range(len(s)):
            t=0
            for w in s[i:]:
                if w in "LR":
                    t+=1
                    startPos[1]+=int(dic[w])
                elif w in "UD":
                    t+=1
                    startPos[0]+=int(dic[w])
                li1[i]=t
                if startPos[0]>n-1 or startPos[0]<0 or startPos[1]>n-1 or startPos[1]<0:
                    li1[i]=t-1
                    break
            startPos=list(sP)
        return li1
x=Solution()

print(x.executeInstructions(2,[0,0],"RDLU"))