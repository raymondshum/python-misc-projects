from leetcode.utils.driver import Driver

class Solution:
    """Key Point: Use a stack to store opening brackets. Pop to compare them to 
    closing brackets.
    
    Link: https://leetcode.com/problems/valid-parentheses/
    
    Method: I chose to build a pattern dictionary to represent valid pairs of
    brackets. Opening brackets (dict keys) are push onto a stack. When a closing 
    bracket is encountered, the stack is popped. The value of dict[opening_bracket]
    is compared to the encountered closing bracket. If there is a mismatch, then
    the function returns False.

    Returns:
        bool: True if string contains brackets in correct order. False if not.
    """
    @staticmethod
    def isValid(s: str) -> bool:
        closing_parens = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        
        stack = []

        for parenthesis in s:
            if parenthesis in closing_parens.keys():
                stack.append(opening_parenthesis := parenthesis)
            else:
                # Edge Case: List contains more closing brackets than opening brackets.
                if len(stack) == 0:
                    return False
                
                last_opening_parenthesis = stack.pop(len(stack) - 1)
                valid_parenthesis = closing_parens[last_opening_parenthesis]
                
                if parenthesis != valid_parenthesis:
                    return False

        # Edge Case: List contains more opening brackets than closing brackets.
        return False if len(stack) > 0 else True
    
def main():
    input = {
        0: {
            "s":  "()",
        },
        1: {
            "s":  "()[]{}",
        },
        2: {
            "s":  "(]",
        },
        3: {
            "s": "{[]}",
        },
        4: {
            "s": "("
        },
        5: {
            "s": "(("
        },
        6: {
            "s": "]"
        }
    }
    output = [True, True, False, True, False, False, False]
    Driver.run_test_cases(Solution.isValid, input, output)

if __name__ == '__main__':
    main()