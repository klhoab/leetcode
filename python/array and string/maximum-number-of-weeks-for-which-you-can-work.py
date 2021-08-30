class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        hi = max(milestones)
        
        if hi*2 <= total:
            return total
        else:
            return (total - hi)*2 +1
