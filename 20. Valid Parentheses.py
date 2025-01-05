class Solution:
    def isValid(self, s):
        characters = {"(": ")",  "[": "]", "{": "}"}
        stack = []
        for i in s:
            if i in characters:
                stack.append(i)
            elif len(stack) == 0 or characters[stack.pop()] != i:
                return False
        return len(stack) == 0
