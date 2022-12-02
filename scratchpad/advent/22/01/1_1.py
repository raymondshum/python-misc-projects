from scratchpad.advent.utils.utils import Utils
from pprint import pprint

def get_max_calories(input):
    max_calories = 0
    current_total = 0
    
    for line in input:

        if line != '':
            current_total += int(line)
        else:
            max_calories = max(max_calories, current_total)
            current_total = 0
    
    return max_calories

def get_calories_list(input):
    calories_list = []
    running_total = 0
    
    for line in input:
        if line != '':
            running_total += int(line)
        else:
            calories_list.append(running_total)
            running_total = 0
    
    if running_total > 0:
        calories_list.append(running_total)
    
    return calories_list

def get_top_x_total(list, top_num):
    list.sort(reverse=True)
    return sum(list[:top_num])
            

def main():
    # Part 1
    file_path = r'input.txt'
    input = Utils.load_input(file_path)
    result = get_max_calories(input)
    print(f"Max calories: {result}")
    
    # Part 2
    input = Utils.load_input(file_path)
    result = get_calories_list(input)
    result = get_top_x_total(result, 3)
    print(f"Top 3 calories (total): {result}")
    
    
if __name__ == "__main__":
    main()