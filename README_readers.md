## Line-by-line text file readers (Python)

Scripts added:

- `read_lines_iter.py`: Uses file iteration (`for line in f`).
- `read_lines_readline.py`: Uses `readline()` in a loop.
- `read_lines_readlines.py`: Uses `readlines()` then iterates the list.
- `read_lines_pathlib.py`: Uses `pathlib.Path.open()` and iteration.

Each script supports:

- `--encoding` (default `utf-8`)
- `--errors` (`strict`, `ignore`, `replace`)
- `--strip-newline` (remove trailing `\n` before printing)
- `--skip-empty` (skip empty lines; if used with `--strip-newline`, emptiness is after stripping)

### Usage

```bash
python3 read_lines_iter.py /path/to/file.txt
python3 read_lines_iter.py /path/to/file.txt --strip-newline --skip-empty
python3 read_lines_readline.py /path/to/file.txt --encoding utf-8 --errors replace
python3 read_lines_readlines.py /path/to/file.txt
python3 read_lines_pathlib.py /path/to/file.txt
```

### Notes

- Iteration (`for line in f`) is generally the most memory-efficient and Pythonic.
- `readlines()` loads all lines into memory; avoid for very large files.
- Use `--errors replace` if you encounter decoding issues with unknown encodings.

