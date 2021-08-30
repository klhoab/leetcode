class Solution:
    def intToRoman(self, num: int) -> str:
        d= {'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000}
        
        ans = ""
        for k in reversed(d.keys()):
            while num - d[k] >= 0:
                ans += k
                num -= d[k]
        return ans