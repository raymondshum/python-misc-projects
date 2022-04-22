import os
from typing import List, TextIO, Tuple

class ReadmeGenerator:
    
    DELIMITER = "\"\"\""
    
    def __init__(self):
        self.target_directories = []
        self.markdown_master_document = ""
    
    def add_directory(self, directory_path: str):
        if not self._directory_is_valid(directory_path):
            raise Exception(f"Directory does not exist: {directory_path}")
        
        self.target_directories.append(directory_path)
    
    def _directory_is_valid(self, directory_path: str) -> bool:
        return os.path.isdir(directory_path)
    
    def read_py_file(self, file_path: str):
        if not self._file_is_valid(file_path):
            raise Exception("File does not exist: {file_path}")
        
        raw_text = self._extract_text(file_path)
        processed_text = self._format_list_to_text(raw_text)
        return (content_dictionary := self._build_content_dictionary(processed_text, file_path))

    def _build_content_dictionary(self, processed_text: str, file_path: str) -> dict[str, str]:
        content = {}
        content["File Name"] = file_path.rsplit("\\", 1)[1]
        processed_text = processed_text.replace("Key Point: ", "")
        content["Key Point"],processed_text =processed_text.split("Link: ", 1)
        content["Link"],processed_text =processed_text.split("Method: ", 1)
        content["Method"], content["Returns"] = processed_text.split("Returns: ")
        return content
    
    def _extract_text(self, file_path: str) -> List[str]:
        delimiter_read = False
        extracted_text = []
        
        with open(file_path) as file_pointer:
            for line in file_pointer:
                if self.DELIMITER in line:
                    if delimiter_read:
                        break
                    else:
                        delimiter_read = True
                if delimiter_read and (stripped_line := line.strip()):
                    extracted_text.append(stripped_line)
                    
        return extracted_text
    
    def _format_list_to_text(self, raw_text: List[str]) -> str:
        extracted_text = " ".join(raw_text)
        return extracted_text.replace(self.DELIMITER, "")
    
    def _file_is_valid(self, file_path: str) -> bool:
        return os.path.isfile(file_path)
    
    def write_readme(self, formatted_text: str):
        pass
    
    def _format_dictionary_to_markdown(self, content_dictionary: dict) -> str:
        markdown = f"# {content_dictionary['File Name']}\n\n"
        for key, value in content_dictionary.items():
            markdown += f"**{key}**: {value}\n\n"
        markdown += "---\n\n"
        return markdown
    
    def _append_markdown(self, markdown_snippet: str):
        self.markdown_master_document += markdown_snippet
    
    
def main():
    # for root, dirs, files in os.walk(test.ROOT_DIRECTORY):
    #     for file in files:
    #         print(os.path.join(root, file))
    test = ReadmeGenerator()
    file_path = "C:\\Users\\rshum\\Documents\\CSUMB\\Misc Projects\\python\\leetcode\\problems\\easy\\1_two_sum.py"
    dict = test.read_py_file(file_path)
    test._append_markdown(test._format_dictionary_to_markdown(dict))
    test._append_markdown(test._format_dictionary_to_markdown(dict))
    print(test.markdown_master_document)
    pass
        
if __name__ == '__main__':
    main()