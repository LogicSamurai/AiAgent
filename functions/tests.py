# tests.py
import unittest
from get_files_info import get_files_info

class TestGetFiles(unittest.TestCase):
    def setUp(self):
        self.get_files_info = get_files_info

    def test_current_directorty(self):
        result = self.get_files_info("calculator")
        print(f"Result for current directory:\n{result}")
        print()

    def test_pkg_directory(self):
        result = self.get_files_info("calculator","pkg")
        print(f"Result for 'pkg' directory:\n{result}")
        print()

    def test_bin_directory(self):
        result = self.get_files_info("calculator","/bin")
        print(f"Result for '/bin' directory:\n{result}")
        print()

    def test_parent_directory(self):
        result = self.get_files_info("calculator","../")
        print(f"Result for '../' directory:\n{result}")
        print()


if __name__ == "__main__":
    unittest.main()