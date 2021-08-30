#https://leetcode.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3 or arr[1] < arr[0]:
            return False
        
        turn = 0
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                return False
            elif turn == 0 and arr[i] > arr[i-1] or (turn == 1 and arr[i] < arr[i-1]):
                continue
            else:
                turn += 1
            
        return turn == 1