class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        head, tail = 0, n - 1

        for cnt in range(n):
            dx = abs(head - tail)
            dy = min(height[head], height[tail])
            if height[head] == dy:
                head += 1
            else:
                tail -= 1
            ans = max(ans, dx * dy)
        return ans
