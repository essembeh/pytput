from pytput import TputFormatter


def tput_format(message: str, *args, check_tty=True, **kwargs):
    """
    Used to format a string with keywords, use string.Formatter spec when needed
    """
    return TputFormatter(check_tty=check_tty).format(message, *args, **kwargs)


def tput_print(message: str, *args, **kwargs):
    """
    Format the given message with tc_format and print it
    """
    print(tput_format(message, *args, **kwargs))
