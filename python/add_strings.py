class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = max(len(num1), len(num2))
        num1= (num1.rjust(n, '0'))[::-1]
        num2= (num2.rjust(n, '0'))[::-1]
        
        carry = 0
        ans = ""
        for i in range(n):
            t = (int)(num1[i]) + (int)(num2[i]) + carry
            carry = t//10
            t %= 10
            ans = ans + (str)(t)

        if carry:
            ans = ans + "1"
        return ans[::-1]
