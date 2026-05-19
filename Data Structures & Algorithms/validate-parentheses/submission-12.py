class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for key in s:
            if key in closeToOpen:
                if stack and stack[-1] == closeToOpen[key]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(key)

        return True if not stack else False

        # if (', '{', '[' exists, then add to stack
        # for it to be in same order... return whether if  ')', '}', ']' 
        # match with the top level of the stack

