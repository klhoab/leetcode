class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = []
        for i in range(1, numRows+ 1):
            t = [1]* i if i <= 2 else [1]+ [a[i-2][j]+ a[i-2][j-1] for j in range(1, i-1)] + [1]
            a += [t]
        return a