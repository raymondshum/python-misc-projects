import string
from pprint import pprint
from scratchpad.advent.utils.utils import Utils

def create_alphabet_dict():
    alphabet_list = list(string.ascii_letters)
    alphabet_dict = {letter: value + 1 for value, letter in enumerate(alphabet_list)}
    return alphabet_dict

def get_rucksack_halves(rucksack_contents):
    midpoint = len(rucksack_contents) // 2
    return [rucksack_contents[:midpoint], rucksack_contents[midpoint:]]

def get_common_item(first_compartment, second_compartment):
    return ''.join(set(first_compartment).intersection(second_compartment))

def get_item_priority(value_dict, item):
    return value_dict.get(item)

def get_all_priorities(alphabet_dict, rucksack_content_list):
    priorities = []
    for rucksack_contents in rucksack_content_list:
        first_compartment, second_compartment = get_rucksack_halves(rucksack_contents)
        common_item = get_common_item(first_compartment, second_compartment)
        priority = get_item_priority(alphabet_dict, common_item)
        priorities.append(priority)
    return priorities

def get_priorities_total(priorities_list):
    return sum(priorities_list)

def split_list(list, sublist_length):
    return [ list[x:x+sublist_length] for x in range(0, len(list), sublist_length)]

def get_common_item_in_group(rucksack_group):
    return ''.join(set(rucksack_group[0]).intersection(rucksack_group[1]).intersection(rucksack_group[2]))

def get_common_items_in_group_list(rucksack_group_list):
    common_item_list = []
    for rucksack_group in rucksack_group_list:
        common_item_list.append(get_common_item_in_group(rucksack_group))
    return common_item_list

def convert_common_item_list_to_priority_list(value_dict, common_item_list):
    return [value_dict.get(item) for item in common_item_list]
        
def main():
    alphabet_dict = create_alphabet_dict()
    
    file_path = r'scratchpad\advent\22\03\input.txt'
    input = Utils.load_input(file_path)
    input_list = split_list(input, 3)
    
    # Part 1
    priorities_list = get_all_priorities(alphabet_dict, input)
    priorities_total = get_priorities_total(priorities_list)
    print(f"P1: {priorities_total}\n")
    
    # Part 2
    common_item_list = (get_common_items_in_group_list(input_list))
    priorities_list = convert_common_item_list_to_priority_list(alphabet_dict, common_item_list)
    priorities_total = get_priorities_total(priorities_list)
    print(f"P2: {priorities_total}")
    
if __name__ == "__main__":
    main()