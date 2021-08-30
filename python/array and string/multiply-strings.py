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
    
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return "0"
        num1 = num1[::-1]
        multi = len(num2) - 1
        ans2 = ""
        d = defaultdict(str)
        d[0]= "0"
        for x in num2:
            carry = 0
            ans = ""
            
            #add memorization
            if x not in d:
                for y in num1:
                    t = (int)(x) * (int)(y) + carry
                    carry = t//10
                    t %= 10
                    ans = ans + (str)(t) 
                if carry:
                    ans = ans + (str)(carry)
                d[x] = ans
            
            ans = d[x]
            ans = ans[::-1] + "0"* multi
            if x: ans2 = self.addStrings(ans2, ans)
            multi-= 1
        return ans2
    
