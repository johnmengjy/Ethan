#!/usr/bin/env python3

import argparse
import sys
from typing import Optional


def parse_arguments(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read a text file line by line using readline() and print to stdout."
    )
    parser.add_argument("path", help="Path to the input text file")
    parser.add_argument("--encoding", default="utf-8", help="File encoding (default: utf-8)")
    parser.add_argument(
        "--errors",
        default="strict",
        choices=("strict", "ignore", "replace"),
        help="Decoding error handling (default: strict)",
    )
    parser.add_argument(
        "--strip-newline",
        action="store_true",
        help="Strip trailing newline from each line before printing",
    )
    parser.add_argument(
        "--skip-empty",
        action="store_true",
        help="Skip empty lines (after stripping if --strip-newline is set)",
    )
    return parser.parse_args(argv)


def main() -> int:
    args = parse_arguments()

    try:
        with open(args.path, "r", encoding=args.encoding, errors=args.errors) as file_obj:
            while True:
                raw_line = file_obj.readline()
                if raw_line == "":
                    break

                line_to_print = raw_line
                if args.strip_newline:
                    line_to_print = line_to_print.rstrip("\n")

                if args.skip_empty:
                    if args.strip_newline:
                        if line_to_print == "":
                            continue
                    else:
                        if line_to_print == "\n":
                            continue

                if args.strip_newline:
                    print(line_to_print)
                else:
                    print(line_to_print, end="")
    except FileNotFoundError:
        print(f"Error: File not found: {args.path}", file=sys.stderr)
        return 2
    except PermissionError:
        print(f"Error: Permission denied: {args.path}", file=sys.stderr)
        return 3
    except UnicodeError as exc:
        print(f"Error: Decoding failed: {exc}", file=sys.stderr)
        return 4

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

