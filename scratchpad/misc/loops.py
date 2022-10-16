def loops(string: str, multiplier: int = 0, left_index = 0) -> str:
    while find_first_index(string, "[") != -1:
        # Find indicies
        left_bracket_index: int = find_first_index(string, "[")
        right_bracket_index: int = find_end_index(string, left_bracket_index)
        first_substring_letter_index: int = left_bracket_index + 1
        multiplier_index:int  = right_bracket_index + 1
        next_letter_index = right_bracket_index + 2
        
        # Perform substring replacement
        multiplier = int(string[multiplier_index])
        substring: str = string[left_bracket_index: next_letter_index]
        expanded_string: str  = multiplier * string[first_substring_letter_index: right_bracket_index]
        string: str = string.replace(substring, expanded_string)
    return string
        
def find_first_index(string: str, character: str) -> int:
    try:
        index = string.index(character)
    except ValueError:
        index = -1
    return index

def find_end_index(string: str, start: int) -> int:
    stack = [string[start]]
    index = start
    while stack:
        index += 1
        char = string[index]
        if char == "]":
            stack.pop(len(stack) - 1)
        elif char == "[":
            stack.append(char)
    return index

print(loops('abcde[fgh]3ijkl'))  # OUTPUT > abcdefghfghfghijkl
print(loops('abcde[f[g]4h]3ijkl'))  #DESIRED OUTPUT > abcdefgggghfgggghfgggghijkl