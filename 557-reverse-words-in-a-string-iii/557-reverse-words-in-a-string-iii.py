class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        l =  []
        for i in words:
            n = i[::-1]
            l.append(n)
            
        return ' '.join(l)
        