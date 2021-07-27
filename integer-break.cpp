class Solution {
public:
    int integerBreak(int n) {
        if (n==2) return 1;
        if (n==3) return 2;
        if (n==4) return 4;
        
        long long int ans = 1;
        while (n>= 5){
            n-= 3; ans*= 3;
        }
        ans *= n;
        return ans;
    }
};
