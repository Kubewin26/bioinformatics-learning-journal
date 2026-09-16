# Week 3 Day 5 — File Reading and Writing

## What I learned

- **File handling with `open()`**: How Python connects to files stored on the disk. The three essential access modes are:
  - `"r"` (read): Opens an existing file to inspect its data line-by-line without altering it.
  - `"w"` (write): Creates a new file or completely wipes/overwrites an existing file to write fresh output.
  - `"a"` (append): Adds new lines to the very end of an existing file without deleting past contents.
- **Why `with open()` is essential**: In professional coding, opening a file leaves a system connection open. Using `with open(...) as f:` is a context manager that automatically and safely closes the file when the loop finishes, even if the program crashes.
- **Why `.strip()` is mandatory**: Every line read from a file ends with an invisible `\n` (newline character from pressing Enter). If not removed with `.strip()`, string operations, length counts, and outputs get distorted by unexpected line breaks and spaces.
- **Guarding with `if line:`**: Checks whether the line actually contains characters. An empty line evaluates to `False`, so `if line:` prevents the script from crashing or running calculations on blank spaces.
- **Tab-Separated Values (TSV)**: A standard, lightweight tabular format where columns are separated by tabs (`\t`). Unlike CSVs, TSVs are heavily favored in bioinformatics because genomic sequences or annotation descriptions might contain commas, which break CSV parsing.
- **Escape characters**:
  - `\t`: Inserts a horizontal tab character (aligns data into columns).
  - `\n`: Inserts a newline character (equivalent to pressing Enter).

## Commands I used

- `touch scripts/python/file_reading.py` — created the Day 5 script.
- `python3 scripts/python/file_reading.py` — executed the file streaming and TSV writing pipeline.
- `cat data/raw/gc_results.txt` — printed the contents of the generated TSV file directly to the terminal.
- `git add`, `git commit -m "..."`, `git push` — staged and committed Day 5 scripts and datasets.

## Biological relevance

In real genomics, sequences are never hardcoded inside a Python script. High-throughput sequencing outputs millions of reads into large FASTA or FASTQ files. Streaming files line-by-line using `with open()` is the only way to process massive gigabyte-scale genomic datasets without running out of RAM or crashing the computer. File I/O is the bridge that turns a standalone Python script into a real-world pipeline.
