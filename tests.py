# tests.py
import unittest
from functions.run_python_file import run_python_file

class TestGetFiles(unittest.TestCase):
    def setUp(self):
        self.run_python_file = run_python_file

    def print_result(self, label, result):
        print(f"Result for {label} directory:")
        if isinstance(result, str):
            # It's an error string, print directly
            print(result)
        print()  # blank line for spacing
    
    def test_mainpy_file(self):
        result = self.run_python_file("calculator","main.py")
        self.print_result("main.py", result)

    def test_main_file(self):
        result = self.run_python_file("calculator", "main.py", ["3 + 5"])
        self.print_result("main.py with attrs", result)

    def test_tests_file(self):
        result = self.run_python_file("calculator", "tests.py")
        self.print_result("tests.py", result)
    
    def test_outer_file(self):
        result = self.run_python_file("calculator","../main.py")
        self.print_result("../main.py", result)

    def test_nonexistent_file(self):
        result = self.run_python_file("calculator","nonexistent.py")
        self.print_result("nonexistent.py", result)

    def test_loremtxt_file(self):
        result = self.run_python_file("calculator","lorem.txt")
        self.print_result("lorem.txt", result)

if __name__ == "__main__":
    unittest.main()