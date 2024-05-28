class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        int ans = 0;
        int n = size(nums);
        for(int i=0;i<(1<<n);i++){
            int c=0;
            for(int k=0;k<n;k++){
                if (i & 1<<k){c^=nums[k];}
            }
            ans+=c;
        }
        return ans;
    }
};