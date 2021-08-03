class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int curr= 0, n = nums.size();
        for (int i=0; i<n; ++i){
            if (nums[i]!= 0){ 
                nums[curr]= nums[i];
                curr++;
            }
        }
        while (curr<n)
            nums[curr++]= 0;
    }
};
