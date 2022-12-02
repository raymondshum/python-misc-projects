class Utils:
    
    @staticmethod
    def read_file(file_path):
        with open(file_path, "r") as reader:
            return reader.readlines()
        
    @staticmethod
    def format_file_lines(file_lines):
        return [int(line.strip().replace("\n", "")) for line in file_lines]
    
    @staticmethod
    def strip_newline_symbol(file_lines):
        return [line.replace("\n", "") for line in file_lines]
    
    @staticmethod
    def load_input(file_path):
        input = Utils.read_file(file_path) 
        return Utils.strip_newline_symbol(input)