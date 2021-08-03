class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> results= vector<int>(2);
        int l= nums.size();
        for (int i=0; i<l; i++)
            for (int j=i+1; j<l; j++)
                if (nums[i]+ nums[j] == target){
                    results[0] = i+1;
                    results[1] = j+1;
                    return results;
                }
    }
};
