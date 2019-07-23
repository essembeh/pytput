import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter

from pytput.style import Style
from pytput.utils import tput_format, tput_print, print_red
from pytput import __title__, __version__

EXAMPLES = (
    (
        "pytput '{0:red,bg_yellow,bold} {1:blink,underline,green}!' 'Hello' 'World'",
        tput_format(
            "{0:red,bg_yellow,bold} {1:blink,underline,green}!", "Hello", "World"
        ),
    ),
    (
        "pytput '{0:red,bg_yellow,bold} {1:blink,underline,green}!' 'Hello' 'World' | tee /tmp/pytput.test",
        "Hello World!",
    ),
    ("cat /tmp/pytput.test", "Hello World!"),
    (
        "pytput --force '{0:red,bg_yellow,bold} {1:blink,underline,green}!' 'Hello' 'World' | tee /tmp/pytput.test",
        tput_format(
            "{0:red,bg_yellow,bold} {1:blink,underline,green}!", "Hello", "World"
        ),
    ),
    (
        "cat /tmp/pytput.test",
        tput_format(
            "{0:red,bg_yellow,bold} {1:blink,underline,green}!", "Hello", "World"
        ),
    ),
)


def _get_epilog():
    out = ["examples"]
    for cmd, output in EXAMPLES:
        out += ("  $ " + cmd, "  " + output)
    out += ("", "available styles:", ", ".join([s.name.lower() for s in Style]))
    return "\n".join(out)


def main():
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
    parser.add_argument("format", nargs=1, help="python str.format-like format")
    parser.add_argument("args", nargs="*", help="format arguments")
    args = parser.parse_args()
    try:
        tput_print(args.format[0], *args.args, check_tty=args.check_tty)
    except BaseException as e:
        print_red(str(e), file=sys.stderr)
        exit(2)


if __name__ == "__main__":
    main()
