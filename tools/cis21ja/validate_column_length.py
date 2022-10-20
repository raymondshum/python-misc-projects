FILE_PATH = r"C:\Users\rshum\Documents\De Anza\CIS 21JA\Projects\Project32_VS2017\assignment_3.asm"
MAX_COLUMN_WIDTH = 80

def read_file(file_path):
    with open(file_path, 'r') as reader:
        lines = reader.readlines()
    return lines

def format_lines(lines):
    return [line.replace("\t","    ").replace("\n","") for line in lines]

def visualize_file(lines):
    line_number = "L#"
    character_count = "C#"
    
    print(f'{line_number: <4}{character_count: <3}{"":=<80}')
    
    for index, line in enumerate(lines):
        line = line.replace("\t","    ")
        line = line.replace("\n","")
        print(f'{index+1: <4}{len(line): <3}{line}')

def audit_file(lines, max_column_width):
    return [(index+1, line) for index, line in enumerate(lines) if len(line) > max_column_width]

def display_audit(violations):
    line_number = "L#"
    character_count = "C#"
    
    print(f"{'    AUDIT REPORT    ':=^87}")
    if not violations:
        print("All lines passed.")
        return
    
    print(f'{line_number: <4}{character_count: <3}{"":=<80}')
    for index, line in violations:
        print(f'{index+1: <4}{len(line): <3}{line}')

def main():
    lines = read_file(FILE_PATH)
    lines = format_lines(lines)
    visualize_file(lines)
    violations = audit_file(lines, MAX_COLUMN_WIDTH)
    print("")
    display_audit(violations)

if __name__ == "__main__":
    main()