class Solution {
public:
    static bool isVowel(const char c2){
        char c= tolower(c2);
        return (c== 'a'|| c=='e'|| c=='i'|| c=='o'|| c=='u');
    }
    string reverseVowels(string s) {
        vector<int> v;
        for (int i=0; s[i]; i++){
            if (isVowel(s[i]))
                v.push_back(i);
        }
        int n= s.length();
        int t= v.size();
        for (int i=0; i<t/2; i++){
            swap(s[v[i]], s[v[t-1-i]]);
        }
        return s;
    }
};
