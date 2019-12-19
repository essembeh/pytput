import unittest

from pytput.tput import Tput


class TestTput(unittest.TestCase):
    def test_tput_properties(self):
        self.assertEqual(Tput.colors(), 256)
        self.assertGreater(Tput.colums(), 1)
        self.assertGreater(Tput.lines(), 1)

    def test_tput_sequences(self):
        self.assertEqual(r"'\x1b7'", repr(Tput.sc()))
        self.assertEqual(r"'\x1b8'", repr(Tput.rc()))
        self.assertEqual(r"'\x1b[H'", repr(Tput.home()))
        self.assertEqual(r"'\n'", repr(Tput.cud1()))
        self.assertEqual(r"'\x1b[A'", repr(Tput.cuu1()))
        self.assertEqual(r"'\x1b[?25l'", repr(Tput.civis()))
        self.assertEqual(r"'\x1b[?12l\x1b[?25h'", repr(Tput.cnorm()))
        self.assertEqual(r"'\x1b[2m'", repr(Tput.dim()))
        self.assertEqual(r"'\x1b[1m'", repr(Tput.bold()))
        self.assertEqual(r"'\x1b[4m'", repr(Tput.smul()))
        self.assertEqual(r"'\x1b[24m'", repr(Tput.rmul()))
        self.assertEqual(r"'\x1b[7m'", repr(Tput.rev()))
        self.assertEqual(r"'\x1b[5m'", repr(Tput.blink()))
        self.assertEqual(r"'\x1b[7m'", repr(Tput.smso()))
        self.assertEqual(r"'\x1b[27m'", repr(Tput.rmso()))
        self.assertEqual(r"'\x1b(B\x1b[m'", repr(Tput.sgr0()))
        self.assertEqual(r"'\x1b[?1049h\x1b[22;0;0t'", repr(Tput.smcup()))
        self.assertEqual(r"'\x1b[?1049l\x1b[23;0;0t'", repr(Tput.rmcup()))
        self.assertEqual(r"'\x1b[K'", repr(Tput.el()))
        self.assertEqual(r"'\x1b[1K'", repr(Tput.el1()))
        self.assertEqual(r"'\x1b[J'", repr(Tput.ed()))
        self.assertEqual(r"'\x1b[H\x1b[2J\x1b[3J'", repr(Tput.clear()))
        self.assertEqual(r"'\x1b[8m'", repr(Tput.invis()))

        for x, y in zip(range(0, 10), range(10, 20)):
            self.assertEqual(
                r"'\x1b[{x};{y}H'".format(x=x + 1, y=y + 1), repr(Tput.cup(x, y))
            )

        for color in range(0, 8):
            self.assertEqual(r"'\x1b[4{0}m'".format(color), repr(Tput.setab(color)))
            self.assertEqual(r"'\x1b[3{0}m'".format(color), repr(Tput.setaf(color)))
