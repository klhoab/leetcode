class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        t = ""
        for v in words:
            t = t+ v
            if t == s:
                return True
        return False
    
