class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'(': ')', '[': ']', '{': '}'}
        control = []

        for i in s:
            if i in parentheses: # 1
                control.append(parentheses[i])
                # print(control)
                
            elif len(control) == 0: # 2
                return False
            elif control.pop() != i: # 3
                return False
        

        if len(control) == 0: # 4
            return True
        else:
            return False

