# Week 3, Day 2: Strings, Slicing, and Reusable Functions

**Date:** September 10, 2026  
**Author:** Winner Kubeyinje  
**Topic:** String Manipulation, Data Types, and Function Architecture

---

## 1. Objectives Completed Today

- Completed and submitted the "Hello World" function on Exercism with `return`, unlocking the Python track.
- Explored data type behavior and operator overloading in Python interactive mode (`python3`).
- Built and executed `scripts/python/strings.py` (string concatenation, slicing, methods, and type inspection).
- Built and executed `scripts/python/functions.py` (created a reusable `calculate_gc()` function and verified predictions).
- Successfully committed all code to version control on GitHub.

---

## 2. Core Concepts & Reflections

### Data Types (`int`, `float`, `str`) & Why They Matter

Python behaves completely differently depending on the data type of the object. The data type determines what operators actually do:

- **Integer (`int`)**: Whole numbers (e.g., `6`, `4`).
- **Float (`float`)**: Numbers with decimal points (e.g., `50.0`, `0.5`).
- **String (`str`)**: Text surrounded by quotes (e.g., `"6"`, `"4"`, `"Homo sapiens"`).

#### The Interactive Proof:

- Running `6 + 4` gives `10` because Python sees two integers and performs **arithmetic addition**.
- Running `"6" + "4"` gives `"64"` because Python sees two strings and performs **concatenation** (gluing text together).
  Data types dictate how Python treats the element versus the object in memory.

---

### String Slicing & The Zero-Indexing Rule

- **What Slicing Is**: In its simplest form, slicing means cutting a specific portion or part out of something.
- **The Zero-Index Rule**: Python always starts counting positions from **`0`**, not `1`. The first letter in every string lives at position `0`.
- **The Half-Open Interval (`[start:stop]`)**:
  - Python includes the start index, but **excludes** the stop index.
  - Slicing `dna[6:9]` starts at position 6 and extracts indices **6, 7, and 8**, stopping right before index 9.
  - **The Length Formula**: $\text{stop} - \text{start} = \text{length}$. In `dna[6:9]`, $9 - 6 = 3$ bases are extracted.
  - In `strings.py`, codon 1 was sliced using `dna[0:3]` (`"ATC"`) and codon 2 using `dna[3:6]` (`"GAT"`).

---

### Functions: Anatomy & Mechanics

A function is a set of instructions encoded into Python so that you can reuse it at any later time without rewriting the logic.

- **`def` (Define)**: This tells Python: _"I want to create a new custom function with this name and these instructions."_
- **Parameters (`sequence`)**: The placeholder slot where inputs enter the function.
- **Indentation**: The 4 spaces tell Python which lines belong inside the function's instruction manual.
- **`return`**: This is critical. It tells Python: _"After completing this entire computation, do not trash the result—bring it back to me so I can see it, print it, or use it."_

---

### The `calculate_gc()` Function & Reusability

The `calculate_gc(sequence)` function demonstrated the true power of automation:

- We configured and wrote the formula once:
  $$\text{GC\%} = \frac{\text{G count} + \text{C count}}{\text{Total Length}} \times 100$$
- We then effortlessly called it on three different test sequences with zero repeated code:
  - `seq1 = "ATCGATCG"` $\rightarrow$ Predicted: **50%** | Output: **50.0%** ✅
  - `seq2 = "GCGCGCGC"` $\rightarrow$ Predicted: **100%** | Output: **100.0%** ✅
  - `seq3 = "ATATATATAT"` $\rightarrow$ Predicted: **0%** | Output: **0.0%** ✅

In real bioinformatics pipelines, this same function can analyze millions of sequencing reads across entire genomes.

---

## 3. Daily Reflection & Surprises

- **The Power of Modern Tooling**: I was surprised by how smoothly writing code can be with VS Code predicting context, syntax, and biological names (like suggesting `"Homo sapiens"` after `BRCA1`).
- **Mindset Shift**: Python is not as intimidating or difficult as I originally anticipated. While AI assistance and predictions make writing code faster, my focus remains on understanding every single line so I have the knowledge and craft at my fingertips.

---

## 4. Next Steps (Week 3, Day 3)

- Dive into **Lists and Loops**: Converting sequences into nucleotide lists and iterating over them using `for base in sequence:`.
- Evening Reading: _Python for Everybody_ (Dr. Chuck) Chapter 2.
