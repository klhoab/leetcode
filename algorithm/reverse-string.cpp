class Solution {
public:
    string reverseString(string s) {
        string s2= s;
        reverse(s2.begin(), s2.end());
        return s2;
    }
};
