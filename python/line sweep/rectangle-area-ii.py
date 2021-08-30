#https://leetcode.com/problems/rectangle-area-ii/

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        
        def getArea(w: int) -> int:
            py = ans= 0
            for y1, y2 in intervals:
                py = max(py, y1)
                ans += max(0, y2 - py)
                py = max(py, y2)
            return ans * w
        
        OPEN, CLOSE = 0, 1
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, OPEN, y1, y2))
            events.append((x2, CLOSE, y1, y2))
        events.sort()
        
        intervals = []
        ans = px = 0
        for x, typ, y1, y2 in events:
            ans += getArea(x - px)

            if typ == OPEN:
                intervals.append((y1, y2))
                intervals.sort()
            else:
                intervals.remove((y1, y2))
            px = x
            
        return ans % (10**9 + 7)