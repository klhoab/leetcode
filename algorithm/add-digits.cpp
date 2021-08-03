class Solution {
public:
    int addDigits(int num) {
        if (num< 10)
            return num;
        
        int a= 0;
        while (num>=10){
            a+= num%10;
            num/=10;
        }
        a+= num;
        return addDigits(a);
    }
};
