import sys
import unittest
from io import StringIO
from os import getenv
from pathlib import Path

from pytput.__main__ import main

TEST_FOLDER = Path(__file__).parent


class TestExecutable(unittest.TestCase):
    def __exec(self, *args, external=False, check=True):
        oldstdout = sys.stdout
        try:
            sys.stdout = StringIO()
            rc = main(args)
            if check:
                self.assertEqual(rc, 0)
            return sys.stdout.getvalue().splitlines()
        except BaseException as e:
            if isinstance(e, SystemExit):
                self.assertTrue(e.code == 0 or not check)
            else:
                self.fail(e)
        finally:
            sys.stdout = oldstdout

    def test_tput_properties(self):
        expected_file = TEST_FOLDER / "executable.txt"
        lines = []
        lines += self.__exec(
            "{0:bold,red} {1:underline,dim,yellow} {2:bg_purple,yellow,blink}",
            "This is",
            "a message",
            "with styles ;)",
        )
        lines += self.__exec(
            "--force",
            "{0:bold,red} {1:underline,dim,yellow} {2:bg_purple,yellow,blink}",
            "This is",
            "a message",
            "with styles ;)",
        )
        lines += self.__exec(
            "--force",
            "{0:bold,red} {1:underline,dim,yellow}\n{2:bg_purple,yellow,blink}",
            "This is",
            "a multiline message",
            "with styles ;)",
        )
        if getenv("PYTPUT_GEN_EXPECTED") == "1":
            with expected_file.open("w") as fp:
                fp.write("\n".join(lines))
            self.skipTest("Expected file generated")

        self.assertTrue(expected_file.exists())
        with expected_file.open() as fp:
            expected_lines = list(filter(None, fp.read().splitlines()))
            self.assertEqual(lines, expected_lines)

    def test_error(self):
        self.__exec("--help")
        self.__exec("Hello {1}", "Test", check=False)
