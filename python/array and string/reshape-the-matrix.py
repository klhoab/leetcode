class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        ans = []
        temp = []
        cnt = 0
        for arr in mat:
            for item in arr:
                temp+= [item]
                cnt += 1
                if cnt == c:
                    cnt = 0
                    ans+= [temp]
                    temp = []
        return ans
        