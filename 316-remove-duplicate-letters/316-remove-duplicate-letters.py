class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
#         res = []
#         minimum = s[0]
#         for i in range(len(s)):
#             if s[i] not in res:
#                 res.append(s[i])
#                 if s[i] < minimum:
#                            minimum = (s[i])
            
#             else:
#                    smallestIndex = res.index(minimum)
#                    currentIntegerIndex = res.index(s[i])
#                    if currentIntegerIndex < smallestIndex:
#                            res.pop(currentIntegerIndex)
#                            res.append(s[i])
#                    else:
#                            continue
#         return ''.join(res)            
        stack = []
        for idx, character in enumerate(s):
            if not stack:
                stack.append(character)
            elif character in stack:
                continue
            else:
                while stack and (character < stack[-1]):
                    if stack[-1] in s[idx + 1:]:
                        _ = stack.pop()
                    else:
                        break
                        
                stack.append(character)
                
        return ''.join(stack)
                           
                
        