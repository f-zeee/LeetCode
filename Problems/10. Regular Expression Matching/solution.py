class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        try:
            if(re.match(p,s).end()==len(s)):
                return True
            else:
                return False
        except:
            return False