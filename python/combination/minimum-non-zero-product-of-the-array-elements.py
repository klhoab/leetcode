#https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        m= 10**9 + 7
        return (pow(2**p-2, 2**(p-1)-1, m) * (2**p - 1) % m ) %m