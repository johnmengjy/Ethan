#!/usr/bin/env python3

import argparse
from typing import TextIO


def stream_lines(file_obj: TextIO, show_line_numbers: bool) -> None:
    for line_index, line in enumerate(file_obj, start=1):
        if show_line_numbers:
            print(f"{line_index}\t{line.rstrip('\n')}")
        else:
            print(line, end="")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Read a text file line by line and print to stdout."
    )
    parser.add_argument("file", help="Path to the input .txt file")
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="File text encoding (default: utf-8)",
    )
    parser.add_argument(
        "--number",
        action="store_true",
        help="Prefix each line with its 1-based line number",
    )
    args = parser.parse_args()

    with open(args.file, "r", encoding=args.encoding) as file_obj:
        stream_lines(file_obj, show_line_numbers=args.number)


if __name__ == "__main__":
    main()

