# Week 4 Day 3 — Codon Translation Engine & Genomic Sequence Analysis

## What I built today

- **`translate_dna(sequence)`**: A biological translation function that steps through a DNA sequence in triplets (`range(0, len, 3)`), extracts 3-base codons (`seq[i : i+3]`), looks them up in a 64-codon dictionary, and assembles the resulting amino acid peptide.
- **Real Genomic Integration**: Re-used our Week 4 Day 2 FASTA parser to process a real genomic dataset `gene.fna` (22,267 base pairs).
- **Tabular Peptide Export**: Successfully translated 7,422 amino acids and exported the structured report to `data/raw/translated_peptides.txt`.

## New syntax and concepts mastered

- **Stepping by triplets**:

  ```python
  for i in range(0, len(sequence) - 2, 3):
      codon = sequence[i : i + 3]
  ```

  - Starts at index 0, increments by 3 on each lap.
  - Slices a 3-base window: `sequence[i : i + 3]` where the ending index is excluded.

- **Defensive dictionary retrieval with `.get()`**:
  - `CODON_TABLE.get(codon, "X")`: Looks up the codon. If an ambiguous or non-standard base appears (like `N`), it safely returns `"X"` instead of crashing with a `KeyError`.
- **The FASTA boundary guard (`current_id is not None`)**:
  - Ensures Python does not attempt to save a nonexistent previous sequence when encountering the very first `>` header of the file.

## Biological relevance

DNA stores the genetic blueprint, but proteins execute cellular biochemistry. High-throughput sequencing outputs nucleotide strings, but identifying protein-coding potential requires computational translation across triplets. In eukaryotic genomes with introns and intergenic regions, translating raw genomic reads reveals Stop codon frequencies (such as the 382 stop codons in this un-spliced locus), showing where coding exons transition into non-coding sequences.
