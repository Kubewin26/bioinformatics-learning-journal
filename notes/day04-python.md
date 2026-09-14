# Week 3, Day 4: Loops, Lists, Enumeration, and Pipeline Automation

**Date:** September 14, 2026  
**Author:** Winner Kubeyinje  
**Topic:** Iteration, Data Collections, and Formatted Output

---

## 1. Objectives Completed Today

- Learned how to store multiple biological sequences in a Python `list`.
- Replaced manual repetitive code with a `for` loop to automate sequence processing.
- Used `enumerate()` to track both sequence index and value simultaneously.
- Adopted modern Python **f-strings** (`f"..."`) for clean, readable output formatting.
- Integrated `classify_gc()` decision logic inside a loop to build an end-to-end classification pipeline in `scripts/python/loops.py`.
- Successfully pushed all code and documentation to GitHub.

---

## 2. Core Concepts & Mental Models

### Lists (`[...]`)

- An ordered collection of items separated by commas inside square brackets:

```python
sequences = ["ATCG", "GCGC", "ATAT"]
```

- In bioinformatics, lists allow us to hold thousands of sequencing reads in memory under a single variable name.

### The `for` Loop (`for item in collection:`)

- Loops automate repetitive tasks. Instead of writing 1,000 lines of code for 1,000 sequences, a loop runs the exact same block of instructions on each sequence.
- **Iteration Variable (`seq`)**: A temporary variable that takes on the value of each element in the list one at a time, from start to finish.

### The `enumerate()` Function & `i + 1`

- A standard loop only gives you the item (`seq`).
- `enumerate(sequences)` gives you two items at once: the position index (`i`) and the value (`seq`).
- **Bridging the 0-Index Gap**: Because Python counts from 0 (`0, 1, 2...`), we use `{i + 1}` so human beings read `Seq 1, Seq 2, Seq 3...` instead of `Seq 0`.

### Formatted Strings (f-strings: `f"..."`)

- Placing an `f` before the opening quote tells Python: _"Evaluate any expressions inside curly braces `{}` and insert the real values directly into the string."_
- Cleaner and less error-prone than chaining multiple commas and quotes inside `print()`.
- **Example:**

```python
f"Seq {i+1}: {classification} ({gc:.1f}%) — Length: {len(seq)} bp"
```

---

## 3. The Power of Pipeline Integration

Today’s script unified **Functions** (reusable logic), **Conditionals** (decision-making), and **Loops** (scaling to datasets).

### Verification Results:

- **Seq 1 (50.0% GC)** -> Correctly classified as **Normal GC**.
- **Seq 2 (100.0% GC)** -> Correctly classified as **High GC**.
- **Seq 3 (0.0% GC)** -> Correctly classified as **Low GC**.
- **Seq 4 (50.0% GC)** -> Correctly classified as **Normal GC**.
- **Seq 5 (50.0% GC)** -> Correctly classified as **Normal GC**.

---

## 4. Next Steps (Week 3, Days 5 & 6)

- **Day 5**: Packaging our nucleotide counting logic into a fully reusable function.
- **Day 6**: The completed `dna_counter.py` mini-project (the capstone deliverable for Month 1 Python).
