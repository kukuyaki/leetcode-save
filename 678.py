class Solution(object):
    def checkValidString(self, s):
        li1=list(s)
        #從左到右遇到左括號的時候把該左括號以及該左括號後的一個右括號去掉
        for i in range(len(li1)):
            if li1[i]=="(":
                for j in range(i,len(li1)):
                    if li1[j]==")":
                        li1[i]=""
                        li1[j]=""
                        break
        #從左到右
        #遇到右括號時，從該右括號往左找*字號，如果有的話把該右括號和該*字號去掉
        #遇到左括號時，從該左括號往右找*字號，如果有的話把該左括號和該*字號去掉
        for i in range(len(li1)):
            if li1[i]=="(":
                for j in range(i,len(li1)):
                    if li1[j]=="*":
                        li1[i]=""
                        li1[j]=""
            elif li1[i]==")":
                for j in range(i,0,-1):
                    if li1[j]=="*":
                        li1[i]=""
                        li1[j]=""
                        break
        #如果第一個為右括號或最後一個為左括號，false
        if li1[0]==")" or li1[-1]=="(":
            return 0
        return 1
        