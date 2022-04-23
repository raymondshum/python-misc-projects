from leetcode.utils.driver import Driver

class Solution:
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