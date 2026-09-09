# Week 3, Day 1: First Python Scripts & Sequence Fundamentals

**Date:** September 9, 2026  
**Author:** Winner Kubeyinje  
**Commit Hash:** `f1b2903`

---

## 1. Objectives for Today

- Set up and confirm Python 3.12 and VS Code Python extension in WSL.
- Create first working Python script (`hello.py`).
- Create `dna_basics.py` to calculate sequence metrics from first principles.
- Push clean, version-controlled scripts to GitHub.

---

## 2. Scripts Created

### `scripts/python/hello.py`

- Demonstrated basic terminal output using the built-in `print()` function.
- Established standard professional header comments (`#`).

### `scripts/python/dna_basics.py`

- Stored a 24-base DNA sequence (`"ATCGATCGTAGCTAGCTAGCATCG"`) in a string variable.
- Used `len()` to compute sequence length ($O(1)$ constant time lookup).
- Used the string method `.count()` to tally each individual nucleotide (A, T, G, C).
- Computed **GC Content** using the formula:
  $$\text{GC\%} = \frac{\text{Count}(G) + \text{Count}(C)}{\text{Total Length}} \times 100$$
- Output:
  - Total Length: 24 bases
  - A: 6 | T: 6 | G: 6 | C: 6
  - GC Content: 50.0%

---

## 3. Key Concepts Mastered

### Computer Science & Python Mechanics

- **Variables**: Named memory references that hold data.
- **Strings (`str`)**: Immutable sequences of characters enclosed in quotes.
- **Functions vs. Methods**:
  - `len()` is a built-in function taking an argument from outside.
  - `.count()` is a method belonging to string objects (called via the dot operator).
- **Operator Precedence (PEMDAS)**: Parentheses are mandatory in `(count_G + count_C) / sequence_length * 100` so addition happens before division.
- **Data Types**: Division with `/` automatically produces a `float` (50.0).

### Biological Significance

- **GC Content & Thermal Stability**: G-C pairs have 3 hydrogen bonds compared to 2 for A-T pairs, requiring higher temperatures ($T_m$) to denature.
- **Chargaff's Observation**: Balanced counts ($A=T=6$, $G=C=6$) reflect base-pairing symmetry.
- **Practical Application**: Primer design for PCR, detecting sequencing contamination, and taxonomy profiling in metagenomics.

---

## 4. Next Steps (Week 3, Day 2)

- Deep-dive into Python strings: zero-indexing, negative indexing, and slicing (`seq[start:stop:step]`).
- Extracting specific codons and sub-sequences.
- Reading: _Python for Everybody_ Chapters 1 & 2.
