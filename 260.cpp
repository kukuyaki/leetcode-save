class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int k=0;
        for(int i=0;i<size(nums);i++){
            k^=nums[i];
        }
        unsigned int p=k & -(unsigned int)k;
        vector<int> w(2,0);

        for(int i=0;i<size(nums);i++){
            if (p & nums[i]){
                w[0]^=nums[i];
            }
            else{
                w[1]^=nums[i];
            }
        }
        return w;
    }
};
