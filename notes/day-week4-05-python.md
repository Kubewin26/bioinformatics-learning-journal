# Week 4 Day 5 — 6-Frame Translation, Reverse Complement Mechanics, and TSV Export

## What 6-frame translation is

- In living cells, DNA is a double-stranded anti-parallel helix ($5' \rightarrow 3'$ and $3' \rightarrow 5'$).
- Ribosomes and RNA Polymerases can only read in the $5' \rightarrow 3'$ direction, but protein-coding genes can be located on **either** the forward strand or the reverse strand.
- **Why there are 6 frames**:
  - The **Forward Strand** ($5' \rightarrow 3'$) has 3 possible reading frames depending on where translation starts: Frame +1 (offset 0), Frame +2 (offset 1), and Frame +3 (offset 2).
  - The **Reverse Strand** runs in the opposite direction. To read it $5' \rightarrow 3'$, we must take the reverse complement of the forward strand. Scanning that opposite strand in triplets gives another 3 frames: Frame -1 (offset 0), Frame -2 (offset 1), and Frame -3 (offset 2).
  - $3 \text{ Forward} + 3 \text{ Reverse} = \mathbf{6\text{ Total Reading Frames}}$. Every genomic locus on Earth has exactly 6 possible frames.

---

## What I built today

- **Terminal-Driven File Creation**: Created `scripts/python/six_frame_translator.py` using the Linux `touch` command in the WSL terminal to build command-line fluency over GUI clicking.
- **`get_reverse_complement(sequence)`**: Implemented Watson-Crick base-pairing via `COMPLEMENT_MAP` dictionary and reversed the string backwards right-to-left using `[::-1]`.
- **`calculate_gc(sequence)`**: Computed locus GC percentage rounded to 2 decimal places using `round(((g + c) / len) * 100, 2)`.
- **`translate_frame(sequence, offset)`**: Modular engine that steps through any DNA strand by triplets starting from a specific offset (0, 1, or 2) and returns the full peptide sequence.
- **`get_longest_peptide(protein_sequence)`**: Slices translated proteins wherever stop codons occur (`protein.split('*')`) to isolate uninterrupted peptide blocks.
- **6-Frame Automated Loop**: Packaged the 6 frames into a list of dictionaries (`frames_to_process`) to loop through all forward and reverse strands cleanly.
- **Structured TSV Exporter**: Outputted multi-frame summary data using tab (`\t`) delimiters and newlines (`\n`) to `data/raw/six_frame_summary.tsv`.

---

## The Mental Models & Cheat Codes Mastered Today

### 1. The Cheat Code for Negatives in Python (`None` & `continue`)

- **Think of `None` as "Empty Hands"**:
  - `current_id = None` means my hands are empty at the start of the file.
  - `if current_id is not None:` means: _"Are my hands currently holding a previous gene?"_
  - On line 1 of the file, my hands are empty, so it evaluates to `False` (do not save ghost data). When hitting the next header, my hands are holding the first gene, so it evaluates to `True` (save the completed gene into the dictionary).
- **Think of `continue` as the "Skip Button"**:
  - `if not line: continue` asks: _"Is this line blank?"_ If `True`, it skips the rest of the loop lap immediately and grabs the next line from the file.

### 2. The File Handle Analogy

- `with open(...) as file_handle:` acts like a spring mechanism that automatically closes the file even if errors occur.
- The `file_handle` is like a micropipette dipping into a test tube—it streams lines one by one without pouring the entire 22,000-base content into memory all at once.

### 3. Slicing and Splitting Idiom (`line[1:].split()[0]`)

When parsing headers like `>seq_001 BRCA1 gene`:

1. `line[1:]`: Slices off position 0 (the `>`), leaving `"seq_001 BRCA1 gene"`.
2. `.split()`: Chops the string by whitespace into a list of words: `['seq_001', 'BRCA1', 'gene']`.
3. `[0]`: Grabs the very first word (`'seq_001'`), discarding description text.

### 4. Slicing Between Stop Codons (`.split('*')`)

```python
fragments = protein_sequence.split("*")
longest_fragment = max(fragments, key=len)
```

Splitting a protein by `*` divides the sequence into chunks between stop codons. Using `max(fragments, key=len)` instantly finds the longest uninterrupted peptide block without any stop signs.

### 5. TSV Formatting Mechanics

- Columns are separated by the tab escape character `\t`.
- Rows terminate with the newline escape character `\n`.
- This creates structured data that can be parsed directly by Pandas, Excel, or R.

---

## Biological findings & experimental results

Executed against the 22,267 bp locus (`NC_065922.1:c19844476-19822210`):

- **GC Content:** 37.14% (indicating an AT-rich insect genome).
- **Frame Distribution:**
  - **Frame +1:** 7,422 aa | 382 stops | **Longest Peptide: 463 aa**
  - **Frame +2:** 7,422 aa | 421 stops | Longest Peptide: 153 aa
  - **Frame +3:** 7,421 aa | 415 stops | Longest Peptide: 120 aa
  - **Frame -1:** 7,422 aa | 435 stops | Longest Peptide: 99 aa
  - **Frame -2:** 7,422 aa | 381 stops | Longest Peptide: 215 aa
  - **Frame -3:** 7,421 aa | 393 stops | Longest Peptide: 139 aa

### Scientific Conclusion:

Frames +2, +3, -1, and -3 exhibit high stop-codon density with maximum peptide lengths below 160 aa, typical of non-coding genomic background. **Frame +1 on the Forward Strand is the decisive biological champion**, containing an unbroken 463-amino-acid peptide (`GPKHCNVFDSAPANKPKLSDEVRSR...`), providing clear evidence of active protein-coding architecture.
