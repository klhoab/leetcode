class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        tail = [] 
        ans = []
        length = 0
        
        for ob in obstacles:
            k = bisect_right(tail, ob)
            if (k >= length):
                tail.append(ob)
                length+= 1
            else:
                tail[k] = ob
            ans.append(k+1)
        
        return ans
