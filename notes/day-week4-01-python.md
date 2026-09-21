# Week 4 Day 1 — Dictionaries and Biological Lookup Tables

## What a dictionary is

- **My Analogy**: A dictionary is like a room filled with labeled containers or people wearing name tags. You don't have to look for someone by what seat they are sitting in; you simply call out their name tag (the **Key**) and you instantly get what they have inside or who they are (the **Value**). It is a container of defined variables where the label is the key and the content is the value (e.g., `ribosome` → `protein factory`).
- **Difference from a list**:
  - **List**: Elements are ordered by integer positions (`0, 1, 2...`). You must know _where_ an item sits.
  - **Dictionary**: Elements are accessed directly by their unique **Key**. Order does not matter; lookup is instant ($O(1)$ constant time).

## What I built today

- **`complement_map`**: A dictionary storing the base-pairing rules of molecular biology (Chargaff's rules). It maps `"A"` to `"T"`, `"T"` to `"A"`, `"G"` to `"C"`, and `"C"` to `"G"`.
- **`get_complement()`**: Loops through any input DNA sequence character-by-character, looks up each nucleotide's complementary pair in `complement_map`, and glues the new bases into a complete complementary strand.
- **`get_reverse_complement()`**: First calls `get_complement()` to generate the complementary bases, then uses `[::-1]` to reverse the strand from end to start. This is essential because double-stranded DNA is antiparallel, and sequencing data from the opposite strand is read in the 5' to 3' reverse direction.
- **`nucleotide_frequency()`**: A dynamic counting function using the `if key in dict` pattern. If a nucleotide has been seen before, it adds 1 to its count; if it is seen for the first time, it initializes the count to 1. Returns a clean histogram dictionary of nucleotide counts.

## New syntax learned today

- **Dictionary creation**: Defined using curly braces `{}` with `key: value` pairs (e.g., `complement_map = {"A": "T", ...}`).
- **Key lookup**: Accessing a value by placing the key in square brackets: `dict["key"]`.
- **Looping with `.items()`**: Iterating through key-value pairs simultaneously (`for base, count in frequencies.items():`), unpacking both the key and value on every lap.
- **Dynamic frequency counter pattern**:
  ```python
  if key in dict:
      dict[key] += 1
  else:
      dict[key] = 1
  ```
- **String reversal with step**: `seq[::-1]` (utilizes `[start:end:step]` with a `-1` step to step backwards through a string).

## Biological relevance

- **Antiparallel sequencing reads**: DNA sequencers only read in the 5' to 3' direction. When analyzing genomic reads from the reverse (minus) strand, bioinformatics pipelines must calculate the reverse complement to align them properly against the reference genome.
- **Codon translation in Month 2**: In translation, 64 mRNA triplets correspond to 20 amino acids. Without dictionaries, we would need 64 clumsy `if/elif` statements. With a dictionary, a codon lookup table (`codon_table["ATG"] = "Methionine"`) translates genetic code into proteins in a single line of code.
