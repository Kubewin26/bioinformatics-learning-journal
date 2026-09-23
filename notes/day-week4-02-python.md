# Week 4 Day 2 — FASTA Parsing, Mental Models, and Integrated Quality Control

## What FASTA format is

- The universal standard file format in computational biology used across NCBI, Ensembl, and UniProt.
- **Structure**:
  - Header lines start with a greater-than symbol `>` followed by a sequence identifier and optional descriptions (e.g., `>seq_001 Homo sapiens BRCA1`).
  - Sequence lines follow the header and contain nucleotide or amino acid sequences.
  - Unlike simple text files, a single biological sequence in a FASTA file can be split across multiple wrapped lines. A parser must concatenate these lines until the next `>` header is encountered.

## What I built today

- **`parse_fasta(filepath)`**: A standalone FASTA parser that reads multi-line sequences from a file and returns a structured dictionary where keys are sequence IDs and values are complete reconstructed sequences (`{id: sequence}`).
- **Multi-line Concatenation**: Managed split lines using string accumulation (`current_seq = current_seq + line`).
- **Boundary Handling**: Saved the completed sequence when a new `>` header was detected, and added a post-loop safety check (`if current_id is not None:`) to ensure the final record in the file is not lost.
- **Integrated FASTA QC Pipeline**: Combined the parsed FASTA output directly with Week 3 QC functions (`calculate_gc`, `classify_gc`, `flag_sequence`) to print a clean, structured quality control table on the terminal.

## The Mental Model for Pipeline Architecture (The Kitchen Recipe)

To overcome feeling stuck when faced with a coding task, I established a 5-stage mental model with my mentor:

1. **Tools (`def`)**: What specific tools/functions do I need to prepare? (e.g., GC calculator, filter).
2. **Prep (Variables & Containers)**: Where is the data coming from/going, and what empty containers (`{}`, `[]`, counters) will store it?
3. **Open (`with open`)**: How do I safely stream the input file line-by-line?
4. **Inspect (`for line in f:` + `if`)**: How do I clean the line (`.strip()`), distinguish headers from sequences (`startswith(">")`), and apply my Stage 1 tools?
5. **Serve (`write` / `print`)**: How do I output the final report to disk or terminal?

- **Formula**: _Tools → Prep → Open → Inspect → Serve._

## New syntax and methods learned today

- `line.startswith(">")`: Evaluates whether a string begins with a specific prefix.
- `line[1:].split()[0]`: The standard FASTA ID extraction idiom:
  1. `line[1:]`: Slices off the leading `>`.
  2. `.split()`: Chops the header into a list of words separated by spaces.
  3. `[0]`: Selects the first word (the crisp sequence ID), discarding extra descriptions.
- `current_id is not None`: Checks if a sequence record is currently active in memory.

## Biological relevance

Real genomic sequencing experiments never store reads in plain single-line text files. FASTA files downloaded from public repositories often format sequences in 60- or 80-character wrapped lines. Being able to programmatically parse multi-line FASTA files into memory structures is the prerequisite for all downstream genomic alignment, assembly, and variant calling.
