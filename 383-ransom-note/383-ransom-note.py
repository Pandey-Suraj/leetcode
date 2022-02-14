class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = []
        m = []
        for i in ransomNote:
            r.append(i)
        for i in magazine:
            m.append(i)
        
        for i in r:
            print(i)
            if i in m:
                m.remove(i)
            else:
                return False
        return True
        print(r, m )