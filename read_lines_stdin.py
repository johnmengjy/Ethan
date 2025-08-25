#!/usr/bin/env python3

import argparse
import sys
from typing import Iterable, Optional, TextIO


def iter_lines_from_stream(stream: TextIO) -> Iterable[str]:
    for line in stream:
        yield line


def iter_lines_from_file(path: str, encoding: str) -> Iterable[str]:
    with open(path, "r", encoding=encoding) as file_obj:
        for line in file_obj:
            yield line


def filter_contains(lines: Iterable[str], substring: Optional[str]) -> Iterable[str]:
    if not substring:
        yield from lines
        return
    for line in lines:
        if substring in line:
            yield line


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Read lines from a file or stdin (use '-' for stdin) and optionally filter by substring."
        )
    )
    parser.add_argument(
        "source",
        help="Path to input file, or '-' to read from stdin",
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="Text encoding for file input (ignored for stdin)",
    )
    parser.add_argument(
        "--contains",
        default=None,
        help="Only output lines that contain this substring",
    )
    args = parser.parse_args()

    if args.source == "-":
        source_lines = iter_lines_from_stream(sys.stdin)
    else:
        source_lines = iter_lines_from_file(args.source, args.encoding)

    for line in filter_contains(source_lines, args.contains):
        print(line, end="")


if __name__ == "__main__":
    main()

