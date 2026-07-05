class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1=len(s)
        n2=len(t)
        s,t=sorted(s),sorted(t)
        if(n1!=n2):
            return False
        else:
            for i in range(0,n1):
                if(s[i]!=t[i]):
                    return False
                
        return True