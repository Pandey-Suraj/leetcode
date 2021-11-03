class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = min(strs,key = len) 
        if len(short) == 0: 
            return ''
        if len(strs) == 1: 
            return strs[0]
        for i in range(0,len(short)): 
            for j in strs : 
                if short[:i+1] != j[:i+1] : 
                    if i-1 > -1 :
                        return short[:i]
                    else :
                        return ''
                else : 
                    pass
        return short