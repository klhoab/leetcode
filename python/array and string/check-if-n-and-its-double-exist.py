#https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d= set()
        for k in arr:
            x = k * 2
            y = k // 2  
            if x in d or (k%2== 0 and y in d):
                return True
            else:
                d.add(k)
        return False