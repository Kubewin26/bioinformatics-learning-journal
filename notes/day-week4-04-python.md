# Week 4 Day 4 — Scanning Reading Frames & Open Reading Frame (ORF) Finder

## What I built today

- **`validate_dna(sequence)`**: A Quality Control tool that counts standard nucleotides (`A, C, G, T`) and detects ambiguous bases (like `N`) before algorithmic scanning.
- **`find_orfs_in_frame(sequence, frame_offset)`**: A biological state machine implementing the "Light Switch" algorithm to scan a reading frame in steps of 3 (`range(frame_offset, len - 2, 3)`), detecting Start (`ATG`) to Stop (`TAA`, `TAG`, `TGA`) windows.
- **`find_all_orfs(sequence)`**: An automated multi-frame collector scanning offsets 0, 1, and 2, packaging every discovered ORF into a structured dictionary record.
- **The Longest ORF Selector**: Applied the Chapter 5 Maximum Loop Pattern from _Python for Everybody_ to extract the biological coding champion from a 22,267 bp locus (`NC_065922.1:c19844476-19822210`).
- **`data/raw/orf_summary.txt`**: Exported structured report ranking candidate coding regions and detailing the champion gene.

---

## Conceptual breakthroughs & mental models

### 1. What Computational Biology Actually Is

In a living cell, enzymes like Helicase, RNA Polymerase, and Ribosomes physically bind, unwind, scan, and step along DNA in triplets. In computational biology, we don't have enzymes or cellular machinery. We translate the physical laws of molecular biology written in plain human English into computational instructions (strings, slices, loops, and dictionaries) so the computer can replicate biological behavior in silicon.

### 2. Algorithmic Thinking: The "Tea & House Cleaning" Model

Computers cannot interpret vague human statements like _"Find the genes"_ or _"Make a cup of tea"_. As bioinformaticians, algorithmic thinking means decomposing a high-level goal into the recipe:

1. Define the ingredients (constants, codon tables, inputs).
2. Clean and prepare the ingredients (FASTA parsing, stripping whitespace, validation).
3. Execute micro-steps in strict logical order (step by 3, check start codon, check stop codon, extract slice, store record).

### 3. Separation of Concerns

A general FASTA parser should **never** crash or reject non-`ACGT` sequences by default. FASTA files can hold RNA (`U`), proteins (20 amino acids), or sequencing reads with ambiguities (`N`). The parser's sole job is handling the text format (headers vs sequences). Biological validation is decoupled into its own independent QC tool.

### 4. Slicing Coordinate Mechanics (`end_index = i + 3`)

Python string slicing (`seq[start : stop]`) excludes the upper index. When an in-frame stop codon begins at index `i`, its 3 nucleotides reside at `i`, `i + 1`, and `i + 2`. To include the third base of the stop codon, the slice boundary must extend to $i + 3$.

### 5. Why There Are Only 3 Forward Reading Frames

Because codons are read in non-overlapping triplets, every starting position is defined by $n \pmod 3$:

- Offset 0 $\rightarrow$ Frame 1
- Offset 1 $\rightarrow$ Frame 2
- Offset 2 $\rightarrow$ Frame 3
- Offset 3 $\rightarrow$ $3 \pmod 3 = 0$ (Returns to Frame 1, shifted by one codon).

---

## Biological findings & experimental results

Executed against the 22,267 bp _Bactrocera neohumeralis_ locus:

- **Purity:** 22,267 bp scanned (100% standard A, C, G, T; zero ambiguous bases).
- **Candidate ORFs:** 283 candidate ORFs detected across the locus:
  - Frame 1: 97 candidate ORFs
  - Frame 2: 91 candidate ORFs
  - Frame 3: 95 candidate ORFs
- **The Champion ORF (Primary Protein-Coding Gene):**
  - **Reading Frame:** Frame 1
  - **Coordinates:** Base 18,652 to 19,965
  - **Length:** 1,314 nucleotides (438 amino acids)
  - **Terminal Codon:** `TAA` (Stop: `*`)
  - **Peptide sequence:** `MRIKDEILKL...`

This 1,314 bp ORF is three times longer than the second-longest candidate (441 bp), providing decisive computational proof of the active protein-coding sequence in this genomic region.
