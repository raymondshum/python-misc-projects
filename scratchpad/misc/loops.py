def loops(string: str, multiplier: int = 0, left_index = 0) -> str:
    while find_first_index(string, "[") != -1:
        start = find_first_index(string, "[")
        end = find_end_index(string, start)
        multiplier = int(string[end + 1])
        substring = string[start:end+2]
        expanded_string = multiplier * string[start + 1: end]
        string = string.replace(substring, expanded_string)
    return string
        
def find_first_index(string: str, character: str) -> int:
    try:
        index = string.index(character)
    except ValueError:
        index = -1
    return index

def find_end_index(string: str, start: int):
    stack = ["["]
    for index, char in enumerate(string[start + 1:]):
        if char == "]":
            stack.pop(len(stack) - 1)
            if not stack:
                return start + index + 1
        elif char == "[":
            stack.append("[")
    

print(loops('abcde[fgh]3ijkl'))  # OUTPUT > abcdefghfghfghijkl
print(loops('abcde[f[g]4h]3ijkl'))  #DESIRED OUTPUT > abcdefgggghfgggghfgggghijkl