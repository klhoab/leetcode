class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int mx, mn, ans= 0;
        for(int i=0; i<nums.size(); ++i){
            if (i==0) mx= mn= ans= nums[i];
            else {
                int mx2, mn2;
                mx2= max(max(nums[i]*mn, nums[i]* mx), nums[i]);
                mn2= min(min(nums[i]*mx, nums[i]* mn), nums[i]);
                mx= mx2;
                mn= mn2;
            }
            ans = max(mx, ans);
        }
        return ans;
    }
};
