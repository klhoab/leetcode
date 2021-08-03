class Solution {
public:
    int reverse(int x) {
        int s = 1;
        
        long long t= 2147483648;
        if (x<= -t || x> t-1) {
            return 0;
        }
        
        if (x<0) {
            x = -x;
            s = -1;
        }
        
        long long int a = 0;
        while (x>0){
            a = a*10+ x%10;
            
            x/=10;
        }
        a*=s; 
        if (a<= -t || a> t-1) {
            return 0;
        }
        else
            return a;
    }
};
