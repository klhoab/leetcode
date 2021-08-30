class Solution:
    def numberToWords(self, num: int) -> str:
        digits= ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven","Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        dic = {
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty', 
            50: 'Fifty', 
            60: 'Sixty', 
            70: "Seventy", 
            80: "Eighty", 
            90: "Ninety",
            100: 'Hundred',
            1000 : 'Thousand',
            1000000: 'Million',
            1000000000: 'Billion'
        }
        
        if num < 20:
            return digits[num]
        else:
            for key in reversed(dic.keys()):
                if (num >= key):
                    x = int(num/ key);
                    y = num % key;
                    if (key >= 100):
                        head = self.numberToWords(x) + " " + dic[key]
                    else:
                        head = dic[key] 
                    tail = (" " + self.numberToWords(y)) if y > 0 else ""
                    return (head + tail)
 