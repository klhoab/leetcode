class Solution {
public:
    int myAtoi(string str) {
        int n= str.length();
        long long int c= 0; int s= 1;
        int i= 0;
        
        while (str[i] && str[i]==' ') i++;
        
        if (str[i] && (str[i]=='-' || str[i]=='+') ){
            if (str[i]== '-') s= -1;
            i++;
        }
        while (str[i] && (str[i]>='0' && str[i]<='9')){
            c= c*10+ str[i]- '0';
            i++;
            if (c*s>= INT_MAX) 
                return INT_MAX;
            if (c*s<= INT_MIN)
                return INT_MIN;
        }
        
        c*= s;
        return c;
    }
};
