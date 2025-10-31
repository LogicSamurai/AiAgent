# # tests.py
# import unittest
# from functions.get_files_info import get_files_info

# class TestGetFiles(unittest.TestCase):
#     def setUp(self):
#         self.get_files_info = get_files_info

#     def print_result(self, label, result):
#         print(f"Result for {label} directory:")
#         if isinstance(result, str):
#             # It's an error string, print directly
#             print(result)
#         else:
#             # It's a list of lines, join normally
#             print("\n".join(result))
#         print()  # blank line for spacing
    
#     def test_current_directory(self):
#         result = self.get_files_info("calculator")
#         self.print_result("current", result)

#     def test_pkg_directory(self):
#         result = self.get_files_info("calculator", "pkg")
#         self.print_result("'pkg'", result)

#     def test_bin_directory(self):
#         result = self.get_files_info("calculator", "/bin")
#         self.print_result("'/bin'", result)

#     def test_parent_directory(self):
#         result = self.get_files_info("calculator", "../")
#         self.print_result("'../'", result)

# if __name__ == "__main__":
#     unittest.main()


# tests.py
import unittest
from functions.get_file_content import get_file_content

class TestGetFiles(unittest.TestCase):
    def setUp(self):
        self.get_file_content = get_file_content

    def print_result(self, label, result):
        print(f"Result for {label} directory:")
        if isinstance(result, str):
            # It's an error string, print directly
            print(result)
        print()  # blank line for spacing
    
    def test_current_directory(self):
        result = self.get_file_content("calculator","lorem.txt")
        self.print_result("current", result)

    # def test_pkg_directory(self):
    #     result = self.get_file_content("calculator", "pkg")
    #     self.print_result("'pkg'", result)

    # def test_bin_directory(self):
    #     result = self.get_file_content("calculator", "/bin")
    #     self.print_result("'/bin'", result)

    # def test_parent_directory(self):
    #     result = self.get_file_content("calculator", "../")
    #     self.print_result("'../'", result)

if __name__ == "__main__":
    unittest.main()