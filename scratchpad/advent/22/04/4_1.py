from pprint import pprint
from scratchpad.advent.utils.utils import Utils

def get_formatted_input(input):
    formatted_input = []
    for line in input:
        first, second = line.strip().split(",")
        f_start, f_stop = first.split("-")
        s_start, s_stop = second.split("-")
        formatted_input.append([int(f_start), int(f_stop), int(s_start), int(s_stop)])
    return formatted_input

def get_contained_intervals(formatted_input):
    overlap = 0
    for index, line in enumerate(formatted_input):
        if (line[0] <= line[2] and line[1] >= line[3]):
            overlap += 1
            print(f"C1:  [{index}] ({line[0]}, {line[1]}) contains ({line[2]}, {line[3]})")
        elif (line[2] <= line[0] and line[3] >= line[1]):
            print(f"C2:  [{index}] ({line[2]}, {line[3]}) contains ({line[0]}, {line[1]})")
            overlap += 1
    print(overlap)

def get_any_overlapping_interval(formatted_input):
    overlap = 0
    
    for index, line in enumerate(formatted_input):
        if (line[0] >= line[2] and line[0] <= line[3]) or (line[1] >= line[2] and line[1] <= line[3]) \
            or (line[2] >= line[0] and line[2] <= line[1]) or (line[3] >= line[0] and line[3] <= line[1]):
            overlap += 1
    
    print(overlap)

def main():
    file_path = r'scratchpad\advent\22\04\input.txt'
    input = Utils.load_input(file_path)
    formatted_input = get_formatted_input(input)
    get_any_overlapping_interval(formatted_input)

    
    

if __name__ == '__main__':
    main()