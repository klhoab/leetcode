class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> v;
        set<int> st;
        for(auto it= nums1.begin(); it!= nums1.end(); it++){
            st.insert(*it);
        }
        for(auto it= nums2.begin(); it!= nums2.end(); it++){
            set<int>::iterator msit= st.find(*it);
            if (msit!= st.end()){
                v.push_back(*it);
                st.erase(msit);
            }
        }
        return v;
        
    }
};
