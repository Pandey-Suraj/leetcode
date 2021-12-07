from itertools import combinations,permutations
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # n = len(s)
        # lis = []
        # final = []
        # prem = permutations(words)
        # for i in list(prem):
        #     lis.append(i)
        # res = [''.join(tups) for tups in lis]
        # for i in res:
        #     if i in s:
        #         for j, ltr in enumerate(s):
        #             index = (s.find(i,j,n))
        #             if index != -1:
        #                  final.append(index)      
        # return(set(final))
        result = []
        origin, M, N = Counter(words), len(words[0]), len(s)
        L = len(words)
        for i in range( N - M*L  + 1):
            current = Counter(origin)
            flag = True
            for j in range(i, i + M*L, M):
                if not current[s[j:j+M]]: 
                    flag = False
                    break
                else:
                    current[s[j:j+M]] -= 1
            if flag : result.append(i)
        return result
                
        