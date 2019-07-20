import os
import unittest
from pathlib import Path

from pytput import tput_format
from pytput.formatter import TputFormatter

TEST_FOLDER = Path(__file__).parent


class TestFormatter(unittest.TestCase):
    def test_text(self):
        expected_file = TEST_FOLDER / "fomatter.txt"
        cf = TputFormatter(check_tty=False)
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
            l1 = cf.format("{0:" + s1 + "} {1:" + s2 + "}!", "Hello", "World")
            l2 = tput_format(
                "{0:" + s1 + "} {1:" + s2 + "}!", "Hello", "World", check_tty=False
            )
            self.assertEqual(l1, l2)
            lines.append(l1)

        if os.getenv("PYTPUT_GEN_EXPECTED") == "1":
            with expected_file.open("w") as fp:
                for l in lines:
                    fp.write(l + "\n")
            self.skipTest("Expected file generated")

        self.assertTrue(expected_file.exists())
        with expected_file.open() as fp:
            expected_lines = list(filter(None, fp.read().split("\n")))
            self.assertEqual(lines, expected_lines)
