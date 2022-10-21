""" !! Modify header attributes in this cell !! """

COMMENT_SYMBOL = ";"     # Single line comment symbol
HEADER_SIDE_WIDTH = 2    # Number of comments on left and right side
BUFFER_SIZE = 2          # Min space between text and sides of header
COLUMN_LIMIT = 78        # Max line length
TAB_SPACES = 4           # Spaces per tab character

HEADINGS = [
    "DESC: ",
    "DUE DATE: ",
]

COMMENT_BLOCK_HEADER = True

def get_total_line_length(line):
    if not COMMENT_BLOCK_HEADER:
        return (HEADER_SIDE_WIDTH * 2) + (BUFFER_SIZE * 2) + len(line)
    else:
        return len(line) + TAB_SPACES

def validate_answer(answer):
    total_line_length = get_total_line_length(answer)
    print(f"Line length: {total_line_length} | Column Limit: {COLUMN_LIMIT}")
    return total_line_length <= COLUMN_LIMIT

def get_user_input():
    user_input = []

    for heading in HEADINGS:
        valid_answer = False
        while not valid_answer:
            answer = heading + input(heading).strip()
            valid_answer = validate_answer(answer)
            print(f'{"PASSED" if valid_answer else "FAILED"} validation.', end="\n\n")
        user_input.append(answer)

    return user_input

def generate_single_line_header(user_input):
    left_border = HEADER_SIDE_WIDTH * COMMENT_SYMBOL + BUFFER_SIZE * " "
    right_border = BUFFER_SIZE * " " + HEADER_SIDE_WIDTH * COMMENT_SYMBOL

    print(COLUMN_LIMIT * COMMENT_SYMBOL)
    for input in user_input:
      num_spaces = COLUMN_LIMIT - get_total_line_length(input)
      print(f'{left_border}{input}{num_spaces * " "}{right_border}')
    print(COLUMN_LIMIT * COMMENT_SYMBOL)

def generate_comment_block_header(user_input):
    spaces = " " * TAB_SPACES
    print("comment !")
    for input in user_input:
        print(f"{spaces}{input}")
    print("!")

def main():
    user_input = get_user_input()
    if not COMMENT_BLOCK_HEADER:
        generate_single_line_header(user_input=user_input)
    else:
        generate_comment_block_header(user_input=user_input)
if __name__ == "__main__":
    main()