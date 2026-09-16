# Week 3 Day 6 — QC Pipeline Mini-Project

## What I built

A complete, automated Sequence Quality Control (QC) pipeline (`week3_qc_pipeline.py`).

- **Input**: A raw file containing DNA reads (`data/raw/test_sequences.txt`), including normal sequences, short fragments, extreme GC-rich/poor sequences, and reads with sequencing errors.
- **Processing**: The pipeline streams each read, strips whitespace, skips blank rows, calculates GC percentage, classifies GC content (HIGH, LOW, NORMAL), categorizes read length (TOO_SHORT, SHORT, ACCEPTABLE), and flags biological issues (such as ambiguous `N` bases or 0%/100% GC).
- **Output**: A live terminal summary of each read and a permanently saved TSV report (`data/raw/qc_report.txt`) recording sequence metrics and pass/fail statuses.

## Concepts I applied

- **String manipulation & slicing**: Using `.count()` to tally nucleotides, `.strip()` to clean inputs, and `line[:12]...` to create tidy truncated previews.
- **Modular functions (`def` / `return`)**: Breaking logic into dedicated, testable functions (`calculate_gc`, `classify_gc`, `classify_length`, `flag_sequence`).
- **Conditionals (`if` / `elif` / `else`)**: Implementing decision logic and thresholds for biological classifications.
- **File I/O (`with open`)**: Concurrently opening an output file for writing while streaming an input file for reading.
- **Loop control**: Using `for line in f:` to iterate through data, and understanding `continue` to skip invalid or blank lines.
- **TSV formatting**: Constructing clean, tab-separated tables using `\t` and `\n` with formatted floating-point numbers (`:.1f`).

## What `pass` is and why it exists

In Python, `pass` is a placeholder statement that does literally nothing. Because Python enforces strict indentation blocks, you cannot leave a function or an `if` block completely empty without triggering an `IndentationError`. Writing `pass` allows a developer to sketch out function skeletons or empty conditions during development without crashing the code. _(In our QC pipeline, "PASS" was also used as our biological status string to indicate a sequence that passed all QC filters)._

## What I found difficult and how I solved it

- **`if line:` vs `if not line:` logic**: Initially, I inverted the meaning of `if line:` as checking whether the line was empty. My mentor walked me through the bouncer/apple analogy: Python evaluates content as `True` and emptiness as `False`. Thus, `if line:` asks _"Does content exist? If yes, proceed"_, whereas `if not line:` asks _"Is this line blank? If yes, skip/continue"_. Simply, the if line: statement condition is 'Is there data here? Is there something here?' If there's something here, True, then you proceed to do what is in the indented lines of code. If it is False, meaning that there's no data there (it is empty), then you don't do it. So the if not line: is the one that asks, 'Is this line blank?' If it is blank (True), stop there / skip. If that statement is False, meaning that it is NOT blank, then you continue.
- **The line continuation slash `\`**: Learned that putting `\` at the end of a long mathematical expression lets a calculation cleanly span multiple lines without Python throwing a syntax error.
- **Function organization**: Clarified that defining functions with `def` only stores the instructions in memory; the actual execution order is determined by where and when those functions are called in the main loop.

## What this pipeline would look like on real data

- **Real input**: In a real research project, `sequences.txt` would be a multi-gigabyte FASTQ file containing millions of short reads directly from an Illumina or Oxford Nanopore sequencer, accompanied by Phred quality scores.
- **Downstream next steps**:
  - The `qc_report.txt` would be used to filter the dataset: passing reads would be piped into sequence aligners (like BWA or Bowtie2) to map against a reference genome.
  - Reads flagged as `FAIL` (due to ambiguous `N`s or extreme adapter contamination) would be discarded or trimmed using tools like Trimmomatic or fastp.
