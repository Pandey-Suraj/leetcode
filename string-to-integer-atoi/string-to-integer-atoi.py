class Solution:
    def myAtoi(self, s: str) -> int:
        sign=1
        s=s.strip()
        if s=="": 
            return 0
        char=s[0]
        if char=="-" or char=="+":
            s=s[1:]
            if char=="-":
                sign=-1
        ans=0
        for ch in s:
            if '0'<=ch<='9':
                ans=ans*10+(int(ch))
            else:
                break
        ans = ans*sign     
        if ans<-2147483648:
            return -2147483648
        elif ans>2147483647:
            return 2147483647
        
        return ans
# class Solution:
#     def myAtoi(self, s: str) -> int:
#         s = ''.join(s.split())
#         print(s)    
        
#         l = []
#         for i in range(len(s)):
            
#             if s[0].isalpha():
#                 return 0
#             if s[i].isnumeric() or s[i] == '-' or s[i] == '+' or s[i] == '.':
#                 print(s[i])
#                 l.append(s[i])
#         print(l)
#         v = ''.join(l)
#         print(v)
#         y = float(v)
#         s = str(y)
        
#         output = -2**31
#         out = 2**31 - 1 
#         if s[0].isnumeric() or s[0] == '-' or s[0] == '+':
#             if s[0] == '-':
#                 task = int(float(s))
#                 if task < -2**31:
#                     return output
#                 else:
#                     return task
#             elif s[0] == '+':
#                 task = int(float(s))
#                 if task > 2**31 - 1:
#                     return out
#                 else:
#                     return task 
#             else: 
#                 task = int(float(s))
#                 return task
#         else:
#             return 0 

                    
                    
            
            
        