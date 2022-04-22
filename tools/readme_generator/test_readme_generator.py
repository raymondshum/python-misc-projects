import unittest
from readme_generator import ReadmeGenerator

class ReadmeGeneratorTestCase(unittest.TestCase):
    
    def setUp(self):
        self.readme_generator = ReadmeGenerator()
        
        self.easy_path = "C:\\Users\\rshum\\Documents\\CSUMB\\Misc Projects\\python\\leetcode\\problems\\easy"
        self.medium_path = "C:\\Users\\rshum\\Documents\\CSUMB\\Misc Projects\\python\\leetcode\\problems\\medium"
        self.hard_path = "C:\\Users\\rshum\\Documents\\CSUMB\\Misc Projects\\python\\leetcode\\problems\\hard"
        self.false_path = "C:\\Users\\rshum\\Documents\\CSUMB\\Misc Projects\\python\\leetcode\\problems\\false"

        self.true_file = "C:\\Users\\rshum\\Documents\\CSUMB\\Misc Projects\\python\\leetcode\\problems\\easy\\1_two_sum.py"
        self.false_file = "C:\\Users\\rshum\\Documents\\CSUMB\\Misc Projects\\python\\leetcode\\problems\\easy\\1_three_sum.py"
    
    def test_directory_is_valid(self):
        self.assertTrue(self.readme_generator._directory_is_valid(self.easy_path))
        self.assertFalse(self.readme_generator._directory_is_valid(self.false_path))
    
    def test_add_directories(self):
        
        self.readme_generator.add_directory(self.easy_path)
        self.assertListEqual(self.readme_generator.target_directories, [self.easy_path])
        
        self.readme_generator.add_directory(self.medium_path)
        self.assertListEqual(self.readme_generator.target_directories, [self.easy_path, self.medium_path])
        
        with self.assertRaises(Exception):
            self.readme_generator.add_directory(self.false_path)
    
    def test_directory_is_valid(self):
        self.assertTrue(self.readme_generator._file_is_valid(self.true_file))
        self.assertFalse(self.readme_generator._file_is_valid(self.false_file))
        
if __name__ == '__main__':
    unittest.main()