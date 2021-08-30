class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        mem= [[[0] * (n) for _ in range(n)] for _ in range(n)]
        
        def dp(i, j, k):
            if i> j:
                return 0
            if mem[i][j][k]:
                return mem[i][j][k]
            
            #Case 1: End current color 
            s= i
            while s <= j and boxes[i] == boxes[s]:
                s+= 1
            cnt = s - i
            ans = (k+ cnt) ** 2 + dp(s, j, 0)
            
            #Case 2: join to the next current color + dp(s,t-1,0)
            for t in range(s, j+1):
                if boxes[t]== boxes[i]:
                    ans = max(ans, dp(s, t-1, 0) + dp(t, j, k+ cnt))
                    #break  (fix case 52: cannot assume the first seen of same color is the correct join) 
            
            mem[i][j][k]= ans           
            return ans
        
        return dp(0, n-1, 0)
