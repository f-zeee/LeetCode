class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        lp="("
        rp=")"
        lpc=0
        count=0
        for i in s:
            if rp == i and lpc==0:
                count+=1
            elif lp==i:
                lpc+=1
            elif rp==i and lpc>0:
                lpc-=1
        return abs(count+lpc)