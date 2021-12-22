class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mydict = {'I':1, 'V':5, 'X':10 , 'L':50, 'C':100, 'D':500, 'M':1000}
        finalnum = 0
        for i in range(len(s)-1):
            if mydict[s[i]] < mydict[s[i+1]]:
                finalnum -= mydict[s[i]]
            else:
                finalnum += mydict[s[i]]
        finalnum += mydict[s[-1]]
        return finalnum