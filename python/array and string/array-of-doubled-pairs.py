class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr= sorted(arr)
        d = defaultdict(int)
        for v in arr:
            if v != 0:
                d[v]+= 1
        
        for k, v in list(d.items()):
            if (d[k]> 0 and k*2 in d and d[k*2] >0):
                t= min(d[k*2], d[k])
                d[k*2] -= t
                d[k]-= t
        
        for k, v in d.items():
            if v:
                return False
        return True
