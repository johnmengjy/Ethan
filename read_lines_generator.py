#!/usr/bin/env python3

import argparse
from typing import Generator, Iterable


def read_lines(
    path: str,
    *,
    encoding: str = "utf-8",
    skip_blank: bool = False,
    strip_newline: bool = False,
) -> Generator[str, None, None]:
    with open(path, "r", encoding=encoding) as file_obj:
        for line in file_obj:
            if skip_blank and not line.strip():
                continue
            yield line.rstrip("\n") if strip_newline else line


def write_lines(lines: Iterable[str]) -> None:
    for line in lines:
        print(line, end="" if line.endswith("\n") else "\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generator-based line reader with common options."
    )
    parser.add_argument("file", help="Path to the input .txt file")
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="File text encoding (default: utf-8)",
    )
    parser.add_argument(
        "--skip-blank",
        action="store_true",
        help="Skip lines that are empty or whitespace only",
    )
    parser.add_argument(
        "--strip-newline",
        action="store_true",
        help="Strip the trailing newline from each line before printing",
    )
    args = parser.parse_args()

    lines = read_lines(
        args.file,
        encoding=args.encoding,
        skip_blank=args.skip_blank,
        strip_newline=args.strip_newline,
    )
    write_lines(lines)


if __name__ == "__main__":
    main()

