class Solution {
public:
    bool isValid(string s) {
        
        stack<char> s2;
        
        for (int i=0;s[i];i++){
            if (s[i]=='(' || s[i]== '{' ||s[i]== '['){
                s2.push(s[i]);
            }
            else {
                if (s2.empty()) return false;
                else if ( (s[i]==')' && s2.top()=='(') || 
                     (s[i]==']' && s2.top()=='[') || 
                     (s[i]=='}' && s2.top()=='{') ){ 
                    s2.pop(); 
                }
                else
                    return false;
            }
        }
        return s2.empty();
    }
};
