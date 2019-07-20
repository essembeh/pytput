import unittest

from pytput import Tput


class TestTput(unittest.TestCase):
    def test_tput_properties(self):
        tput = Tput()
        self.assertEqual(tput.colors, 256)
        self.assertGreater(tput.colums, 1)
        self.assertGreater(tput.lines, 1)

    def test_tput_sequences(self):
        tput = Tput()

        self.assertEqual(r"'\x1b7'", repr(tput.sc))
        self.assertEqual(r"'\x1b8'", repr(tput.rc))
        self.assertEqual(r"'\x1b[H'", repr(tput.home))
        self.assertEqual(r"'\n'", repr(tput.cud1))
        self.assertEqual(r"'\x1bM'", repr(tput.cuu1))
        self.assertEqual(r"'\x1b[?25l'", repr(tput.civis))
        self.assertEqual(r"'\x1b[34h\x1b[?25h'", repr(tput.cnorm))
        self.assertEqual(r"'\x1b[2m'", repr(tput.dim))
        self.assertEqual(r"'\x1b[1m'", repr(tput.bold))
        self.assertEqual(r"'\x1b[4m'", repr(tput.smul))
        self.assertEqual(r"'\x1b[24m'", repr(tput.rmul))
        self.assertEqual(r"'\x1b[7m'", repr(tput.rev))
        self.assertEqual(r"'\x1b[5m'", repr(tput.blink))
        self.assertEqual(r"'\x1b[3m'", repr(tput.smso))
        self.assertEqual(r"'\x1b[23m'", repr(tput.rmso))
        self.assertEqual(r"'\x1b[m\x0f'", repr(tput.sgr0))
        self.assertEqual(r"'\x1b[?1049h'", repr(tput.smcup))
        self.assertEqual(r"'\x1b[?1049l'", repr(tput.rmcup))
        self.assertEqual(r"'\x1b[K'", repr(tput.el))
        self.assertEqual(r"'\x1b[1K'", repr(tput.el1))
        self.assertEqual(r"'\x1b[J'", repr(tput.ed))
        self.assertEqual(r"'\x1b[H\x1b[J'", repr(tput.clear))

        for x, y in zip(range(0, 10), range(10, 20)):
            self.assertEqual(
                r"'\x1b[{x};{y}H'".format(x=x + 1, y=y + 1), repr(tput.cup(x, y))
            )

        for color in range(0, 8):
            self.assertEqual(r"'\x1b[4{0}m'".format(color), repr(tput.setab(color)))
            self.assertEqual(r"'\x1b[3{0}m'".format(color), repr(tput.setaf(color)))
