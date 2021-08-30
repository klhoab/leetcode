#https://leetcode.com/problems/complex-number-multiplication/

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        x1, y1 = [ int(x) for x in num1[:-1].split('+')]
        x2, y2 = [ int(x) for x in num2[:-1].split('+')]
        return str(x1* x2 - y1* y2) + "+" + str(x1* y2 + x2* y1) + "i"
        