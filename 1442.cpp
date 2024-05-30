using namespace std;
class Solution {
public:
    int pain(int p,vector<int> s){
        int tar=0;
        for(int i=0;i<p;i++){
            tar^=s[i];
        }
            return tar;
        };
    int countTriplets(vector<int>& arr) {
        int count=0;
        int n=size(arr);
        for(int i=0;i<n;i++){
            for(int k=i;k<n;k++){
                if (pain(i,arr)==pain(k+1,arr)){
                    count+=k-i;
                }
            }
        }
        return count;
    }
};