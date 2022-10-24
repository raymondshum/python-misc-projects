from scratchpad.advent.utils.utils import Utils

def main():
    file_path = r"input.txt" 
    file_lines = Utils.format_file_lines(Utils.read_file(file_path))
    
    count = 0
    
    for index, number in enumerate(file_lines[:-2]):
        if index == 0:
            prev_sum = number + file_lines[index + 1] + file_lines[index + 2]
        else:
            current_sum = prev_sum - file_lines[index - 1] + file_lines[index + 2]
            
            if current_sum > prev_sum:
                count += 1
            
            prev_sum = current_sum
    
    print(count)
if __name__ == '__main__':
    main()