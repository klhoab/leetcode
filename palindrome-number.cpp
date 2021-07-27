class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0) return false;
        int y= 0, x2= x;
        while (x2>0){
            y= y*10+ x2%10;
            x2/= 10;
        }
        return (x==y);
    }
};
