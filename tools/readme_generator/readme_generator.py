import os
from typing import List

class ReadmeGenerator:
    
    DELIMITER = "\"\"\""
    
    def __init__(self):
        self.target_directories = []
        self.markdown_master_document = ""
    
    def add_directory(self, directory_path: str):
        if not self._directory_is_valid(directory_path=directory_path):
            raise Exception(f"Directory does not exist: {directory_path}")
        
        self.target_directories.append(directory_path)
    
    def _directory_is_valid(self, directory_path: str) -> bool:
        return os.path.isdir(directory_path)
    
    def read_py_file(self, file_path: str):
        if not self._file_is_valid(file_path=file_path):
            raise Exception("File does not exist: {file_path}")
        
        raw_text = self._extract_text(file_path=file_path)
        processed_text = self._format_list_to_text(raw_text=raw_text)
        return (content_dictionary := self._build_content_dictionary(processed_text=processed_text, file_path=file_path))

    def _build_content_dictionary(self, processed_text: str, file_path: str) -> dict[str, str]:
        content = {}
        content["File Name"] = file_path.rsplit(os.sep, 1)[1]
        processed_text = processed_text.replace("Key Point: ", "")
        
        # TODO: turn this into an exception
        if processed_text:
            content["Key Point"],processed_text =processed_text.split("Link: ", 1)
            content["Link"],processed_text =processed_text.split("Method: ", 1)

            #TODO: Extract and call in another generalized processing step
            # Processes docstring link into .md link
            raw_text = content.get("Link", "")
            problem_name = self._get_file_name_from_path(content.get("File Name", ""))
            content["Link"] = f"[{problem_name}]({raw_text})"

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
        return os.path.isfile(path=file_path)
    
    def write_readme(self, directory_path: str):
        with open(f"{directory_path}README.md", "w+") as file:
            file.truncate(0)
            file.write(f"# Leetcode DocStrings\n\nThis README file was autogenerated with readme_generator.py.\n\n")
            file.write(self._get_toc(directory_path=directory_path))
            file.write(self.markdown_master_document)

    def _get_toc(self, directory_path: str):
        file_paths = self._get_all_files_in_directory(directory_path=directory_path)
        file_names = [file_path.rsplit(os.sep, 1)[1].replace(".", "") for file_path in file_paths]
        md_string = "# Contents\n"
        for file_name in file_names:
            md_string += f"- [{file_name[:-2]}](#{file_name})\n" # Truncate py suffix
        md_string += "\n"
        return md_string
    
    def _get_file_name_from_path(self, file_path: str):
        return " ".join(file_path.removesuffix(".py").split("_")[1:])
    
    def _format_dictionary_to_markdown(self, content_dictionary: dict) -> str:
        markdown = f"# {content_dictionary['File Name']}\n\n"
        for key, value in content_dictionary.items():
            markdown += f"**{key}**: {value}\n\n"
        markdown += "\n[Return to Top](#contents)\n\n---\n\n"
        return markdown
    
    def _append_markdown(self, markdown_snippet: str):
        self.markdown_master_document += markdown_snippet
    
    def _get_all_files_in_directory(self, directory_path: str) -> list:
        files_in_directory = []
        
        for file in os.listdir(directory_path):
            if file.endswith(".py"):
                files_in_directory.append(os.path.join(directory_path, file))
                
        # sort by digits in filename
        # https://stackoverflow.com/questions/36259763/sort-list-of-string-based-on-number-in-string
        files_in_directory.sort(key=lambda name: int(''.join(filter(str.isdigit, name))))
        return files_in_directory
    
    def _sort_list_by_numeric_value(self, list: list[str]) -> list[str]:
        list.sort(key=lambda name: int(''.join(filter(str.isdigit, name))))
    
    def write_docstring_to_md(self, directory_path: str):
        files = self._get_all_files_in_directory(directory_path=directory_path)
        print(files)

        for file in files:
            dict = self.read_py_file(file)
            markdown = self._format_dictionary_to_markdown(content_dictionary=dict)
            self._append_markdown(markdown_snippet=markdown)

        print(self.markdown_master_document)
        self.write_readme(directory_path=directory_path)

        # TODO: Extract to "clear buffer" method
        self.target_directories = []
        self.markdown_master_document = ""
    
    def write_all_directories_to_md(self, directory_paths: list[str]):
        for directory_path in directory_paths:
            self.write_docstring_to_md(directory_path=directory_path)
    
def main():
    leetcode_directory_path =  "/workspaces/python-misc-projects/leetcode/problems"
    directories = [
        leetcode_directory_path + "/" + "easy/",
        leetcode_directory_path + "/" + "medium/",
    ]
    test = ReadmeGenerator()
    test.write_all_directories_to_md(directory_paths=directories)

if __name__ == '__main__':
    main()