class Solution:
    def countAndSay(self, n: int) -> str:
        s='1'
        for _ in range(1,n):
            tmp=''
            i,j=0,0
            while j<len(s):
                while j<len(s) and s[i]==s[j]:
                    j+=1
                tmp+=str(j-i)+str(s[i])
                i=j
            s=tmp
        return s
        