class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for d in path.split('/'):
            if d == '.' or d == '':
                continue
            if d == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(d)

        return '/' + '/'.join(stack)
        # print(path.split('/'))
        