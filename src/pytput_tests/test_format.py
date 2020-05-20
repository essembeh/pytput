import unittest
from os import getenv
from pathlib import Path

from pytput.formatter import TputFormatter
from pytput.utils import tput_format

TEST_FOLDER = Path(__file__).parent


class TestFormatter(unittest.TestCase):
    def test_text(self):
        expected_file = TEST_FOLDER / "fomatter.txt"
        lines = []
        for s1, s2 in (
            ("", ".1"),
            ("bold", "dim"),
            ("underline", "blink"),
            ("standout", "reverse"),
            ("black", "red"),
            ("green", "yellow"),
            ("blue", "purple"),
            ("cyan", "white"),
            ("bg_black", "bg_red"),
            ("bg_green", "bg_yellow"),
            ("bg_blue", "bg_purple"),
            ("bg_cyan", "bg_white"),
            (
                "reset,bold,underline,blink,green,bg_blue",
                "bold,underline,blink,green,bg_blue,reset",
            ),
            ("red,green,cyan", "standout,reverse"),
        ):
            fmt = "{'Hello':" + s1 + "} {0:" + s2 + "}!"
            l1 = TputFormatter(check_tty=False).format(fmt, "World")
            l2 = tput_format(fmt, "World", check_tty=False)
            self.assertEqual(l1, l2)
            lines.append(l1)

        if getenv("PYTPUT_GEN_EXPECTED") == "1":
            with expected_file.open("w") as fp:
                fp.write("\n".join(lines) + "\n")
            self.skipTest("Expected file generated")

        self.assertTrue(expected_file.exists())
        with expected_file.open() as fp:
            expected_lines = list(filter(None, fp.read().splitlines()))
            self.assertEqual(lines, expected_lines)
