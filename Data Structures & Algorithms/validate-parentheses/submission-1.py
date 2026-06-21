class Solution:
    def isValid(self, s: str) -> bool:
        # input: string to parse parentheses
        # output: bool showing validity

        # Approach: We want a stack to store and pop brackets
        stack = []
        open_bracket = ["(","{","["]
        mapping = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for i in range(len(s)):
            if s[i] in open_bracket:
                stack.append(s[i])
            else:
                # Closed bracket
                if len(stack) > 0:
                    complement = stack.pop()
                    if mapping[s[i]] != complement:
                        return False
                else:
                    return False
                    
        if len(stack) > 0:
            return False
        return True