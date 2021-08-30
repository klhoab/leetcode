class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-x for x in piles]
        heapify(piles)
        
        for i in range(k):
            t = heappop(piles) // 2
            heappush(piles, t)
        
        return -sum(piles)
        
