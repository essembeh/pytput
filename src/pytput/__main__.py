import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter

from pytput import __title__, __version__
from pytput.style import Style
from pytput.utils import tput_print, tput_format

EXAMPLE_STR = '{"Hello":red,bg_yellow,bold} {0:blink,underline,green}!'
EXAMPLES = (
    (
        "{prog} '{fmt}' 'World'".format(prog=__title__, fmt=EXAMPLE_STR),
        tput_format(EXAMPLE_STR, "World", check_tty=False),
    ),
    (
        "{prog} '{fmt}' 'World' | tee /tmp/pytput.test".format(
            prog=__title__, fmt=EXAMPLE_STR
        ),
        "Hello World!",
    ),
    ("cat /tmp/pytput.test", "Hello World!"),
    (
        "{prog} --force '{fmt}' 'World' | tee /tmp/pytput.test".format(
            prog=__title__, fmt=EXAMPLE_STR
        ),
        tput_format(EXAMPLE_STR, "World", check_tty=False),
    ),
    ("cat /tmp/pytput.test", tput_format(EXAMPLE_STR, "World", check_tty=False)),
)


def _get_epilog():
    out = ["examples"]
    for cmd, output in EXAMPLES:
        out += ("  $ " + cmd, "  " + output)
    out += ("", "available styles:", ", ".join(map(str.lower, Style.all_styles())))
    return "\n".join(out)


def main(sysargs=None):
    parser = ArgumentParser(
        prog=__title__,
        epilog=_get_epilog(),
        formatter_class=RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--version",
        action="version",
        version="{0} version {1}".format(__title__, __version__),
    )
    parser.add_argument(
        "-f",
        "--force",
        dest="check_tty",
        default="True",
        action="store_false",
        help="force styles and colors. By default, if STDOUT is not a TTY (ex: in a pipe or redirected in a file), colors and styles are disabled",
    )
    parser.add_argument("format", help="python str.format-like format")
    parser.add_argument("args", nargs="*", help="format arguments")
    args = parser.parse_args(sysargs)
    try:
        tput_print(args.format, *args.args, check_tty=args.check_tty)
    except BaseException as e:
        print(Style.RED.apply(e), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
