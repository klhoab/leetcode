class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> v;
        for (int i=0; i<=num; i++){
            int n= i, c= 0;
            while (n> 0){
                c+= n%2;
                n/= 2;
            }
            v.push_back(c);
        }
        return v;
    }
};
