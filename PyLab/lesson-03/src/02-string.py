from argparse import ArgumentParser
from typing import Any


def print_obj_info(obj: Any):
    value: Any = obj
    type_name: str = type(obj).__name__
    bytes_taken: int = obj.__sizeof__()
    print(f"Value: {value}\tType: {type_name}\tBytes taken: {bytes_taken}")


def example01(args):
    print_obj_info(args.s)
    lyrics = """
Because of you,
I never stray too far from the sidewalk.
"""
    print_obj_info(lyrics)

    file_path = r".\lyrics.txt"
    with open(file_path, "r") as f:
        lyrics = f.read()
    print_obj_info(lyrics)


def exercise01(name: str, singer: str, duration: float, lyrics: str):
    format_str = """{:#>10}
This is the information of the song:
Song name:\t{:0<15}
Singer:\t\t{:0<15}
Duration:\t{:0<15.2f}
Lyrics: 
{}
{:#>10}"""
    print(format_str.format("", name, singer, duration, lyrics, ""))


def main(args):
    exercise01(
        "Because of you",
        "Kelly Clarkson",
        3.41,
        "Because of you,\nI never stray too far from the sidewalk.",
    )


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--s", type=str, help="any string", default="Hello")
    args = arg_parser.parse_args()
    main(args)
