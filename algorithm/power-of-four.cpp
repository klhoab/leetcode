class Solution {
public:
    bool isPowerOfFour(int num) {
        while (num>= 4){
            if (num%4 == 0)
                num/=4;
            else return false;
        }
        return (num==1);
    }
};
