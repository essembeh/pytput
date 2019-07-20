import os
import subprocess
import unittest
from pathlib import Path

TEST_FOLDER = Path(__file__).parent


class TestTput(unittest.TestCase):
    def __exec(self, *args):
        return list(filter(None, subprocess.check_output(args).decode().split("\n")))

    def test_tput_properties(self):
        expected_file = TEST_FOLDER / "executable.txt"
        lines = []
        lines += self.__exec(
            "pytput",
            "{0:bold,red} {1:underline,dim,yellow} {2:bg_purple,yellow,blink}",
            "This is",
            "a message",
            "with styles ;)",
        )
        lines += self.__exec(
            "pytput",
            "--force",
            "{0:bold,red} {1:underline,dim,yellow} {2:bg_purple,yellow,blink}",
            "This is",
            "a message",
            "with styles ;)",
        )
        lines += self.__exec(
            "pytput",
            "--force",
            "{0:bold,red} {1:underline,dim,yellow}\n{2:bg_purple,yellow,blink}",
            "This is",
            "a multiline message",
            "with styles ;)",
        )
        if os.getenv("PYTPUT_GEN_EXPECTED") == "1":
            with expected_file.open("w") as fp:
                for l in lines:
                    fp.write(l + "\n")
            self.skipTest("Expected file generated")

        self.assertTrue(expected_file.exists())
        with expected_file.open() as fp:
            expected_lines = list(filter(None, fp.read().split("\n")))
            self.assertEqual(lines, expected_lines)
