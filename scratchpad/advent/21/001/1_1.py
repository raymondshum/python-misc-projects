from scratchpad.advent.utils.utils import Utils


def get_num_increasing(file_lines):
    count = 0
    for index, number in enumerate(file_lines):
        if index == 0:
            continue
        if number > (prev_number := file_lines[index - 1]):
            count += 1
    return count

def main():
    file_path = r"input.txt"
    file_lines = Utils.format_file_lines(Utils.read_file(file_path))
    print(get_num_increasing(file_lines))
    # print(file_lines[1:])
    

if __name__ == '__main__':
    main()