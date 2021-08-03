class Solution {
public:
    static bool cmp_by_value(const pair<int,int>& l, const pair<int,int>& r) {  
        return l.second > r.second;  
    }
    
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> mp;
        vector<int> v;
        
        for (const auto &p: nums){
            mp[p]++;   
        }
        vector<pair<int,int> > val(mp.begin(), mp.end());  
        sort(val.begin(), val.end(), cmp_by_value);  
        
        for(int i=0; i<k; i++){
            v.push_back(val[i].first);
        }
        return v;
    }
};
