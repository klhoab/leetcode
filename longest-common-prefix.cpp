class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        int m = 0;
        
        string ans= "";
        
        for(int i=0;i<n;i++){
            m = max(m, (int)(strs[i].length()));
        }
        
        for (int j=0;j<m;j++){
            for(int i=1;i<n;i++){
                if (strs[i][j]!= strs[0][j]){
                    return ans;
                }
            }
            ans+= strs[0][j];
        }
        
        return ans;
    }
};
