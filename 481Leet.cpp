#include <iostream>
using namespace std;
class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int i=0;
        int tot=0;
        int ans=0;
        for(int j=0;j<size(s);j++){
            tot+=abs(s[j]-t[j]);
            while (tot>maxCost){
                tot-=abs(s[i]-t[i]);
                i++;
            }
            ans=max(ans,j-i+1);
        }
        return ans;
    }
};