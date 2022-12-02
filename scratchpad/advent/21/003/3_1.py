from copy import deepcopy
from scratchpad.advent.utils.utils import Utils
from statistics import mode, multimode
from pprint import pprint

def get_mode(input, index):
    column = [line[index] for line in input]
    modes = multimode(column)
    if len(modes) == 1:
        return modes[0]
    else:
        return '1'

def invert_binary_string(binary_string):
    inverted_string = ""
    for digit in binary_string:
        if digit == '1':
            inverted_string += '0'
        else:
            inverted_string += '1'
    return inverted_string

def get_most_common_bits(input):
    result = ""
    for index in range(len(input[0])):
        result += get_mode(input, index)
    return result

def binary_to_decimal(binary_string):
    result = 0
    for power, digit in enumerate(binary_string[::-1]):
        result += int(digit) * (2 ** power)
    return result

def get_rate(input, rate):
    mode = get_most_common_bits(input)
    
    if rate == "gamma":
        binary_string = mode
    else:
        binary_string = invert_binary_string(mode)
        
    return binary_to_decimal(binary_string)

def get_power_consumption(epsilon, gamma):
    return epsilon * gamma

def filter_list(input, rating_type):
    result = deepcopy(input)
    num_bits = len(input[0])
    for position in range(num_bits):
        mode = get_mode(result, position)
        
        if rating_type == 'oxygen':
            bit_criteria = mode
        else:
            bit_criteria = invert_bit(mode)
        
        result = list(filter(
            lambda string: 
                int(string[position]) == int(bit_criteria),
            result
        ))

        if len(result) == 1:
            break
        
    return result
    
            

def invert_bit(bit):
    return '0' if bit == '1' else 1

def main():
    file_path = r"input.txt"
    input = Utils.read_file(file_path) 
    input = [[*line.replace("\n", "")] for line in input]
    
    rates = {
        "gamma" : 0, 
        "epsilon": 0
    }
    
    for rate in rates:
        rates[rate] = get_rate(input, rate)
        print(f"{rate}: {rates.get(rate)}")
    
    print("power:", get_power_consumption(**rates), end="\n\n")
    
    rating_types = {
        'oxygen': 0,
        'c02': 0
    }
    
    for rating_type in rating_types:
        result = filter_list(input,rating_type)
        decimal = binary_to_decimal(result[0])
        rating_types[rating_type] = decimal
        print(f"{rating_type}: {decimal}")
    
    print("life support:", get_power_consumption(*rating_types.values()), end="\n\n")
        
    

if __name__ == '__main__':
    main()